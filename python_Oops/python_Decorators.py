def greet(fx):
    def mfx(
        *args, **kwargs
    ):  # for accepting arguments in the function we need to write this
        print("Good Morning")
        result = fx(*args, **kwargs)
        print("Thanks for using this function")
        return result

    return mfx


@greet
def hello():
    print("Hello world")


@greet
def add(a, b):
    print("print a + b : ", a + b)
    return a + b


# greet(hello)()
hello()
# greet(add)(1, 2)
result = add(1, 2)
print("Result : ", result)
