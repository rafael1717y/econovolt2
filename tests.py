import unittest
from app import create_app
from app.ext.auth.models import User 

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()


    def test_password_hashing(self):
        u = User(username='susan55')
        u.set_password('cat5')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat5')) 

    



if __name__ == '__main__':
    unittest.main(verbosity=2)