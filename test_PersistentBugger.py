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
