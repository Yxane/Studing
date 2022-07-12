def rec(x):
    if x <= 5:
        print(x)
        rec(x + 1)
        print(x)


def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


def fibonacci(x):
    if x == 1:
        return 0
    if x == 2:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)


def palindrome(some_string):
    if len(some_string) <= 1:
        return True
    if some_string[0] != some_string[-1]:
        return False
    return palindrome(some_string[1:-1])

def change_string(some_sting):
    if len(some_sting) == 1 or len(some_sting) == 2:
        return some_sting
    return some_sting[0]+"("+change_string(some_sting[1:-1])+")"+some_sting[-1]

if __name__ == '__main__':
    # rec(1)
    # print(fact(3))
    # print(fibonacci(10))
    # print(palindrome("asdddsa"))
    # print(palindrome("asddd"))
    print(change_string("a;sldkfjasl;dkf"))