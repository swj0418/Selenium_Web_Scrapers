import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os
import sys

DATA_PATH = 'F:/2018_Spring/Programming/Python/G2B_2/core/Data/'
OUTPUT_FILE_PATH = 'F:/2018_Spring/Programming/Python/G2B_2/core/Organized.csv'
FILE_CONTAINER = []

def getFiles():
    FILE_CONTAINER = os.listdir(DATA_PATH)

    COUNTER = 0
    for fileName in FILE_CONTAINER:
        FILE_PATH = DATA_PATH + fileName
        print("Progress... ", COUNTER)
        COUNTER += 1
        with open(FILE_PATH, encoding='cp949') as file:
            findContractName(file)


def findContractName(file):
    Soup: BeautifulSoup = BeautifulSoup(file, "lxml")
    tables = Soup.find_all('table')

    contractInfo = extractContractInformation(tables[0])

    # for tables, skip tables[0] for Bidder Information
    tables = tables[1:]

    # Call this once to write header items
    # extractHeader(Soup)

    bidder_count = 0
    for table in tables:
        extractBidderInformation(table, contractInfo)

        bidder_count += 1

        """
        if bidder_count is 2:
            break
        """

""" Run this once """
def extractHeader(Soup: BeautifulSoup):
    headers = Soup.thead.find_all('th')

    with open(OUTPUT_FILE_PATH, mode='w+', encoding='utf-8') as outputFile:
        for item in headers:
            outputFile.write(item.string)
            outputFile.write(',')

        outputFile.write("\n")


# Pass on table[0] make it a string and continuously apppend this string when performing operation extractBidderInfo
def extractContractInformation(table):
    contractInfoContainer = table.find_all('td')
    for idx in range(len(contractInfoContainer)):
        contractInfoContainer[idx] = str(contractInfoContainer[idx]).replace("<td>", "").replace("</td>", "").strip()

    neededInformation = []
    neededInformation.append(contractInfoContainer[0])  # 입찰공고번호
    neededInformation.append(contractInfoContainer[2].replace('<td colspan="3">', ''))  # 입찰공고명
    neededInformation.append(contractInfoContainer[3])  # 설계금액
    neededInformation.append(contractInfoContainer[4])  # 추정가격(예정가격)
    neededInformation.append(contractInfoContainer[7])  # 심사기준

    """
    returnString: str = ""
    for idx in range(len(neededInformation)):
        returnString += neededInformation[idx] + ','
    """

    return neededInformation


def extractBidderInformation(table, contractInfo):
    table_td = table.find_all('td')
    with open(OUTPUT_FILE_PATH, mode='a+', encoding='EUC-KR') as outputFile:
        for idx in range(len(table_td)):

            # First line (Second as whole) contains '낙찰'
            # It should be treated differently starting from the second bidder
            if idx <= 7:
                if idx is 0:
                    for i in range(len(contractInfo)):
                        outputFile.write(str(contractInfo[i]).replace(",", ""))
                        outputFile.write(',')
                # print(str(table_td[idx]).replace("<td>", "").replace("</td>", "").replace(",", "").replace(' ',
                #                                                                                           '').strip())
                # print("====================================================================================")
                outputFile.write(
                    str(table_td[idx]).replace("<td>", "").replace("</td>", "").replace(",", "").replace(' ',
                                                                                                         '').strip())
                outputFile.write(',')


                if idx % 7 is 0 and idx is not 0:
                    outputFile.write('\n')
            else:
                if idx % 8 is 0:
                    for i in range(len(contractInfo)):
                        outputFile.write(str(contractInfo[i]).replace(",", ""))
                        outputFile.write(',')
                # print(str(table_td[idx]).replace("<td>", "").replace("</td>", "").replace(",", "").replace(' ',
                #                                                                                         '').strip())
                # print("====================================================================================")
                outputFile.write(
                    str(table_td[idx]).replace("<td>", "").replace("</td>", "").replace(",", "").replace(' ', '').strip())
                outputFile.write(',')

                if idx % 8 is 7:
                    outputFile.write('\n')



getFiles()





"""
tbody : contains general information about the contract
table : bidder information in a table
thead : Column label in thead
"""