# Syntax of maps and filter

# the function map takes a function and an iterable and returns an iterable whose values are
# the function the function applied to every input iterable value

# a filter will be applied to an iterable whose return value is a filter object
# the return values of the filter object need to match a given condition


def addtwo(item):
    return item + 2


def main() -> None:
    # the iterable datatype will be just a the address in memory
    print(f"The map will return the address of the iterable: {map(addtwo, [1,2,3])}")
    print(f"Iterable casted to a list: {list(map(addtwo, [1,2,3]))}")

    # map and lambda together
    print(f"Map and lambda together: {list(map(lambda x: x + 2, [1, 2, 3]))}")

    # using a filter
    mylist = [x for x in range(10)]
    print(f"Casting to a list a filter: {list(filter(lambda x: x % 2 == 0, mylist))}")

    # using map instead of a filter
    print(f"Casting to a list a map: {list(map(lambda x: x % 2 == 0, mylist))}")

if __name__ == "__main__":
    main()
