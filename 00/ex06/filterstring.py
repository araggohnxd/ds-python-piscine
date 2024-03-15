from ft_filter import ft_filter
import sys


def main():
    """
    Prints the result of filtering a list of strings for words S that have a
    length greather than N. The first argument should be a string with each
    word separated by a space.

    If no argument is provided, prints an error.

    If more than two arguments are provided, prints an error.

    If the second argument is not an integer, prints an error.
    """

    try:
        args = sys.argv[1:]

        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        try:
            n = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(list(ft_filter(lambda s: len(s) > n, args[0].split())))

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


if __name__ == "__main__":
    main()
