from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import selenium
import selenium.common.exceptions as se_excpetion
from threading import Thread
import time
import os
import sys
import fileinput

class requestmanager(Thread):
    def __init__(self, baseurl, startdate, enddate, keyword):
        Thread.__init__(self)
        self.baseurl = baseurl
        self.startdate = startdate
        self.enddate = enddate
        self.keyword = keyword

    def run(self):
        self.connecting()
        self.navigate()
        self.parse_and_download(0)
        self.parse_and_download(10)
        self.parse_and_download(20)
        self.parse_and_download(30)
        self.parse_and_download(40)
        self.parse_and_download(50)
        self.parse_and_download(60)
        self.parse_and_download(70)
        self.parse_and_download(80)
        self.parse_and_download(90)
        self.parse_and_download(100)
        self.parse_and_download(110)
        self.parse_and_download(120)
        self.parse_and_download(130)
        self.parse_and_download(140)
        self.parse_and_download(150)

    def connecting(self):
        #self.browser = webdriver.Firefox(executable_path='E:\Libraries\Python\geckodriver-v0.20.0-win64\geckodriver.exe')
        self.browser = webdriver.Firefox(executable_path='E:\Libraries\Python\geckodriver-v0.20.0-win64\geckodriver.exe')
        self.browser.implicitly_wait(3)
        self.browser.get(self.baseurl)
        self.browser.set_window_size(1920, 3000) # Setting a browser size long solved the identifying issue

    def navigate(self):
        """
        Until getting into 토지정책
        :return:
        """
        self.browser.switch_to.default_content()
        print("First browser : ", self.browser.title, " ||||| WindowHandle : ", self.browser.current_window_handle)

        self.browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.SUBTRACT)
        self.browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.SUBTRACT)
        self.browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.SUBTRACT)
        self.browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.SUBTRACT)
        self.browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.SUBTRACT)

        iframes = self.browser.find_elements_by_tag_name('iframe')
        for f in iframes:
            print(f.get_attribute('title'))

        frame1 = self.browser.find_element_by_id("iframeEpeople")
        self.browser.switch_to.frame(frame1)

        button = self.browser.find_elements_by_tag_name("a")
        print("Button number 19 : ", button[19].tag_name)
        button[19].send_keys(Keys.ENTER)

        """
        From 토지정책 to setting up the search options
        """

        self.browser.implicitly_wait(10)
        time.sleep(1)

        iframes = self.browser.find_elements_by_tag_name('iframe')

        """
        I don't know how the hell did I get here. But it worked.
        Now setting up search options
        """
        inputcomponents = self.browser.find_elements_by_tag_name('input')

        for input_c in inputcomponents:
            if input_c.get_attribute('title') == "시작일":
                print('Start date found!')
                print(input_c.get_property('value'))
                input_c.clear()
                input_c.send_keys(self.startdate) # Indents in dates are very important for the web to understand

            if input_c.get_attribute('title') == "종료일":
                print('End date found!')
                print(input_c.get_property('value'))
                input_c.clear()
                input_c.send_keys(self.enddate)

            if input_c.get_attribute('title') == "검색어":
                print('Search text area found!')
                input_c.send_keys(self.keyword)

            if input_c.get_attribute('title') == "검색":
                print("Searching !")
                input_c.send_keys(Keys.ENTER)

        time.sleep(5) # Waiting minimum 0.8 second required for the webdriver to identify newly updated page

    def parse_and_download(self, count):

        """
        5 to 14 : pages to go into
        15 to ~ : next frames
        """

        tmpload = self.browser.find_elements_by_tag_name("a")

        time.sleep(0.1)
        self.count = count

        # Checking for pages in the given time frame
        # Only the first time
        if count is 0:
            self.whole_pages_length = (int(
                self.browser.find_element_by_xpath('//*[@id="content"]/div[3]/table/tbody/tr[1]/td[1]').text) // 10) + 1
            self.total_info_sessions = int(self.browser.find_element_by_xpath('//*[@id="content"]/div[3]/table/tbody/tr[1]/td[1]').text)
            print("Total Pages in the time frame [", self.startdate, " --- ", self.enddate, "] : ", self.whole_pages_length)

        # Ten info sessions
        for idx in range(5,15):

            # Giving time to load fully a new info session
            time.sleep(0.1)

            # Terminating condition
            if(self.total_info_sessions is self.count):
                print("Job done... Terminating")
                self.browser.close()

            print("From thread : ", self.name, "     Information Session retrieved : ", self.count, " / ", self.total_info_sessions, "           Index : ", idx)
            self.count += 1

            try:
                toload = self.browser.find_elements_by_tag_name("a")
            except(se_excpetion.SessionNotCreatedException):
                print("Session not created exception occurred")
                pass

            if self.count <= 10:
                try:
                    toload[idx].click()
                except:
                    time.sleep(1)
                    toload[idx].send_keys(Keys.ENTER)
            else:
                try:
                    toload[idx].send_keys(Keys.ENTER)
                except:
                    time.sleep(1)
                    toload[idx].send_keys(Keys.ENTER)

            time.sleep(1)
            page_source = self.browser.page_source

            dirp = "./" + self.keyword + "_" + str(self.startdate)
            if not os.path.exists(dirp):
                os.makedirs(dirp)

            filename = dirp + "/Data_" + str(self.count) + ".txt"

            with open(filename, "w+") as file:
                try:
                    file.write(page_source)
                except:
                    print("Exception occurred while writing onto a file")
                    pass

            # Now going back to upper frame by clicking "목록"
            go_back_to_list = self.browser.find_element_by_xpath('//*[@id="content"]/p/a')
            try:
                go_back_to_list.send_keys(Keys.ENTER)
            except:
                go_back_to_list.click()

            time.sleep(1)

            # Going to the next page
            if idx is 14:
                click_to_go_next= self.browser.find_element_by_class_name('btn.next')
                click_to_go_next.send_keys(Keys.ENTER)
                time.sleep(0.1)





