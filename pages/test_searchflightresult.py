from selenium.webdriver.common.by import By

from base.basedriver import BaseDriver


class searchflight(BaseDriver):
    def __init__(self,driver,wait):
        super().__init__(driver)
        self.driver=driver
        self.wait=wait
    def resultflight(self):
        self.driver.find_element(By.XPATH,"//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(4)
