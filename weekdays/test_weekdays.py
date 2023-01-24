import unittest
from datetime import date
from weekdays import weekdays


class TestWeekdays(unittest.TestCase):
    """Implement tests for weekdays here."""
    date1 = date(2023, 1, 22)
    date2 = date(2023, 1, 23)
    date3 = date(2023, 1, 24)
    date4 = date(2023, 1, 29)

    def testWeekdays1(self):
        self.assertEqual(40, weekdays(self.date1, self.date4))

    def testWeekdays2(self):
        self.assertEqual(16, weekdays(self.date2, self.date3))


if __name__ == "__main__":
    unittest.main()
