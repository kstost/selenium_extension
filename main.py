#------------------------------------------------------------------------------------------------------
# 필요한 모듈 임포트
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from easysqlite import EasySQLite
from crawlext import *
import time 
#------------------------------------------------------------------------------------------------------
# 브라우저 환경 설정
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("lang=ko_KR")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
#------------------------------------------------------------------------------------------------------

# 크롤링 코드 작성
# 여기서 부터 크롤링을 위한 코드를 작성하면 됩니다

# 크롬브라우저를 실행합니다
driver = openChrome(chrome_options)

# 주소창에 주소를 입력하고 접속합니다
# 접속을 하면 웹브라우저는 서버로부터 페이지를 전송받고 화면에 표현하는 과정을 거칩니다. 이것이 완료된 후에야 True 가 리턴됩니다
# 완료되기 전에는 계속 if 에서 머무릅니다
# 기본적으로 30초가 지나도 완료되지 않으면 False 가 리턴됩니다.
# 이 시간을 임의로 정하고 싶다면 openURL('주소', driver, timeout=60) 이렇게 원하는 만큼 정해줄 수 있습니다
if openURL('https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/', driver):

    # 페이지의 로드가 완료된 후에 내가 가져오길 원하는 데이터가 담긴 엘리먼트를 선택합니다
    # 로드가 완료된 직후에는 아직 이 엘리먼트가 존재하지 않을 수도 있습니다

    # 아래와 같은 방법으로 내가 원하는 엘리먼트를 선택해줍니다
    # a 라고 쓰면 태그이름이 a 인것들을 선택하겠다는 의미입니다
    # 
    # 이 표현은 querySelectorAll 에서 사용하는 것과 동일합니다
    # https://developer.mozilla.org/ko/docs/Web/API/Document/querySelectorAll
    # 
    # 엘리먼트가 아직 존재하지 않는다면 존재할때까지 기다립니다
    # 기본적으로 30초가 지나도 존재하지 않으면 None 을 리턴합니다
    # openURL 과 동일한 방법으로 timeout 을 지정할 수 있습니다
    #
    # 선택하고자 하는 요소가 한개이던 한개이상이던 리턴값의 타입은 언제나 list 입니다
    # body 같은것을 선택하면 문서내에 한개이므로 요소가 한개인 list 가 리턴됩니다
    selected = selector('a',driver)

    # 선택된 요소 한개 한개는 WebElement 라고 부릅니다
    # https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html
    # 문서에서 관련 API 를 참고할 수 있습니다
    for element in selected:
        print(element.get_attribute('href'))
    print('-'*80)

    # 위 코드의 selected = selector('a',driver) 와 동일한 방법으로써 아래와 같이도 가능합니다
    # 한가지 차이점은 a 가 존재하지 않는다면 생길때까지 기다려주지 않고 바로 리턴합니다
    selected = js("return document.querySelectorAll('a')", driver)
    for element in selected:
        print(element.get_attribute('href'))
    print('-'*80)

    # 위 코드의 selected = selector('a',driver) 와 동일한 또 다른 방법으로써 아래와 같이도 가능합니다
    # 이 방법도 역시 a 가 존재하지 않는다면 생길때까지 기다려주지 않고 바로 리턴합니다
    # 이 방법은 웹페이지 내에 jquery 가 적용 되어있는 경우 사용 가능합니다
    # jquery 사용 가능 여부는 isJQueryImported 함수로 확인 할 수 있습니다
    # jquery 가 적용되있지 않은 사이트의 경우 openURL로 불러오는 시점에 기본적으로 적용시킵니다
    if isJQueryImported(driver):
        selected = js("return $('a').pure()", driver)
        for element in selected:
            print(element.get_attribute('href'))
        print('-'*80)

    # 이 코드는 셀레늄 웹드라이버에서 제공하는 API 입니다
    # 이 방법도 역시 a 가 존재하지 않는다면 생길때까지 기다려주지 않고 바로 리턴합니다
    selected = driver.find_elements_by_tag_name('a')
    for element in selected:
        print(element.get_attribute('href'))
    print('-'*80)

    # 이 코드는 셀레늄 웹드라이버에서 제공하는 API 입니다
    # 이 방법은 selector() 함수처럼 a 엘리먼트가 존재해서 선택되어질수 있을때까지 기다려준다는점이 동일합니다.
    # 코드 중에 있는 30은 기다려주는 시간입니다
    selected = WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
    for element in selected:
        print(element.get_attribute('href'))
    print('-'*80)

    # 화면을 지웁니다 (모든 엘리먼트가 제거됩니다)
    # 지워준 후 selector('a',driver) 를 실행하면 찾고자 하는건 존재하지 않고, 또 생겨날 일도 없기 때문에 계속 기다리다가 타임아웃 이후에 None 을 리턴할것입니다
    clear(driver)

    # 타임아웃을 1초로해서 실행해보겠습니다
    selected = selector('a',driver, timeout=1)

    # None이 확인될것입니다
    print(selected)

    # 또 다른 페이지로의 이동을 원하면 이렇게 해줍니다.
    print('-'*80)
    if openURL('https://ko.wikipedia.org/wiki/%EC%9B%B9_%ED%81%AC%EB%A1%A4%EB%9F%AC', driver):
        print(js("return location.href+' 로 접속했습니다';", driver))
        try:
            selected = selector('.mw-parser-output ul', driver)
            for li in selected[3].find_elements_by_tag_name('li'):
                print(li.text)
        except BaseException:
            pass


        # 페이지의 높이를 얻어올 수 있습니다
        height = js("return document.documentElement.scrollHeight", driver)
        print('페이지의 높이는 %s pixel 입니다' % height)
        print('-'*80)

        # 링크를 클릭할 수 있습니다
        # 링크를 누르면 웹페이지가 이동하게되는데요, 이동하게될때는 이동을 유발하는 코드의 전후에 아래와 같은 모습으로 작성해주는것을 권장드립니다
        # 이렇게 해주는 이유는 페이지 이동후 로딩완료를 보장받기 위함이며 onload 함수가 리턴되는 시점이 이동하고 난 뒤 다음페이지의 로딩이 완료된 시점입니다
        # openURL 함수를 이용해 페이지를 이동한 경우에는 자체적으로 이 처리를 해주므로 생략해도 좋습니다
        leaveMarker = beforeLeavePage(driver)
        js("document.querySelectorAll('.mw-wiki-logo')[0].click()", driver)
        onload(leaveMarker, driver, jquery=True)
        print(js("return location.href+' 로 접속했습니다';", driver))

        # 아래와 같은 이동도 마찬가지 입니다
        leaveMarker = beforeLeavePage(driver)
        js("location.href='https://www.naver.com/';", driver)
        onload(leaveMarker, driver, jquery=True)
        print(js("return location.href+' 로 접속했습니다';", driver))

# 모든 작업 완료 후 크롬브라우저를 끕니다
driver.quit()
