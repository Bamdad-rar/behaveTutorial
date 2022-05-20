from behave import *


@when("I try to multiply 2 with 3")
def _(context):
    context.result = 2 * 3


@given("that I dont want to see the decimal values")
def _(context):
    context.result = int(context.result)


@then("I will get 6 as a result")
def _(context):
    assert 6 == context.result
