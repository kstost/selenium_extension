from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import os
import platform

def js(code, driver, asyncro=False):
    try:
        if asyncro:
            return driver.execute_async_script(''+code.strip())
        else:
            return driver.execute_script(''+code.strip())
    except BaseException:
        return None

def runJSLib(path, driver, template={}, asynchro=False):
    try:
        with open(dirPath()+path, 'r') as code_js: 
            code = code_js.read()
            if template:
                for key in template:
                    value = str(template[key])
                    code = code.replace('#:'+key+':#', value)
            if asynchro:
                return driver.execute_async_script(code)
            else:
                return driver.execute_script(code)
    except TimeoutException:
        pass

def waitingForPageLoadingComplete(driver,timeout):
    return runJSLib('jslib/ready.js', driver, template={'timeout':timeout}, asynchro=True)

def importingJQuery(driver):
    runJSLib('jslib/jquery-3.4.1.js', driver, asynchro=False)
    return True

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
        clear(driver)
        driver.get(url)
        wt = waitingForPageLoadingComplete(driver, timeout)
        if wt and jquery:
            importingJQuery(driver)
        return wt
    except TimeoutException:
        pass

def selector(query, driver, timeout=30):
    try:
        return runJSLib('jslib/selector.js', driver, template={'query':query, 'timeout':timeout}, asynchro=True)
    except TimeoutException:
        pass
