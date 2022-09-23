def main():
    string = "a"
    none = None
    empty_string = ""
    empty_list = []
    empty_tuple = ()
    empty_set = set()
    empty_range = range(0)

    zero_int = 0
    zero_float = 0.0
    zero_complex = complex(0j)

    if string:
        print("\nAssigned strings are considered as a True.")
    if not none:
        print("\nNone is considered as False.")
    if not empty_string:
        print("\nEmpty strings are considered as a False.")
    if not empty_tuple:
        print("\nEmpty tuple is considered as False.")
    if not empty_list:
        print("\nEmpty list is considered as False.")
    if not empty_set:
        print("\nEmpty set is considered as False.")
    if not empty_range:
        print("\nEmpty range is considered as False.")
    if not zero_int:
        print("\nZero integer is considered as False.")
    if not zero_float:
        print("\nZero float is considered as False.")
    if not zero_complex:
        print("\nZero comples is considered as False.")


if __name__ == "__main__":
    main()
