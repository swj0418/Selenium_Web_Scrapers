from bs4 import BeautifulSoup
from threading import Thread
import requests
from requests import Request
import time
import sys
import os

NAVERIN = 'https://kin.naver.com/'
QNA = 'qna/'
LISTING = 'list.nhn?'
DIR = 'dirId='
# NAVERIN + QNA + LISTING + DIR + DIRIDs
ENGINES = []

class Query_Engine(Thread):
    Req = requests.api
    Completion = False
    def __init__(self, url):
        Thread.__init__(self)
        self.url = url

    def run(self):

        print("Thread for ", self.url, " has been started")
        self.IterQuery = '&queryTime=2018-03-27%2010%3A17%3A04&page='
        for idx in range(1, 100):
            time.sleep(5)
            print(self.url + self.IterQuery + str(idx))
            url_F = self.url + self.IterQuery + str(idx)

            request_F = requests.get(url_F)
            if request_F.status_code is not 200:
                print(request_F.status_code)
                break

            soup = BeautifulSoup(request_F.text, 'html5lib')
            qtext = []
            qtext = soup.find_all("td", {"class": "title"})
            if qtext.__len__() == 0:
                break

            qtcount = 0
            for qt in qtext:
                text = qt.text.strip()
                if "내공" in text:
                    text = text.replace("내공", "")
                    text = text[5 :]
                    text = text.strip()

                print(qtcount, " : ", text)
                qtcount += 1

                try:
                    with open("./Questions.csv", 'a', encoding='EUC-KR') as file:
                        file.write(text + "\n")

                    with open("./Questions.txt", mode='a', encoding='EUC-KR') as file:
                        file.write(text + "\n")
                except:
                    try:
                        with open("./Questions.csv", 'a', encoding='UTF-8') as file:
                            file.write(text + "\n")

                        with open("./Questions.txt", mode='a', encoding='UTF-8') as file:
                            file.write(text + "\n")
                    except:
                        pass


        Completion = True
        print("Thread ", self.ident, " Complete ", Completion)
        ENGINES.remove(self)


class Querier:
    DirID_L1 = ['11', '1', '2', '3', '8', '7', '6', '4', '9']  # In order 교육학문, 컴퓨터통신, 게임, 엔터테인먼트, 생활, 건강, 사회정치, 경제, 여행
                                                               # After that, starting from 01 (2nd Layer), it goes deep until the 3rd layer which also is numbered the same way ex) 01, 02
    # DirID_L1 = ['1']

    def __init__(self):
        print("Initializing a Querier")
        self.startEngineThread()

    def startEngineThread(self):
        url = NAVERIN + QNA + LISTING + DIR

        for l1 in self.DirID_L1:
            print("L1=============================================")
            print(l1)

            for l2 in range(1, 10):
                print("L2=======================")
                if l2 < 10:
                    dirID_l1l2 = url + str(l1) + '0' + str(l2)
                    # print(url + str(l1) + '0' + str(l2))
                    self.l3_manuever(dirID_l1l2)
                else:
                    dirID_l1l2 = url + str(l1) + str(l2)
                    # print(url + str(l1) + str(l2))
                    self.l3_manuever(dirID_l1l2)

    def l3_manuever(self, l1l2):
        for l3 in range (1, 10):
            print("L3=======")
            if l3 < 10 and ENGINES.__len__() <= 50:
                dirID_F = l1l2 + '0' + str(l3)
                # HTML Parsing
                engine = Query_Engine(dirID_F)
                ENGINES.append(engine)
                engine.start()


            elif l3 >= 10 and ENGINES.__len__() <= 50:
                dirID_F = l1l2 + str(l3)
                # HTML Parsing
                engine = Query_Engine(dirID_F)
                ENGINES.append(engine)
                engine.start()

            else:
                try:
                    time.sleep(1)
                    print('\033[93m' + 'MAXIMUM THREAD REACHED' + '\033[0m')
                    print('\033[93m' + 'Threads Alive Below')
                    for T in ENGINES:
                        print(T)
                        if T.Completion is True:
                            T.join()
                            ENGINES.remove(T)
                        else:
                            print(T.Completion)
                            continue
                except:
                    continue


class ThreadChecker(Thread):
    def __init(self):
        Thread.__init__(self)

    def run(self):

        while True:
            time.sleep(5)
            print( '\033[91m', "Threads Alive >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ", ENGINES.__len__(), '\033[0m')


tc = ThreadChecker()
tc.start()

querier = Querier()

