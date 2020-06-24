from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import logging



from Links import *

link = Links("dbforge/mysql/")


logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
class GetData:

    def GetProductListFromSite(self):

        driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install())
        logging.info("Browser Launched")
        driver.get("https://www.devart.com/dbforge/mysql/")
        logging.info("Navigation to www.devart.com/dbforge/mysql/")
        try:
            waitForElement = WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, "/html/body/section[2]/div/div/div[1]/h1/a"),
                                                 text_="dbForge Studio for MySQL")


            )
            logging.info("Waiting for load first product block with name dbForge Studio for MySQL")
            self.elementsName = driver.find_elements_by_class_name("quietLink")
            logging.info("Taking all product's name from page to list")
            self.productsList = [i.text for i in self.elementsName]
            logging.info("Convert product's name from element's names from html type to readable names")
            return self.productsList
        finally:
            driver.quit()
            logging.info("Browser closed")






