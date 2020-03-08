from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os
import time
import platform

def js(code, driver, asynchro=False):
    try:
        if asynchro:
            return driver.execute_async_script(''+code.strip())
        else:
            return driver.execute_script(''+code.strip())
    except BaseException:
        return None

def runJSLib(path, driver, *argus, template={}, asynchro=False):
    try:
        with open(dirPath()+path, 'r') as code_js: 
            code = code_js.read()
            if template:
                for key in template:
                    value = str(template[key])
                    code = code.replace('#:'+key+':#', value)
            if len(argus) > 0:
                if asynchro:
                    # !!!
                    return driver.execute_async_script(code, *argus)
                else:
                    return driver.execute_script(code, *argus)
            else:
                if asynchro:
                    return driver.execute_async_script(code)
                else:
                    return driver.execute_script(code)
    except TimeoutException:
        pass

def waitingForPageLoadingComplete(driver,timeout):
    return runJSLib('jslib/ready.js', driver, template={'timeout':timeout}, asynchro=True)

def event(driver, element, mode):
    return runJSLib('jslib/event.js', driver, element, mode, asynchro=False)

def importingJQuery(driver):
    return runJSLib('jslib/jquery-3.4.1.js', driver, asynchro=False)

def isJQueryImported(driver):
    return js('try{return jQuery.fn.jquery==="3.4.1"}catch{return false;}', driver, asynchro=False)

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
        driver.set_script_timeout(3600*24)
        driver.set_page_load_timeout(timeout)
        return driver
    except BaseException:
        pass

def clear(driver):
    runJSLib('jslib/clear.js', driver)

def openURL(url, driver, timeout=30, jquery=True):
    try:
        marker = beforeLeavePage(driver)
        driver.get(url)
        wt = waitingForPageLoadingComplete(driver, timeout)
        if wt and jquery:
            importingJQuery(driver)
        onload(marker, driver)
        return wt
    except TimeoutException:
        pass

def selector(query, driver, timeout=30):
    try:
        return runJSLib('jslib/selector.js', driver, template={'query':query, 'timeout':timeout}, asynchro=True)
    except TimeoutException:
        pass

def beforeLeavePage(driver):
    return runJSLib('jslib/define_refresh_mark.js', driver)

def onload(marker, driver):
    if not marker:
        marker = ''
    while not js("let marker='"+marker+"';return (marker.length?window[marker]===undefined:true) && document.readyState==='complete'", driver):
        time.sleep(0.1)
