import unittest
import sys
sys.path.insert(0,'../..')
from project import app

def add(x,y):
    return x+y

class Test(unittest.TestCase):
    def test_add(self):
        result = add(2,4)
        self.assertEqual(result,6)

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/courses', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
