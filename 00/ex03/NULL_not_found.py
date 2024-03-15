def isNan(n):
    return n != n


def NULL_not_found(object: any) -> int:
    nullnames = {
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake",
    }

    objtype = type(object)
    objname = nullnames.get(type(object))

    if object is None:
        print(f"Nothing: {object} {objtype}")
    elif (objtype is float and isNan(object)) \
            or (objtype is int and object == 0) \
            or (objtype is str and object == '') \
            or (objtype is bool and not object):
        print(f"{objname}: {object} {objtype}")
    else:
        print("Type not found")
        return 1

    return 0
