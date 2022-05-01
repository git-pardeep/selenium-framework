import time


class BaseDriver:
    def __init__(self,driver):
        self.driver=driver
    def scroldriver(self):
        pagelength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeight;return document.body.scrollHeight")
        match = False
        while match == False:
            lastcount = pagelength
            time.sleep(4)
            pagelength = self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);var pagelength=document.body.scrollHeigth;return document.body.scrollHeight")
            if lastcount == pagelength:
                match = True
        time.sleep(4)
