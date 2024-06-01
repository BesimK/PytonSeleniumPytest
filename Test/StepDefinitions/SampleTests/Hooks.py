from behave import *

use_step_matcher("re")


@given("I do something")
def step_impl(context):
    print("Given")


@when("I do another thing")
def step_impl(context):
    print("When")


@then("I should be OK")
def step_impl(context):
    print("Then")
