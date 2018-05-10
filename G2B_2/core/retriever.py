import selenium as selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os

GECKO_DRIVER_PATH: str = 'H:\Drivers\GeckoDriver\geckodriver-v0.20.0-win64\geckodriver.exe'
RAIL_BASE_URL: str = 'http://ebid.kr.or.kr/krn/krnAwardList.do'

Driver = webdriver.Firefox(executable_path=GECKO_DRIVER_PATH)
Frame = None
AbsoluteParentHandle = None
Global_Step = 0

def connect():
    Driver.get(RAIL_BASE_URL)
    Driver.switch_to.default_content()
    time.sleep(0.1)



def maneuver():
    # Enter Search Timeframe
    dateStart = Driver.find_element_by_xpath('//*[@id="fromDate"]')

    # Switching Search to '공사'
    contructionContractSelection = Driver.find_element_by_xpath('/html/body/section/article[1]/form/ul/li[1]/select/option[2]')
    contructionContractSelection.click()

    time.sleep(0.1)
    dateStart.click()
    backButton = Driver.find_element_by_xpath('/html/body/div/div/a[1]/span')
    for clickTimes in range(219): # 219
        backButton.click()
        backButton = Driver.find_element_by_xpath('/html/body/div/div/a[1]/span')

    dayButton = Driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]')
    dayButton.click()
    time.sleep(0.1)

    # Press Search Button
    searchButton = Driver.find_element_by_xpath('/html/body/section/article[1]/div/button')
    searchButton.click()
    time.sleep(5)


"""
Method only for a higher_level method "outerIteration"
************* ONLY FOR USE IN outerIteration FUNCTION *************
"""
def getInsideItem(): # LEVEL 2
        time.sleep(0.1)

        parentHandle = Driver.current_window_handle # LEVEL 1 Parent Handle
        Driver.switch_to.window(Driver.window_handles.pop())

        """
        Going Deeper
        """
        # /html/body/section/form[2]/div[1]/button  ==> Xpath when there is only one button
        # /html/body/section/form[2]/div[1]/button[2] == Xpath when there are two buttons

        # Find by class aproach
        level3ButtonContainer: [] = Driver.find_elements_by_class_name('btn_t2')

        # There could be two elements. So I have to devise some mechanism to determine.
        WebDriverWait(Driver, 120).until(EC.visibility_of_element_located((
            By.XPATH, '/html/body/section/form[2]/div[1]')))
        print(level3ButtonContainer)

        # This randomly throws : list index out of range. I have no idea why.
        try:
            if len(level3ButtonContainer) is 2:
                level3Button = level3ButtonContainer[1]
            else:
                level3Button = level3ButtonContainer[0]

            level3Button.click()

            getFinalItem()
        except:
            getInsideItem()

        """
        OUT
        """
        Driver.switch_to.window(parentHandle)


def getFinalItem():
    time.sleep(0.1)

    parentHandle = Driver.current_window_handle # Parent handle
    Driver.switch_to.window(Driver.window_handles.pop())

    """
    Going Deeper
    """
    time.sleep(3) # Takes some time to load a final element

    # Wait for the item to show up
    # /html/body/section/form/article[1]/div/div/table/tbody/tr[2]/td
    contractName = WebDriverWait(Driver, 60).until(EC.visibility_of_element_located((
        By.XPATH, '/html/body/section/form/article[1]/div/div/table/tbody/tr[2]/td')))

    soup: BeautifulSoup = Driver.page_source

    if os.path.exists('./Data/') is not True:
        os.mkdir('./Data/')

    # If contract name contains "/" delete it. Program will mistake it for a directory separator
    contractNameTmp: str = contractName.text
    contractName = contractNameTmp.replace("/", "")

    with open(file='./Data/' + contractName + '.txt', mode='w+', encoding='cp949') as fileToWrite:
        fileToWrite.write(soup)

    time.sleep(1)


    """
    OUT
    """
    Driver.close()
    Driver.switch_to.window(parentHandle)


def outerIteration(): # LEVEL 1
    global Global_Step
    xpathOuterItemFront = '/html/body/section/article[2]/div[1]/div[2]/table/tbody/tr['
    xpathOuterItemBack = ']/td[4]'
    for outerIdx in range(1,10):
        print("Currently iterating ... ", Global_Step)
        Global_Step = Global_Step + 1

        outerItemButton = Driver.find_element_by_xpath(xpathOuterItemFront + str(outerIdx) + xpathOuterItemBack)
        outerItemButton.click()

        # 1st approach : call a function "getInsideItem" and switch Driver to that popup instance to work in it.
        getInsideItem()


def MetaIteration(): # Biggest Iteration Level 0
    # 3 <= x <= 11  AND THEN press 12 to go to next page iterate this.
    xpathmetaItemFront = '/html/body/section/article[2]/div[2]/p/a['
    xpathmetaItemBack = ']'

    pageSelectorCounter = 3
    for metaidx in range(200): # Won't be bigger than 200. Just for the defition purpose
        print("================================== PAGE SELECTION ", pageSelectorCounter, " ======================================")
        outerIteration()

        if pageSelectorCounter is 13:
            print(" *********************** Page reset to 3 *********************** ")
            pageSelectorCounter = 3

        #Find Next Batch Page Button
        nextBatchPageButton = Driver.find_element_by_xpath(xpathmetaItemFront + str(pageSelectorCounter) + xpathmetaItemBack)
        nextBatchPageButton.click()
        pageSelectorCounter += 1



connect()
maneuver()
# outerIteration() <== This function is now called under "MetaIteration"
MetaIteration()