import new_pytest

def function_pytest_test(x):
    return x * 10

def test_pytest_function():
    assert function_pytest_test(3)==30
    assert function_pytest_test(4)==40
    assert function_pytest_test(5)==40

def function_add_test(a,b):
    return a+b
def test_add_function():
    assert function_add_test(20,30)==50
def fun_sub_test(a,b):
    return a-b
def test_sub_fun():
    assert fun_sub_test(156,23)==133