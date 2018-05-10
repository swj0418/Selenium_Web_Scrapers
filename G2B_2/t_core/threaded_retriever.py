from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os
from threading import Thread

GECKO_DRIVER_PATH: str = 'H:\Drivers\GeckoDriver\geckodriver-v0.20.0-win64\geckodriver.exe'
RAIL_BASE_URL: str = 'http://ebid.kr.or.kr/krn/krnAwardList.do'

GECKO_DRIVERS = []

Frame = None
AbsoluteParentHandle = None
Global_Step = 0

Driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)


def connect():
    Driver.get(RAIL_BASE_URL)
    Driver.switch_to.default_content()


def setSearchOptions(timeToStart: int):
    # Enter Search Timeframe
    dateStart = Driver.find_element_by_xpath('//*[@id="fromDate"]')

    # Switching Search to '공사'
    contructionContractSelection = Driver.find_element_by_xpath('/html/body/section/article[1]/form/ul/li[1]/select/option[2]')
    contructionContractSelection.click()

    time.sleep(0.1)
    dateStart.click()
    backButton = Driver.find_element_by_xpath('/html/body/div/div/a[1]/span')
    for clickTimes in range(timeToStart): # 219
        backButton.click()
        backButton = Driver.find_element_by_xpath('/html/body/div/div/a[1]/span')

    dayButton = Driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]')
    dayButton.click()
    time.sleep(0.1)

    # Press Search Button
    searchButton = Driver.find_element_by_xpath('/html/body/section/article[1]/div/button')
    searchButton.click()
    time.sleep(5)

    WebDriverWait(Driver, 120).until(EC.visibility_of_element_located((
        By.XPATH, '/html/body/section/form[2]/div[1]')))


    def threadInitialization():
        xpathmetaItemFront = '/html/body/section/article[2]/div[2]/p/a['
        xpathmetaItemBack = ']'

        pageSelectorCounter = 3
        for metaidx in range(200):  # Won't be bigger than 200. Just for the defition purpose
            print("================================== PAGE SELECTION ", pageSelectorCounter,
                  " ======================================")

            outerIteration()

            if pageSelectorCounter is 13:
                print(" *********************** Page reset to 3 *********************** ")
                pageSelectorCounter = 3

            # Find Next Batch Page Button
            nextBatchPageButton = Driver.find_element_by_xpath(
                xpathmetaItemFront + str(pageSelectorCounter) + xpathmetaItemBack)
            nextBatchPageButton.click()
            pageSelectorCounter += 1


connect()
setSearchOptions(10)
