
import check50
import check50.py


@check50.check()
def exists():
    """ Check that secret_codes.py exists """
    check50.exists("secret_codes.py")

@check50.check(exists)
def runs():
    """ File runs without syntax errors"""
    check50.py.compile("secret_codes.py")


@check50.check(runs)
def has_main():
    imprt = check50.py.import_("secret_codes.py")
    if not imprt.main():
        raise check50.Failure("Your program does not have a main() function")
