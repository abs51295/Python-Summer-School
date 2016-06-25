a = 42


def foo():
    # global a
    # a = 13
    print("Inside foo")


foo()


def foo():
    print("Inside boo")

foo()
