import time

import allure
from datetime import datetime
from allure_combine import combine_allure
from Main.Pages.BasePage import BasePage
from Main.Utilities import Helpers
from Main.Utilities.DriverManager import DriverManager
from Main.Utilities.Pages import Pages


def before_all(context):
    browser = context.config.userdata.get('Browser', 'chrome')
    DriverManager.get_driver(browser)
    context.pages = Pages()
    print("----------------------------Tests Has Been Started----------------------------")


def before_scenario(context, scenario):
    browser = context.config.userdata.get('Browser', 'chrome')
    DriverManager.get_driver(browser)
    print(f"before_scenario: Starting scenario: {scenario.name}")


def after_scenario(context, scenario):
    browser = context.config.userdata.get('Browser', 'chrome')
    if scenario.status == 'failed':
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"screenshot_{browser}_{timestamp}.png"
        screenshot = DriverManager.get_driver().get_screenshot_as_png()
        allure.attach(screenshot, name=screenshot_name, attachment_type=allure.attachment_type.PNG)
    DriverManager.quit_driver()
    print(f"----------------------------Scenario:{scenario.name} Has Been Ended ----------------------------")


def after_all(context):
    DriverManager.quit_driver()
    driver = context.config.userdata.get('Browser', 'chrome')
    Helpers.generate_report(driver)
    print("----------------------------Tests Has Been Ended----------------------------")

# def before_feature(context, feature):
#     """
#     Runs before each feature.
#     """
#     print(f"before_feature: Starting feature: {feature.name}")
#
#
# def after_feature(context, feature):
#     """
#     Runs after each feature.
#     """
#     print(f"after_feature: Finished feature: {feature.name}")
#
#
#
#
# def before_step(context, step):
#     """
#     Runs before each step.
#     """
#     print(f"before_step: Starting step: {step.name}")
#
#
# def after_step(context, step):
#     """
#     Runs after each step.
#     """
#     print(f"after_step: Finished step: {step.name}")
#
#
# def before_tag(context, tag):
#     """
#     Runs before each tag.
#     """
#     print(f"before_tag: Before tag: {tag}")
#
#
# def after_tag(context, tag):
#     """
#     Runs after each tag.
#     """
#     print(f"after_tag: After tag: {tag}")
