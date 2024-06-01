from Main.Utilities.DriverManager import DriverManager
from allure_behave.hooks import allure_report


def after_scenario(context, scenario):
    allure_report()
    DriverManager.quit_driver()
    print(f"after_scenario: Finished scenario: {scenario.name}")


def before_all(context):
    DriverManager.get_driver()
    print("before_all: Running once before all tests")


def after_all(context):
    DriverManager.quit_driver()
    print("after_all: Running once after all tests")

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
# def before_scenario(context, scenario):
#     """
#     Runs before each scenario.
#     """
#     print(f"before_scenario: Starting scenario: {scenario.name}")
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
