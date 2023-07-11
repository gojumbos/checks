
import check50
import check50.py


@check50.check()
def exists():
    """ Check that secret_codes.py exists """
    check50.exists("secret_codes.py")

@check50.check(exists)
def runs():
    """ File runs without syntax errors """
    check50.py.compile("secret_codes.py")

@check50.check(runs)
def safe():
    """ Main func prints Safe for bad input"""
    out = check50.run("python secret_codes.py").stdin("[-1]").stdin("0").stdin("0").stdout()
    if out != "Safe":
        raise check50.Mismatch("Safe", out)


@check50.check(runs)
def check_1():
    """ Main func prints correctly """
    out = check50.run("python secret_codes.py").stdin("[0,1,2,3,4]").stdin("1").stdin("2").stdout()
    if out != "[2,3]":
        raise check50.Mismatch("[2,3]", out)

@check50.check(runs)
def check_2():
    """ Main func prints correctly when signal is last character """
    out = check50.run("python secret_codes.py").stdin("[5,7,6,8]").stdin("8").stdin("4").stdout()
    if out != "[]":
        raise check50.Mismatch("[2,3]", out)

