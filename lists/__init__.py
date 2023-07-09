
import check50
import check50.py


@check50.check()
def exists():
    """ Check that arrays.py exists """
    check50.exists("arrays.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("arrays.py")


@check50.check(run)
def tip1():
    """ The last 3 digits is correct """
    out = check50.run("python arrays.py").stdin("[3, 4, 5, 6, 7, 8]").stdin("3").stdout()
    if not out.strip() == "21":
        raise check50.Mismatch("21", out, help="Bad output for last 3 digits")


