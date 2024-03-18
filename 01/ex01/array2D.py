def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of a 2D array and truncates it, printing its new shape.

    `family`
        List to print and truncate.

    `start`
        Index to start truncation.

    `end`
        Index to stop truncation.

    Returns:
    The truncated list.
    """

    try:
        assert isinstance(family, list), \
               "family must be a list"

        assert all(isinstance(item, list) for item in family), \
               "family must be a list of lists"

        assert isinstance(start, int), \
               "start must be an int"

        assert isinstance(end, int), \
               "end must be an int"

        assert all(len(item) == len(family[0]) for item in family), \
               "lists in family differ in size"

        result = family[start:end]

        print(f"My shape is : ({len(family)}, {len(family[0])})")
        print(f"My new shape is : ({len(result)}, {len(result[0])})")

        return result

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


def main():
    """
    Some tests for `slice_me`.
    """

    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
