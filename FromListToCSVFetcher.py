'''
Class realize conversion from list to csv, and csv to list
'''
from getData import *
import os

Data = GetData()
Data.GetProductListFromSite()


class FromListToCSVFetcher:
    reverseList = []
    strip_file = []

    def fetcher(self):
        if len(Data.productsList) == 0:
            print("Class FromListToCSVFetcher\n"
                  "method fetcher took empty list")
            return

        if os.stat("etalonProductsListFile.csv").st_size != 0:
            os.remove("etalonProductsListFile.csv")
        else:
            pass


        with open('etalonProductsListFile.csv', 'a', newline="\n")  as file:
            for i in Data.productsList:
                file.write(f'{i}\n')

    def reverseFetcher(self):
        with open('etalonProductsListFile.csv', 'r') as etalonFile:
            fileContent = (etalonFile.readlines())
            strip_file = [item.strip() for item in fileContent]
            return strip_file


