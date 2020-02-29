# selenium_extension

사용법은 main.py 파일의 크롤링부분 코드에 원하는 크롤링을 위한 코드를 작성하여 터미널등에서 실행합니다  
$ python3 main.py  

```python
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
    # 이 표현은 제이쿼리 셀렉터 방법을 따릅니다
    # 이 선택표현을 쓰는 방법은 구글에 "제이쿼리 셀렉터" 라고 검색하면 많이 찾을 수 있습니다
    # https://zetawiki.com/wiki/JQuery_%EC%85%80%EB%A0%89%ED%84%B0
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

    # 화면을 지웁니다 (모든 엘리먼트가 제거됩니다)
    # 지워준 후 selector('a',driver) 를 실행하면 찾고자 하는건 존재하지 않고, 또 생겨날 일도 없기 때문에 계속 기다리다가 타임아웃 이후에 None 을 리턴할것입니다
    clear(driver)

    # 타임아웃을 1초로해서 실행해보겠습니다
    selected = selector('a',driver, timeout=1)

    # None이 확인될것입니다
    print(selected)

# 모든 작업 완료 후 크롬브라우저를 끕니다
driver.quit()

```
