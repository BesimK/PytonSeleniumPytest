import requests
import io
from PIL.Image import Image
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Main.Utilities.DriverManager import DriverManager
from PIL import Image, ImageChops


class BasePage:
    def __init__(self):
        self.driver = DriverManager.get_driver()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)

    def _wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def _open(self, url):
        self.driver.get(url)

    def _click(self, locator):
        element = self._find_element(locator)
        element.click()

    def _enter_text(self, locator, text):
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def _is_visible(self, locator):
        try:
            self._wait_for_element(locator)
            return True
        except TimeoutException:
            return False

    def _is_enabled(self, locator):
        try:
            element = self._find_element(locator)
            return element.is_enabled()
        except TimeoutException:
            return False

    def _get_attribute(self, locator, attribute):
        element = self._find_element(locator)
        return element.get_attribute(attribute)

    def _wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def _wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _wait_for_element_to_be_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def _wait_for_element_to_be_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def _wait_for_text_to_be_present_in_element(self, locator, text):
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def _wait_for_url_to_change(self, old_url):
        return self.wait.until(EC.url_changes(old_url))

    def _get_current_url(self):
        return self.driver.current_url

    def _get_title(self):
        return self.driver.title

    def _get_page_source(self):
        return self.driver.page_source

    def _select_dropdown_by_value(self, locator, value):
        element = self._find_element(locator)
        select = Select(element)
        select.select_by_value(value)

    def _select_dropdown_by_visible_text(self, locator, text):
        element = self._find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)

    def _scroll_to_element(self, locator):
        element = self._find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def _switch_to_frame(self, locator):
        element = self._find_element(locator)
        self.driver.switch_to.frame(element)

    def _switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def _switch_to_window(self, window_name):
        self.driver.switch_to.window(window_name)

    def _take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def _accept_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    def _dismiss_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def _get_alert_text(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert.text

    def _is_element_present(self, locator):
        try:
            self._find_element(locator)
            return True
        except TimeoutException:
            return False

    def _wait_for_element_to_disappear(self, locator):
        try:
            WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def _upload_file(self, locator, file_path):
        element = self._find_element(locator)
        element.send_keys(file_path)

    def _hover_over_element(self, locator):
        element = self._find_element(locator)
        actions = webdriver.ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def _double_click(self, locator):
        element = self._find_element(locator)
        actions = webdriver.ActionChains(self.driver)
        actions.double_click(element).perform()

    def _right_click(self, locator):
        element = self._find_element(locator)
        actions = webdriver.ActionChains(self.driver)
        actions.context_click(element).perform()

    def _drag_and_drop(self, source_locator, target_locator):
        source_element = self._find_element(source_locator)
        target_element = self._find_element(target_locator)
        actions = webdriver.ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

    def _is_selected(self, locator):
        element = self._find_element(locator)
        return element.is_selected()

    def _execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    def _add_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def _get_cookie(self, name):
        return self.driver.get_cookie(name)

    def _delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def _delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def _refresh_page(self):
        self.driver.refresh()

    def _navigate_back(self):
        self.driver.back()

    def _navigate_forward(self):
        self.driver.forward()

    def _clear_input_field(self, locator):
        element = self._find_element(locator)
        element.clear()

    def _download_file(self, locator, download_path):
        element = self._find_element(locator)
        element.send_keys(download_path)

    def _select_checkbox(self, locator):
        checkbox = self._find_element(locator)
        if not checkbox.is_selected():
            checkbox.click()

    def _deselect_checkbox(self, locator):
        checkbox = self._find_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def _select_radio_button(self, locator):
        radio_button = self._find_element(locator)
        if not radio_button.is_selected():
            radio_button.click()

    def _press_key(self, locator, key):
        element = self._find_element(locator)
        element.send_keys(key)

    def _press_enter(self, locator):
        self._press_key(locator, Keys.ENTER)

    def _press_escape(self, locator):
        self._press_key(locator, Keys.ESCAPE)

    def _load_image_from_disk(self, path):
        return Image.open(path)

    def _load_image_from_web(self, element):
        # Capture the image from the web element
        img_src = element.get_attribute("src")
        image_content = requests.get(img_src).content
        return Image.open(io.BytesIO(image_content))

    def _compare_images(self, path, element):
        # Ensure both images are in the same mode and size
        expected = self._load_image_from_disk(path)
        print("expected")
        actual = self._load_image_from_web(element)
        print("actual")
        if expected.mode != actual.mode or expected.size != actual.size:
            return False
        # Calculate the difference
        diff = ImageChops.difference(expected, actual)
        # If diff is all black, the images are the same
        if not diff.getbbox():
            return True
        return False
