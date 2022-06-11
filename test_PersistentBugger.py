from PersistentBugger import main

# initial test
def test_init():
    assert (main()) == False


# 1 input validation
def test_StringInput():
    """Input is string, return False"""
    param = "1"
    assert (main(param)) == False


def test_NegativeInput():
    """Input is negative, return False"""
    param = -1
    assert (main(param)) == False


def test_Zero():
    """Input is zero, return zero"""
    param = 0
    assert (main(param)) == 0


def test_SingleDigits():
    """Input is single digit, return 0"""
    param = 9
    assert (main(param)) == 0


# 2a one-cyle nums


def test_OneCycle1():
    """Input is 11, return 1 (1*1=1)"""
    param = 11
    assert (main(param)) == 1


def test_OneCycle2():
    """Input is 22, return 1 (2*2=4)"""
    param = 22
    assert (main(param)) == 1


def test_OneCycle3():
    """Input is 33, return 1 (3*3=9)"""
    param = 33
    assert (main(param)) == 1
