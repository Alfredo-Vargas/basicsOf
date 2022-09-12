import unittest
import calc

# Can run this in terminal by:
# python -m unittest test_calc.py
# Output must be a dot for each successful test
# Also number of tests performed and final status is printed


class TestCalc(unittest.TestCase):
    # Test functions that do not start with test_ are not called
    def add_test(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()

# Methods and what it Checks.
# Ref: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

# assertEqual(a, b)
# a == b

# assertNotEqual(a, b)
# a != b

# assertTrue(x)
# bool(x) is True

# assertFalse(x)
# bool(x) is False

# assertIs(a, b)
# a is b

# assertIsNot(a, b)
# a is not b

# assertIsNone(x)
# x is None

# assertIsNotNone(x)
# x is not None

# assertIn(a, b)
# a in b

# assertNotIn(a, b)
# a not in b

# assertIsInstance(a, b)
# isinstance(a, b)

# assertNotIsInstance(a, b)
# not isinstance(a, b)
