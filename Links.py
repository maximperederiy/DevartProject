'''
Class realize link addition
'''
class Links():
    def __init__(self,link):
        self.link = link
    def complitePage(self):
        link = "https://www.devart.com/"+self.link
        return link