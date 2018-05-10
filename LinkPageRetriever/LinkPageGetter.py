from selenium import webdriver
import selenium.webdriver.common.keys as keys
from bs4 import BeautifulSoup
import time

GECKO_DRIVER_PATH: str = 'H:\Drivers\GeckoDriver\geckodriver-v0.20.0-win64\geckodriver.exe'

class linkGetter():
    def __init__(self, Link_Page_Path):
        self.Driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
        self.Driver.get(Link_Page_Path)
        self.Driver.switch_to.default_content()

    def showComponents(self):
        self.Soup = BeautifulSoup(self.Driver.page_source)
        self.Soup = self.Soup.prettify()
        print(self.Soup)

    def indexFinding(self):
        """
        REF)
        self.upperIndexContainer.append(self.Driver.find_element_by_xpath("/html/body/div/div[1]/header/nav/ul/li[1]/ul/li[1]/a"))
        self.upperIndexContainer.append(self.Driver.find_element_by_xpath("/html/body/div/div[1]/header/nav/ul/li[1]/ul/li[2]/a"))
        self.upperIndexContainer.append(self.Driver.find_element_by_xpath("/html/body/div/div[1]/header/nav/ul/li[2]/ul/li[1]/a"))
        """

        self.upperIndexContainer = []
        searchStringFront: str = "/html/body/div/div[1]/header/nav/ul/li["
        searchStringMiddle: str = "]/ul/li["
        searchStringBack: str = "]/a"
        for upperIdx in range(1,10): # Front Iteration
            for lowerIdx in range(1,10): # Back Iteration
                try:
                    print(searchStringFront + str(upperIdx) + searchStringMiddle + str(lowerIdx) + searchStringBack)
                    elementToAppend = self.Driver.find_element_by_xpath(searchStringFront + str(upperIdx) + searchStringMiddle + str(lowerIdx) + searchStringBack)
                    elementName = elementToAppend.get_attribute()
                    print(elementName)
                    # self.clickanddownload(elementToAppend, elementName)

                    self.upperIndexContainer.append(elementToAppend)
                except:
                    print("End lower index")
                    break

    def clickanddownload(self, elementToDownload, elementName):
        elementToDownload.click()
        time.sleep(0.1)
        self.Driver.switch_to.window(self.Driver.current_window_handle)
        Soup = BeautifulSoup(self.Driver.page_source)
        pSoup = Soup.prettify()
        with open("./" + elementName + ".txt", encoding='utf-8') as file:
            file.write(pSoup)










getter = linkGetter("http://kicm.or.kr/")
getter.indexFinding()