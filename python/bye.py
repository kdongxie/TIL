def hello(func):
    def wrapper():
        print("hihi")
        func()
        print("hihi")
    return wrapper()


@hello
def bye():
    print("bye bye")

if __name__ == "__main__":
    bye()
