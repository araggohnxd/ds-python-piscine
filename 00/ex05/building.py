import sys
import string


def count(s: str):
    """
    s
        string to count from

    Counts how many uppercase, lowercase, punctuation, whitespace and digit
    characters are there in the provided string.
    """

    count_uppercase = sum(map(str.isupper, s))
    count_lowercase = sum(map(str.islower, s))
    count_punctuaton = sum(1 for char in s if char in string.punctuation)
    count_whitespace = sum(map(str.isspace, s))
    count_digits = sum(map(str.isdigit, s))

    print(f"{count_uppercase} upper letters")
    print(f"{count_lowercase} lower letters")
    print(f"{count_punctuaton} punctuation marks")
    print(f"{count_whitespace} spaces")
    print(f"{count_digits} digits")


def main():
    """
    Prints how many uppercase, lowercase, punctuation, whitespace and digit
    characters are there in the provided string.

    If no argument is provided, prompts for input.

    If more than one argument is provided, prints an error.
    """

    try:
        args = sys.argv[1:]

        if len(args) > 1:
            raise AssertionError("more than one argument provided")
        elif len(args) < 1:
            print("What is the text to count?")
            s = sys.stdin.read()
        else:
            s = args[0]

        count(s)

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        exit(1)


if __name__ == "__main__":
    main()
