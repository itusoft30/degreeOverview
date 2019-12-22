import unittest
import sys
sys.path.insert(0,'../..')
from project import app
import sqlalchemy


sqlalchemy.engine = sqlalchemy.create_engine('postgres://zgolxdxdhgqrwk:3f2f58e0d6baa234f1569a4a92bf9043c48a534edb6027902e488c8999fe8e33@ec2-174-129-33-30.compute-1.amazonaws.com:5432/df6qc7mlpccpkh')
connection = sqlalchemy.engine.connect()

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

    def test_Register_Small_Password(self):
        response = self.app.post('/register',
                      data=dict(name='test', surname='test',
                                email='akyuzi15',password='test',
                                confirm_password='test'),
                      follow_redirects=True)
        self.assertIn(b'Field must be between 5 and 10 characters long.', response.data)

    def test_Register_Wrong_ConfirmPassword(self):
        response = self.app.post('/register',
                      data=dict(name='test123', surname='test123',
                                email='akyuzi15',password='test123',
                                confirm_password='test'),
                      follow_redirects=True)
        self.assertIn(b'Field must be equal to password.', response.data)

    def test_Register_Same_Email(self):
        response = self.app.post('/register',
                      data=dict(name='test123', surname='test123',
                                email='akyuzi15',password='test123',
                                confirm_password='test123',department=1,
                                title='pro'),
                      follow_redirects=True)
        self.assertIn(b'The email is already taken.', response.data)

    def test_Register_Same_Email(self):
        response = self.app.post('/register',
                      data=dict(name='test123', surname='test123',
                                email='akyuzi15',password='test123',
                                confirm_password='test123',department=1,
                                title='pro'),
                      follow_redirects=True)
        self.assertIn(b'The email is already taken.', response.data)

    def test_Register_True(self):
        response = self.app.post('/register',
                      data=dict(name='test123', surname='test123',
                                email='akyuzi15',password='test123',
                                confirm_password='test123',department=1,
                                title='pro'),
                      follow_redirects=True)
        self.assertIn(b'The email is already taken.', response.data)

if __name__ == '__main__':
    unittest.main()
