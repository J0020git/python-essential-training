class NonIntArgumentException(Exception):
    pass


def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != int:
                raise NonIntArgumentException()
        return func(*args)

    return wrapper


@handleNonIntArguments
def sum(a, b, c):
    return a + b + c


try:
    result = sum(1, 2, "a")
    print("This should not print out")
except NonIntArgumentException as e:
    print("Hooray!")
