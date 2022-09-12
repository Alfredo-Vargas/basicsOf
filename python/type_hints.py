def luhn_checksum(number: str) -> bool:
    def digits_of(nr) -> list[int]:
        return [int(c) for c in nr]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0


# example of reason number 3
def is_eligible_for_bonus(
    contracts_landed: int, hours_worked: int, is_family: bool
) -> bool:
    if is_family:
        return True
    return contracts_landed > 0 and hours_worked > 40
    # if contracts_landed > 0 and hours_worked > 40:
    #     return True


# Reasons to use type hints
# Ref:https://www.youtube.com/watch?v=dgBCEB2jVU0&list=WL&index=30&t=79s
# Reason Number 1
"""Types help me write shorter documentation """
# Reason Number 2
"""Types are helpful while writing code"""
# Reason Number 3
"""Types hints make coupling more explicit"""
# Reason Number 4
"""Types hints force you to be explicit about your data structures"""
# Reason Number 5
"""Type hints simplify your code"""
