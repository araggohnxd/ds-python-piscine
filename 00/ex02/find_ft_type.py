def all_thing_is_obj(object: any) -> int:
    typenames = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    objtype = type(object)
    objname = typenames.get(objtype, "Type not found")

    if objtype == str:
        print(f"{object} is in the kitchen : {objtype}")
    elif objname != "Type not found":
        print(f"{objname} : {objtype}")
    else:
        print(objname)

    return 42
