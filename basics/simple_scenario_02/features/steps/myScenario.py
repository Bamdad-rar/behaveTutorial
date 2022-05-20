from behave import *

@when('When I add the numbers "{first_number}" and "{second_number}"')
def _(context,first_number,second_number):
    context.result = int(first_number) + int(second_number)
    
    
@then('The result must be "{result}"')
def _(context,result):
    assert context.result == int(result)

