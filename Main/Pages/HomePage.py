import time
from Main.Pages.BasePage import BasePage
from Main.Pages.PageLocators.HomePageLocators import HomePageLocators


class HomePage(BasePage):
    def __init__(self):
        super()._init_()

    def click_pay_now_button(self):
        return self.click(HomePageLocators.PayNowButton)

    def do_the_trick(self):
        self.open(HomePageLocators.dummyUrl1)
        time.sleep(10)

