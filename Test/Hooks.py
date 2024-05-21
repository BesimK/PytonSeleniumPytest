import time

import pytest
from Main.Utilities.DriverManager import DriverManager


@pytest.fixture(scope="class")
def hooks():
    print("\nSetUp")
    driver = DriverManager.get_driver()
    driver.get("https://www.google.com/")
    time.sleep(10)

    yield
    print("TearDown")
    if driver:
        driver.quit()
