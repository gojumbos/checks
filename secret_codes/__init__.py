
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


check50.check(runs)
def type_ret():
    # imprt = check50.py.import_("secret_codes.py")
    out = check50.run("python secret_codes.py").stdin([]).stdin(0).stdin(0).stdout()
    print(out)
