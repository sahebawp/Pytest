import time
from selenium import webdriver


class SeleniumHandler():
    '''
        Clas to invoke Browser and handle
        all the webdriver/selenium related logic

    '''

    def ope_browser_and_validate(self, url):
        '''
        function to open browser and fetch the given url
        checks for the current url as given url
        :param url:
        :return: None
        '''

        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        time.sleep(10)
        assert driver.current_url == url
