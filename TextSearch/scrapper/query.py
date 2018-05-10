import requests
from bs4 import BeautifulSoup
import bs4


class Query:
    Soup = bs4.BeautifulSoup
    Lang = None
    HTMLComponent = []
    Tags = []


    def __init__(self, wordtoquery, lang):
        self.wordtoquery = wordtoquery
        self.Lang = lang
        print('Query class created')
        print('Querying ', wordtoquery, " from Google")
        self.initial_connectweb()
        self.DetectHtmlComponents()

    def initial_connectweb(self):
        try:
            self.tmp = 'https://google.com/' + 'search?hl=' + self.Lang + '&' + 'dcr=0&ei=jN2sWv7wIsS50gTP_rKYDg&q=Search&q=' + self.wordtoquery
            print("Querying by ::::: ", self.tmp)
            self.Connection = requests.get(self.tmp)
            self.text = self.Connection.text
            self.Soup = BeautifulSoup(self.text, 'html5lib')
        except:
            print('An error occurred while connecting to google')

    def DetectHtmlComponents(self):
        for tag in self.Soup.find_all(True):
            if self.Tags.__contains__(tag.name) is not True:
                self.Tags.append(tag.name)
                print(tag.name)

    def printbytags(self):
        for tag in self.Tags:
            print("=============================================================================================================== ", tag
                  ," ===============================================================================================================")
            print(self.Soup.find(tag))

    def findtagelement(self, tag):
        if tag not in self.Tags:
            print("Your tag :: ", tag, " is not in the document")
        else:
            printdoc = self.Soup.tag
            print(printdoc)
