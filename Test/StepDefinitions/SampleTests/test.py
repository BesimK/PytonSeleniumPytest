from behave import *

from Main.Utilities.Pages import Pages
from Main.Utilities.SoftAssertions import SoftAssertions

use_step_matcher("re")


@given("user is navigated to Wikipedia")
def step_impl(context):
    Pages.get_homepage().wikipedia()


@when('user makes a search for "(.+)"')
def step_impl(context, text):
    Pages.get_homepage().search(text)


@then('user should see "(.+)"')
def step_impl(context, expected):
    actual = Pages.get_homepage().take_title()
    SoftAssertions.assert_that(actual, "Wikipedia Title").is_equal_to(expected)


@then("user should see right picture")
def step_impl(context):
    pass
