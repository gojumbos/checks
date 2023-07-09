
import check50
import check50.py


@check50.check()
def exists():
    """ Check that four4s.py exists """
    check50.exists("four4s.py")

@check50.check(exists)
def runs():
    """ File runs without syntax errors"""
    check50.py.compile("four4s.py")


@check50.check(runs)
def strings():
    """ File has only the allowed characters and operations """
    with open("four4s.py") as f:
        filedata = f.read()
        count4s = filedata.count("4")
        if count4s != 20:
            raise check50.Failure("You must use exactly four 4s in each number's calculation")

        count_eqs = filedata.count("=")
        if count_eqs != 5:
            raise check50.Failure("You can only assign the 5 variables shown in the template")

        if filedata.count("**") > 0:
            raise check50.Failure("You can only use basic math operations, no exponents")

        allowed_chars = ["4","=","/","*","+","-","(",")", " ","\n"]
        for char in allowed_chars:
            filedata = filedata.replace(char,"")

        if filedata != "zeroonetwothreefour":
            raise check50.Failure("You can only use basic math operations and must start from the template provided")



@check50.check(runs)
def equals_expected():
    """ Integer results are equal to expected values """
    one = check50.py.import_("four4s.py").one
    two = check50.py.import_("four4s.py").two
    three = check50.py.import_("four4s.py").three
    four = check50.py.import_("four4s.py").four
    names = [one, two, three, four]
    integers = [1, 2, 3, 4]
    for i in range(4):
        if names[i] != integers[i]:
            raise check50.Mismatch(names[i], integers[i])

