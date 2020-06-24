import getData

'''
  Class realize conversion from page's data to list with products names
  '''


class ProductList(getData.GetData):

    def parser(elementsName):
        productsList = [i.text for i in elementsName]
        return productsList
