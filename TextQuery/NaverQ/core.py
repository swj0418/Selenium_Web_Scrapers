#######################################################################################################################
#                                                 SETTER FOR CONNECTION                                               #
#######################################################################################################################

import urllib3
from threading import Thread
from selenium import webdriver
from selenium import __version__
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

class Selenium_Connection(Thread):
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        self.establish_connection()

        # Task Specific
        # Task 1 Basic Question
        self.maneuver_question_initial()

    def establish_connection(self):
        self.driver = webdriver.Firefox(executable_path='E:\Libraries\Python\geckodriver-v0.20.0-win64\geckodriver.exe')
        self.driver.get(self.url)
        print("Driver Booting Up. Selenium Version : ", __version__)

        # Set browser size long so that all the content on the browser currently showing can be revealed by selenium driver
        self.driver.set_window_size(1920, 5000)
        self.driver.switch_to.default_content()

        # Wait
        time.sleep(0.5)

    def maneuver_question_initial(self):
        self.driver.find_element_by_xpath('//*[@id="main_content"]/div[2]/div[1]/div/div[2]/div[1]/h5/a').send_keys(
            Keys.ENTER)

        # Initializing qtext list
        self.qtext = []
        self.itercount = 0

        for _ in range(100000):
            time.sleep(0.3)
            self.retrieve_question_texts()


    def retrieve_question_texts(self):
        tagsSel = self.driver.find_elements_by_tag_name('a')

        soup = BeautifulSoup(self.driver.page_source, 'html5lib')
        tags = soup.findAll('a')

        tagscount = 0
        for tag in tagsSel:
            # print(tagscount, " ", tag.text)
            tagscount += 1

            if (tagscount >= 116 and tagscount <= 155):
                self.qtext.append(tag.text)
                with open('./Questions.txt', 'a+') as f:
                    f.write(tag.text + "\n")

        if self.itercount % 10 is not 0 and self.itercount // 10 is 0:
            xp = '//*[@id="list_noanswer"]/div/div[4]/a[' + (str)((self.itercount % 10) + 2) + ']'
            self.driver.find_element_by_xpath(xp).send_keys(Keys.ENTER)

        elif self.itercount is not 0 and self.itercount % 10 is 0 and self.itercount // 10 is 0:
            self.driver.find_element('//*[@id="list_noanswer"]/div/div[4]/a[11]').send_keys(Keys.ENTER)

        elif self.itercount % 10 is not 0 and self.itercount // 10 is not 0:
            xp = '//*[@id="list_noanswer"]/div/div[4]/a[' + (str)((self.itercount % 10) + 1) + ']'
            self.driver.find_element_by_xpath(xp).send_keys(Keys.ENTER)

        elif self.itercount % 10 is 9 and self.itercount // 10 is not 0:
            self.driver.find_element('//*[@id="list_noanswer"]/div/div[4]/a[12]').send_keys(Keys.ENTER)

        print(self.itercount)

        self.itercount += 1



    def get_driver(self):
        return self.driver