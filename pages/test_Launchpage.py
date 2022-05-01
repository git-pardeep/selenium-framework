import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from base.basedriver import BaseDriver
# from selenium import webdriver

class Launchpage(BaseDriver):
    def __init__(self,driver,wait):
        # super().__init__(driver,wait)
        self.driver=driver
        self.wait=wait
    def departloc(self,departlocation):
        depart_from=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_city']")))
        depart_from.send_keys(departlocation)
        depart_from.send_keys(Keys.ENTER)
    def goingto(self,goingtolocation):
        goingto=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_arrival_city']")))
        goingto.click()
        goingto.send_keys(goingtolocation)
    def searchResults(self,searchResult):
        searchresult=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div/li")))
        for result in searchresult:
            if searchResult in result.text:
                result.click()
                break
    def selectdate(self,selectdates):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_date']"))).click()
        # searchdate=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class='inActiveTD']"))).find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class='inActiveTD']")
        searchdate=self.driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class='inActiveTD']")
        print(len(searchdate))
        for date in searchdate:
            if date.get_attribute("data-date") == selectdates:
                date.click()
                time.sleep(4)
                break
    def clicksearch(self):
        searrchflght=self.driver.find_element(By.XPATH,"//input[@id='BE_flight_flsearch_btn']")
        searrchflght.click()
        time.sleep(4)
