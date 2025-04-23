# tuple
def sum(*args):
    result = 0
    for number in range(0, len(args)):
        result += args[number]
        print(f"now, the result is {result}")
    return result


print(sum(1, 2, 3, 4, 5, 6))


# keyword
def infos(**info):
    print(info)
    print(type(info))


infos(name="Chucky", age=38, address="TW")


# tuple & keyword
def texts(*tuples, **keywords):
    print("I want like to eat {} {}".format(tuples[0], keywords["food"]))


texts(14, 3, name="Chucky", food="eggs")
