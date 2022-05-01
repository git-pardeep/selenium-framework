import time
import pytest
from pages.test_Launchpage import Launchpage

@pytest.mark.usefixtures("setup")
class Testframework():
    def test_framework(self):
        lp=Launchpage(self.driver,self.wait)
        lp.departloc("New Delhi")
        lp.goingto("Ban")
        lp.searchResults("Bangalore (BLR)")
        lp.selectdate("09/08/2022")
        lp.clicksearch()
        lp.scroldriver()

        sf=searchflight(self.driver)
        sp.resultflight()
        all_stop=self.wait.until(EC.presence_of_all_elements_located((By.XPATH,"//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
        for stop in all_stop:
            print("the Text",+stop.text)
            assert stop.text =='1 Stop'
            print("assert Pass")


