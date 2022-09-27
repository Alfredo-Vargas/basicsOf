# Syntax of lambdas:
# <lambda keyword> <list of arguments> <colon> <expression>
# Example: lambda x: 2 * x ** 3
def outer_func(f, value):
    return f(value)


def main() -> None:

    # with an outer function
    print(f"Lambda using outer function: {outer_func(lambda x: 2 * x**3, 4)}")

    # with a Immediately Invoked Function Expression (IFFE ~ pronounced "iffy")
    print("Lambda using Immediately Invoked Function Expression (IFFE):")
    print((lambda x, y: x + " " + y)("Johan", "Van Bauwel"))

    # lambda using positional arguments
    print("Lambda using positional arguments:")
    print((lambda x, y, z: x + y + z)(1, 2, 3))

    # lambda using keyword arguments
    print("Lambda using keyword arguments:")
    print((lambda x, y, z: x + y + z)(1, z=3, y=2))

    # lambda using default arguments
    print("Lambda using default arguments:")
    print((lambda x, y=3, z=4: x + y + z)(1))
    print((lambda x, y=3, z=4: x + y + z)(1, 2))
    print((lambda x, y=3, z=4: x + y + z)(1, 2, 3))

    # lambda using *args
    print("Lambda using *args:")
    print((lambda *args: sum(args))(1, 2, 3))

    # lambda using **kwargs
    print("Lambda using **kwargs:")
    print((lambda **kwargs: sum(kwargs.values()))(x=1, y=2, z=3))


if __name__ == "__main__":
    main()
