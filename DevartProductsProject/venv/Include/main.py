import csv

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from FromListToCSVFetcher import *
from Links import *
from productsList import *


class TestSuite:
    '''
    Steps to reproduce:
    1)Go to page
    2)Take all name's product's on this page
    3)Write names to CSV file
    4)Compare len's CSV with element's count
    '''
    link = Links("dbforge/mysql/")
    prodPars = productList
    fetcher = FromListToCSVFetcher()

    def TestCase(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(self.link.complitePage())
        driver.implicitly_wait(5)
        elementsName = driver.find_elements_by_class_name("quietLink")

        self.prodPars.parser(elementsName)
        self.fetcher.fetcher(self.prodPars.parser(elementsName))
        assert 8 == len(self.prodPars.parser(elementsName))
        self.fetcher.reverseFetcher()
        driver.quit()

    def Compare(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.get(self.link.complitePage())
        driver.implicitly_wait(5)
        elementsName = driver.find_elements_by_class_name("quietLink")
        self.prodPars.parser(elementsName)

        etalonProductList = self.fetcher.reverseFetcher()
        actualProductList = self.prodPars.parser(elementsName)

        if etalonProductList == actualProductList:
            print("Two lists are equal")
        else:
            print([[x for x in etalonProductList if x not in actualProductList], [x for x in actualProductList if x not in etalonProductList]])





test = TestSuite()
test.TestCase()
test.Compare()
