from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os
import time
import platform

def readfile(file):
    rt = []
    if os.path.isfile(file):
        f = open(file, 'r', encoding='utf-8')
        while True:
            line = f.readline()
            if not line:
                break
            rt.append(line)
        f.close()
    return ''.join(rt)

def compile(code):
    code = code.split('\n')
    ncodeline = []
    for line in code:
        candidate = line.strip()
        start = candidate[:5]
        end = candidate[-6:]
        path = ''
        if start == "(['#:" and end == ":#']);":
            path = candidate[5:].split(':')[0]
        if len(path) > 0:
            filepath = dirPath() + path
            ncodeline.append('/* ['+filepath+'] */')
            ncodeline.append(''+compile(readfile(filepath))+'')
            ncodeline.append('/* [/'+filepath+'] */')
        else:
            ncodeline.append(line)
    return '\n'.join(ncodeline)

def jsa(code, driver):
    return js(code, driver, asynchro=True)
    
def js(code, driver, asynchro=False):
    try:
        code = code.strip()
        if os.path.isfile(code):
            code = readfile(code)
        code = compile(code)
        _code = readfile(dirPath() + 'jslib/console_shell.js').replace("(['#:code:#']);", code).strip()
        rtnnn = None
        if asynchro:
            rtnnn = driver.execute_async_script(_code)
        else:
            rtnnn = driver.execute_script(_code)
        return rtnnn
    except BaseException as e:
        print('js:Error: '+str(e))
        return None

def runJSLib(path, driver, *argus, template={}, asynchro=False):
    try:
        code = readfile(dirPath() + path)
        if template:
            for key in template:
                value = str(template[key])
                code = code.replace('#:'+key+':#', value)
        if len(argus) > 0:
            if asynchro:
                return driver.execute_async_script(code, *argus)
            else:
                return driver.execute_script(code, *argus)
        else:
            if asynchro:
                return driver.execute_async_script(code)
            else:
                return driver.execute_script(code)
    except BaseException as e:
        print('runJSLib:Error: '+str(e))
        pass

def waitingForPageLoadingComplete(driver,timeout):
    return runJSLib('jslib/ready.js', driver, template={'timeout':timeout}, asynchro=True)

def changeselect(driver, element, mode):
    return runJSLib('jslib/changeselectelement.js', driver, element, mode, asynchro=False)

def event(driver, element, mode):
    return runJSLib('jslib/event.js', driver, element, mode, asynchro=False)

def importingJQuery(driver):
    return runJSLib('jslib/jquery-3.4.1.js', driver, asynchro=False)

def isJQueryImported(driver):
    return js('return (typeof jQuery) !== "undefined";', driver, asynchro=False)

def dirPath():
    return os.path.dirname(os.path.realpath(__file__))+'/'

def openChrome(chrome_options, timeout=30):
    drivers = {
        'windows': 'chromedriver',
        'darwin': 'chromedriver',
        'linux': 'chromedriver'
    }
    try:
        pla = platform.system().lower()
        driv = drivers[pla]
        driver = webdriver.Chrome(executable_path=dirPath()+'./drivers/'+pla+'/'+driv, options= chrome_options)
        driver.set_script_timeout(3600*(24*365*10))
        driver.set_page_load_timeout(timeout)
        return driver
    except BaseException as e:
        print('openChrome:Error: '+str(e))
        pass

def clear(driver):
    runJSLib('jslib/clear.js', driver)

def openURL(url, driver, timeout=30, jquery=True):
    try:
        marker = beforeLeavePage(driver)
        driver.get(url)
        wt = waitingForPageLoadingComplete(driver, timeout)
        onload(marker, driver, jquery=jquery)
        return wt
    except BaseException as e:
        print('openURL:Error: '+str(e))
        pass

def selector(query, driver, timeout=30):
    try:
        return runJSLib('jslib/selector.js', driver, template={'query':query, 'timeout':timeout}, asynchro=True)
    except BaseException as e:
        print('selector:Error: '+str(e))
        pass

def beforeLeavePage(driver):
    return runJSLib('jslib/define_refresh_mark.js', driver)

def onload(marker, driver, jquery=True):
    if not marker:
        marker = ''
    while not js("let marker='"+marker+"';return (marker.length?window[marker]===undefined:true) && document.readyState==='complete'", driver):
        time.sleep(0.1)
    if jquery and not isJQueryImported(driver):
        importingJQuery(driver)
