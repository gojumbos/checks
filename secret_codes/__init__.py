
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
    out = check50.run("python secret_codes.py").stdin("[1]").stdin("0").stdin("0").stdout()
    if "Safe" not in out:
        raise check50.Mismatch("Safe", out)


@check50.check(runs)
def check_1():
    """ Main func prints correctly """
    out = check50.run("python secret_codes.py").stdin("[0,1,2,3,4]").stdin("1").stdin("2").stdout()
    if "[2, 3]" not in out :
        raise check50.Mismatch("[2,3]", out)
    for x in ["0","1","4"]:
        if x in out:
            raise check50.Failure("You printed out something extra " + str(x))

@check50.check(runs)
def check_2():
    """ Main func prints correctly when signal is last character """
    out = check50.run("python secret_codes.py").stdin("[5,7,6,8]").stdin("8").stdin("4").stdout()
    if "[]" not in out:
        raise check50.Mismatch("[]", out)
    for x in ["5","7","6","8"]:
        if x in out:
            raise check50.Failure("You printed out something extra " + str(x))

@check50.check(runs)
def check_3():
    """ Main func prints correctly when signal is first character """
    out = check50.run("python secret_codes.py").stdin("[5,7,6,8]").stdin("5").stdin("3").stdout()
    if "[7, 6, 8]" not in out:
        raise check50.Mismatch("[7,6,8]", out)



