from project import app
import unittest


class Test(unittest.TestCase):
    def test_home(self):
        result = add(2,4)
        self.assertEqual(result,6)


if __name__ == '__main__':
    unittest.main()
