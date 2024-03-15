import sys


def str_to_morse(s: str):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }

    morse = [morse_dict[char] for char in s.upper() if char in morse_dict]

    if len(morse) != len(s):
        raise AssertionError("the arguments are bad")

    return ' '.join(morse)


def main():
    try:
        args = sys.argv[1:]

        if len(args) != 1:
            raise AssertionError("the arguments are bad")

        print(str_to_morse(args[0]))

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


if __name__ == "__main__":
    main()
