import requests
from bs4 import BeautifulSoup
from selenium import __version__
from selenium import webdriver
import time
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

class govconn_1:
    baseurl = 'http://www.g2b.go.kr/'

    def __init__(self):
        print("Connecting to ... ", self.baseurl)

        next_conn = govconn_bid_info(self.baseurl)


class govconn_bid_info:
    baseurl = 'pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do'

    def __init__(self, prev_url):
        print("====== 입찰정보 ======")
        self.request = requests.get(prev_url + self.baseurl)

        soup = BeautifulSoup(self.request.text, 'lxml')

        sel_enter = sel_entering_point(prev_url + self.baseurl)


class sel_entering_point:
    chromedriverPath = 'H:\Drivers\Chrome Driver\chromedriver_win32\chromedriver.exe'
    geckodriverPath = 'H:\Drivers\GeckoDriver\geckodriver-v0.20.0-win64\geckodriver.exe'

    def __init__(self, url):
        print("Booting up Selenium")
        # self.driver = webdriver.Chrome(executable_path=self.chromedriverPath)
        self.driver = webdriver.Firefox(executable_path=self.geckodriverPath)
        self.driver.implicitly_wait(3)
        self.driver.get(url)

        time.sleep(0.5)

        self.driver.switch_to.default_content()

        frame = self.driver.find_element_by_xpath('//*[@id="sub"]')
        self.driver.switch_to.frame(frame)
        time.sleep(0.1)
        frame = self.driver.find_element_by_xpath('/html/frameset/frame[1]')
        self.driver.switch_to.frame(frame)
        time.sleep(0.1)

        service_tab = self.driver.find_element_by_xpath('/html/body/div/ul/li[3]/a')
        service_tab.click()
        bid_result_tab = self.driver.find_element_by_xpath('/html/body/div/ul/li[3]/ul/li[5]/a')
        bid_result_tab.click()
        self.driver.switch_to.default_content()

        frame = self.driver.find_element_by_xpath('//*[@id="sub"]')
        self.driver.switch_to.frame(frame)
        frame = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(frame)

        search_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]/div/a[1]')
        search_button.click()
        self.driver.switch_to.default_content()

        frame = self.driver.find_element_by_xpath('//*[@id="sub"]')
        self.driver.switch_to.frame(frame)
        time.sleep(0.1)
        frame = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(frame)
        time.sleep(0.1)
        """
        Initialize directories
        """
        try:
            os.mkdir('./DetailedData/')
        except:
            pass


        """
        First time data labeling
        """
        with open('overview.csv', 'w+', encoding='EUC-KR') as file:

            for idx in range(1, 11):
                file.write(self.driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/table/thead/tr/th[" + str(idx) + "]").text + ',')

            file.write("\n")

        """
        Main Content
        """

        for i in range(100):
            self.printData()

            """
            Level 1 Data Iteration
            """
            self.data_level_1()

            time.sleep(0.1)
            if i is 0:
                next_btn = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/a')
            elif 1 <= i < 10:
                next_btn = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/a' + '[' + str(i + 2) + ']')
            elif i >= 10:
                next_btn = self.driver.find_element_by_xpath(
                    '/html/body/div/div[2]/div[3]/a' + '[' + str((i % 10) + 3) + ']')

            print(i)
            next_btn.click()



    def printData(self):
        tr_elements = self.driver.find_elements_by_tag_name('tr')
        for ele in tr_elements:
            td_elements = ele.find_elements_by_tag_name('td')

            for eletd in td_elements:
                self.save_overview_data(eletd.text, endl=False)
                print(eletd.text, end="\t")

            self.save_overview_data("-", True)
            print()

    def save_overview_data(self, data, endl):
        with open("overview.csv", 'a', encoding='EUC-KR') as file:
            try:
                if endl is True:
                    file.write("\n")
                elif endl is False:
                    if "," in data:
                        file.write(data + ",")
                    elif data is "-":
                        file.write("-" + ",")
                    else:
                        file.write(data + ",")
            except:
               file.write("NULL" + ",")

    def data_level_1(self):
        starttime = time.ctime()

        for idx in range(1 , 30):
            btn = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/table/tbody/tr[' + str(idx) + ']/td[11]/div/a')
            btn.click()
            time.sleep(0.2)

            # Xpath to reason.
            # //*[@id="container"]/div[2]/dl/dd/ul/li/strong

            try:
                Auction_No = self.driver.find_element_by_xpath('/html/body/div/div[2]/form[1]/div[2]/table/tbody/tr[1]/td[1]/div').text
                print("입찰 공고번호" + Auction_No)
                print("Companies applied : ", self.driver.find_element_by_xpath('//*[@id="upcheForm"]/div/div[2]/span').text)

                """
                Individual Auctioneer Information
                """
                for i in range (1, 100):
                    try:
                        row = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/table/tbody/tr[' + str(i) + ']')
                        elements = row.find_elements_by_tag_name("td")
                        for elem in elements:
                            print(elem.text, end='\t')

                            with open('./DetailedData/' + Auction_No + '.csv', 'a', encoding='cp949') as dfile:
                                dfile.write(elem.text + ',')


                        print()
                        with open('./DetailedData/' + Auction_No + '.csv', 'a', encoding='cp949') as endlf:
                            endlf.write("\n")
                        """
                        Retrieval and saving
                        """
                    except:
                        break



            except:
                print("No Data")
                pass

            time.sleep(0.1)

            for i in range(3, 10):
                try:
                    self.driver.find_element_by_xpath('/html/body/div/div[2]/div[' + str(i) + ']/div/a').click()
                    break
                except:
                    pass
