# Main/Utilities/driver_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Main.Utilities.ConfigurationManager import ConfigurationManager


class DriverManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            browser = ConfigurationManager.get_config_value('browser')
            if browser.lower() == 'chrome':
                options = webdriver.ChromeOptions()
                options.add_argument("--start-maximized")
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                cls._driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            elif browser.lower() == 'firefox':
                options = webdriver.FirefoxOptions()
                # Note: Firefox doesn't support --start-maximized directly
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
                options.set_preference("dom.webnotifications.enabled", False)
                options.set_preference("dom.webdriver.enabled", False)
                cls._driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            elif browser.lower() == 'edge':
                options = webdriver.EdgeOptions()
                options.add_argument("--start-maximized")
                options.add_experimental_option("excludeSwitches", ["enable-automation"])
                cls._driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),
                                             options=options)
            else:
                raise ValueError(f"Browser '{browser}' is not supported.")
            cls._driver.implicitly_wait(10)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
