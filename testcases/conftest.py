import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield #tear down method
    driver.close()
# import pytest
#
#
# @pytest.fixture()
# def setup():
#     print("hi")
#     yield
#     print("end")