def ft_filter(function, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items that are
    true.
    """

    if function is None:
        return (item for item in iterable if item)

    return (item for item in iterable if function(item))


def main():
    """
    Some tests for ft_filter.
    """

    charlist = ['g', 'e', 'j', 'a', 's', 'p', 'r', 'i']
    filter_charlist = filter(lambda c: c in ['a', 'e', 'i'], charlist)

    print(charlist, list(filter_charlist))

    numlist = [3, 0, 1, 2]
    filter_numlist = filter(None, numlist)

    print(numlist, list(filter_numlist))


if __name__ == "__main__":
    main()
