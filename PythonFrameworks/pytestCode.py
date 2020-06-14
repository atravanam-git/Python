#==========================================================================# import selenium binding libraries
# import keys class from webdriver common functions
# create a chrome / browser instance
# Next, use the .get() method of the driver to load a website.
#==========================================================================import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestWebPage:
    @pytest.fixture()
    def setUP(self):
        global driver
        driver = webdriver.Chrome(
            executable_path="C:/eclipse-workdirectory/Python/CorePythonProject/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://www.python.org")
        yield
        driver.close()
        driver.quit()
        print("Test run completed successfully")

    def test_pgTitle(self, setUP):
        title = driver.title
        assert title == "Welcome to Python.org"

    def test_pgSearch(self, setUP):
        elem = driver.find_element_by_name('q')
        elem.clear()
        elem.send_keys("Pycon")
        elem.send_keys(Keys.RETURN)
        txtLabel = driver.find_element_by_class_name("list-recent-events menu")
        assert txtLabel == "list-recent-events menu"