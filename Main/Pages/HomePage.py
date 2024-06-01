import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Main.Pages.BasePage import BasePage
from Main.Pages.PageLocators.HomePageLocators import HomePageLocators
from Main.Utilities.ConfigurationManager import ConfigurationManager


class HomePage(BasePage):
    def __init__(self):
        super().__init__()

    def wikipedia(self):
        self._open(ConfigurationManager.get_config_value("baseUrl"))

    def search(self, word):
        self._find_element(HomePageLocators.SearchBar).send_keys(word)
        time.sleep(3)
        self._find_element(HomePageLocators.SearchBar).send_keys(Keys.RETURN)

    def take_title(self):
        return self._get_text(HomePageLocators.Title)

    def is_right_pic_displayed(self):
        element = self.driver.find_element(By.XPATH,
                                           "//img[@src=\"//upload.wikimedia.org/wikipedia/commons/thumb/9/9b"
                                           "/Gang_of_Four_in_Chicago.jpg"
                                           "/220px-Gang_of_Four_in_Chicago.jpg\"]")

        path = "C:\\Users\\BESIM\\PycharmProjects\\SamplePythonUI\\Main\\GraphicalData\\GOF.jpg"
        return self._compare_images(path, element)
