def factorial(num):
    if type(num) != int or num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
