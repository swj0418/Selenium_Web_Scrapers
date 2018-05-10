import tests.context

from NaverQ.core import Selenium_Connection
from selenium.webdriver.common.keys import Keys

class TestUnit_1:
    def __init__(self, url):
        self.url = url;
        selConn = Selenium_Connection(url)
        selConn.run()
        self.driver = selConn.get_driver()


TU1 = TestUnit_1(url = "https://kin.naver.com/index.nhn")


# id : au_board_list