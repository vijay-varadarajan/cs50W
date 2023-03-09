# python allows functional programming paradigm
def announce(f):
    def wrapper():
        print("Function begins")
        f()
        print("Function ends")
    return wrapper

@announce
def hello():
    print("hello, world")

hello()