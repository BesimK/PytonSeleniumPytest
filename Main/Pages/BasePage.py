from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Main.Utilities.DriverManager import DriverManager


class BasePage:
    def _init_(self):
        self.driver = DriverManager.get_driver()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)
        self.init_elements()

    def init_elements(self):
        # This method allows you to initialize elements like Java's PageFactory.initElements()
        pass

    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_visible(self, locator):
        try:
            self.wait_for_element(locator)
            return True
        except TimeoutException:
            return False

    def is_enabled(self, locator):
        try:
            element = self.find_element(locator)
            return element.is_enabled()
        except TimeoutException:
            return False

    def get_attribute(self, locator, attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_for_element_to_be_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_text_to_be_present_in_element(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_url_to_change(self, old_url):
        return self.wait.until(EC.url_changes(old_url))

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def get_page_source(self):
        return self.driver.page_source

    def select_dropdown_by_value(self, locator, value):
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)

    def select_dropdown_by_visible_text(self, locator, text):
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def switch_to_frame(self, locator):
        element = self.find_element(locator)
        self.driver.switch_to.frame(element)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_alert_text(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert.text

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(self, locator):
        try:
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def upload_file(self, locator, file_path):
        element = self.find_element(locator)
        element.send_keys(file_path)

    def hover_over_element(self, locator):
        element = self.find_element(locator)
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def double_click(self, locator):
        element = self.find_element(locator)
        actions = webdriver.ActionChains(self.driver)
        actions.double_click(element).perform()

    def right_click(self, locator):
        element = self.find_element(locator)
        actions = webdriver.ActionChains(self.driver)
        actions.context_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        actions = webdriver.ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def is_selected(self, locator):
        element = self.find_element(locator)
        return element.is_selected()

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def refresh_page(self):
        self.driver.refresh()

    def navigate_back(self):
        self.driver.back()

    def navigate_forward(self):
        self.driver.forward()

    def clear_input_field(self, locator):
        element = self.find_element(locator)
        element.clear()

    def download_file(self, locator, download_path):
        element = self.find_element(locator)
        element.send_keys(download_path)

    def select_checkbox(self, locator):
        checkbox = self.find_element(locator)
        if not checkbox.is_selected():
            checkbox.click()

    def deselect_checkbox(self, locator):
        checkbox = self.find_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def select_radio_button(self, locator):
        radio_button = self.find_element(locator)
        if not radio_button.is_selected():
            radio_button.click()

    def press_key(self, locator, key):
        element = self.find_element(locator)
        element.send_keys(key)

    def press_enter(self, locator):
        self.press_key(locator, Keys.ENTER)

    def press_escape(self, locator):
        self.press_key(locator, Keys.ESCAPE)
