# Copied from: https://docs.python.org/3/library/unittest.html
import basicCommands as basic
import unittest as test


class TestBacisCommandsMethods(test.TestCase):

    def test_totalSeconds_AllZero(self):
        """
        Test totalSeconds function
        """
        result = basic.totalSeconds(0, 0, 0)
        self.assertEqual(result, 0, "Should be 0")

    def test_totalSeconds_OneHour(self):
        """
        Test totalSeconds function - 1 hour
        """
        result = basic.totalSeconds(1, 0, 0)
        self.assertEqual(result, 3600, "Should be 3,600")

    def test_totalSeconds_OneMinute(self):
        """
        Test totalSeconds function - 1 minutes
        """
        result = basic.totalSeconds(0, 1, 0)
        self.assertEqual(result, 60, "Should be 60")

    def test_totalSeconds_OneSecond(self):
        """
        Test totalSeconds function - 1 second
        """
        result = basic.totalSeconds(0, 0, 1)
        self.assertEqual(result, 1, "Should be 1")


def test_kilometerToMile(self):
    """
    Test kilometerToMile function - 1.61 kilometer
    """
    result = basic.kilometerToMile(1.61)
    self.assertEqual(result, 1, "Should be 1")


if __name__ == '__main__':
    test.main()
