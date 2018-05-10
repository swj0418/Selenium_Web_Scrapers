from bs4 import BeautifulSoup
import requests
from scrapper import helpers
from scrapper import query
from scrapper.query import Query
from scrapper import requestm


def requestSearch(address, keyword):
    url = address + '/search?dcr=0&ei=y2irWtqeAov38gXiw5yIDg&q=' + keyword

    return requests.get(url).text

def readWeb(address):
    url = address
    request = requests.get(url)
    print(request)
    print(request.headers)
    print(request.encoding)

    return request.text

def refine(text):
    soup = BeautifulSoup(text, "lxml")

    return soup.prettify()

def getSoup(text):
    return BeautifulSoup(text, "html5lib")

def printMetaInfo(soup):
    print("Title : ", soup.title.string)
    print("p : ", soup.p.string)
    print("a : ", soup.a.string)

def printTags(soup):
    list = []
    for tag in soup.find_all(True):
        list.append(tag.name)

    refinedList = helpers.RemoveDuplicateFromList(list)
    print("Tags in the html page : ", refinedList)

def sortNullTags(soup):
    ret = []
    tmp = []
    for tag in soup.find_all(True):
        tmp.append(tag.name)

    refinedList = helpers.RemoveDuplicateFromList(tmp)
    ValidList = []
    for tag in refinedList:
        print(soup.find(tag).name)

    ret = ValidList
    print("================= Sorted List ===================")
    for item in ret:
        print(item)
    return ret

def printComponent(soup, comp):
    NoneCount = 0
    for tag in soup.find_all(comp):
        if tag.string is not None:
            print(tag.string)
        else:
            NoneCount += 1;

    print("None Count : ", NoneCount)


#Q = Query('Machine Learning', 'kr')
#Q.findtagelement('a')
