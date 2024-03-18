def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculates the BMI of each pair of height and weight given.

    ```
    BMI == w / h ^ 2
    BMI => Body mass index
      w => Weight
      h => Height
    ```

    `height`
        List of heights.

    `weight`
        List of weights.

    Returns:
    A list with the calculated BMIs.
    """

    try:
        assert height is not None and weight is not None, \
        "arguments must not be None"

        assert len(weight) == len(height), "lists differ in size"

        assert all(isinstance(value, (int, float)) for value in height), \
               "list values must be either int or float"

        assert all(isinstance(value, (int, float)) for value in weight), \
               "list values must be either int or float"

        assert min(height) >= 0 and min(weight) >= 0, \
               "list values must be positive"

        return [w / h ** 2 for w, h in zip(weight, height)]

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applies a limit on a list of BMIs.

    `bmi`
        List of BMIs to limit.

    `limit`
        Value to limit to.

    Returns:
    A list of booleans indicating wether the BMI at a given index is above the
    limit or not.
    """

    try:
        assert bmi is not None and limit is not None, \
               "arguments must not be None"

        assert all(isinstance(value, (int, float)) for value in bmi), \
               "list values must be either int or float"

        assert isinstance(limit, int), "limit must be int"

        assert min(bmi) >= 0 and limit >= 0, \
               "list and limit values must be positive"

        return [value > limit for value in bmi]

    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")


def main():
    """
    Some tests for `give_bmi` and `apply_limit`.
    """

    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
