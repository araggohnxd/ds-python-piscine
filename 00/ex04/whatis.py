import sys

args = sys.argv[1:]

try:
    if len(args) == 1:
        try:
            n = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")

        print("I'm Even." if n % 2 == 0 else "I'm Odd.")

    elif len(args) > 1:
        raise AssertionError("more than one argument is provided")

except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
