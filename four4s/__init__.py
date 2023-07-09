import check50
import check50.py


@check50.check()
def exists():
    """ Check that four4s.py exists """
    check50.exists("four4s.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("four4s.py")
