import pytest

'''@pytest.mark.parametrize("a,b,c",[(1,2,3),(9,6,15)])
def test_functionAdd(a,b,c):
    assert a+b==c'''

@pytest.mark.parametrize("x,y,z",[("hi","hello","hihello"),("i"," am","i am")])
def test_functionConcat(x,y,z):
    assert x+y==z
