from FromListToCSVFetcher import *
from getData import *
fetcher = FromListToCSVFetcher()
data = GetData()

def RunTest():
    '''
    Steps to reproduce:
    1)Go to page
    2)Take all name's product's on this page
    3)Write names to CSV file
    4)Compare len's CSV with element's count
    '''


    Data = data.GetProductListFromSite()
    etalonProductList = fetcher.reverseFetcher()
    if etalonProductList == Data:
        print("Two lists are equal")
    else:
        print([[x for x in etalonProductList if x not in Data],
               [x for x in Data if x not in etalonProductList]])




RunTest()




