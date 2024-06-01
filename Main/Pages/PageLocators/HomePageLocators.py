from selenium.webdriver.common.by import By


class HomePageLocators:
    SearchBar = (By.NAME, "search")
    Title = (By.XPATH, "//span[text()=\"Gang of Four\"]")
    Pic = (By.XPATH, "//img[@src=\"//upload.wikimedia.org/wikipedia/commons/thumb/9/9b/Gang_of_Four_in_Chicago.jpg"
                     "/220px-Gang_of_Four_in_Chicago.jpg\"]")
