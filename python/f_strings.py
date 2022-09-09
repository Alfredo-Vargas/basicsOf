import datetime
from dataclasses import dataclass


@dataclass  # provides a wrapper method for printing
class User:
    first_name: str
    last_name: str

    # This instroduces a user friendly method for printing
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


def main():
    number = 800
    print(f"The number {number} in hex is {number:x}.")
    print(f"The number {number} in octal is {number:o}.")
    print(f"The number {number} in scientific is {number:e}.")
    print(f"The number {number} padded with size 6 is {number:06}.")
    print(f"The number {number} with two decimal places {number:.2f}.")
    print(f"\nA big number with comma separator is {44000000000:,.2f}")
    print(f"To print a percentage: {0.34567:.2%}\n")

    for i in range(8, 12):
        print(f"The number right aligned is {i:6}.")

    print()
    greet = "Hi"
    print(f"To right aling a string: {greet:>10}")
    print(f"To center a string: {greet:^10}")
    print(f"To left align a string: {greet:<10}")

    print("You can specify a char for the padding:")
    print(f"To right aling a string: {greet:_>10}")
    print(f"To center a string: {greet:_^10}")
    print(f"To left align a string: {greet:_<10}")

    user = User("Elon", "Musk")
    print(f"User printed using the dunder str method: {user}.")
    print(f"User printed using the wrapper developer method: {user!r}.")
    print(f"User printed using the repr method: {repr(user)}.")
    name = "Elon"
    print(f"Name printed using the raw option, includes single quotes: {name!r}\n")

    today = datetime.datetime.now()
    print(f"Simple date printing: {today}.")
    print(f"Show the hours and minutes: {today:%H:%M}.")
    print(f"Show the hours minutes seconds and miliseconds: {today:%H:%M:%S.%f}.")
    print(f"Show the year month day hours minutes seconds and miliseconds: {today:%Y-%M-%H %H:%M:%S.%f}.")
    print(f"Show only the last two digits of the year: {today:%y}.")
    print(f"Show only date: {today:%D}.")
    print(f"Show only time: {today:%T}.")
    print(f"Show the week day name: {today:%A}.")
    print(f"Show the month name: {today:%B}.")
    print(f"Show the date according to current local : {today:%x}.")
    print(f"Show the time according to current local : {today:%X}.\n")

    print(f"{{single braces}}")
    print(f"{{{{double braces}}}}")
    dictionary = {"hello": "world"}
    print(f"Printing a dictionary value, Hello {dictionary['hello']}\n")

    x = 45
    y = 78
    print(f"Some debugging techniques: {x=}, {y=}")
    print(f"Some debugging techniques: {x = }, {y = }")

    # Multiline strings
    name = "Albert"
    country = "Germany"
    city = "Ulm"
    sentence = (
            f"The physicist {name} "
            f"is from {country}. "
            f"He was born in the city called {city}."
            )
    print(sentence)


if __name__ == "__main__":
    main()
