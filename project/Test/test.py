import unittest
import sys
sys.path.insert(0,'../..')
from project import app


class Test(unittest.TestCase):
    def setUp(self) :
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index(self):

        response = self.app.get('/courses', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_goTo_profile(self):
        response = self.app.get('/profile',follow_redirects=True)
        self.assertTrue(b'Please log in to access this page.' in response.data)

    def test_True_login(self):
        response = self.app.post('/login', data=dict(email='akyuzi15', password='admin'),follow_redirects=True)
        self.assertIn(b'PROFILE',response.data)

    def test_False_login(self):
        response = self.app.post('/login', data=dict(email='akyuzi15', password='admin12'),follow_redirects=True)
        self.assertIn(b'Login Unsuccessful. Please check email and password',response.data)

    def test_logut(self):
        self.app.post('/login', data=dict(email='akyuzi15', password='admin'), follow_redirects=True)
        response = self.app.get('/logout', follow_redirects=True)
        self.assertIn(b'WELCOME TO', response.data)

    def test_Register_Same_Email(self):
        response = self.app.post('/register',
                      data=dict(name='test', surname='test',
                                email='akyuzi15',password='test',
                                confirm_password='test',department='Economy',
                                title='test'),
                      follow_redirects=True)
        self.assertIn(b'The email is already taken.', response.data)



if __name__ == '__main__':
    unittest.main()
