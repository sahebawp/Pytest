
from search_bar_functionality_pytest.selenium_helper import  SeleniumHandler


def test_search_bar():
    handler = SeleniumHandler()
    url = 'https://www.google.com/'
    handler.ope_browser_and_validate(url)

