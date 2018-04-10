from rot13 import Rot13
from sign_up import SignUp
import unittest


class TestRot13(unittest.TestCase):
    def test_rot13(self):
        rot = Rot13()
        self.assertEqual(rot.rot13_transform('abc'), 'nop')
        self.assertEqual(rot.rot13_transform('    '), '    ')
        self.assertEqual(rot.rot13_transform('#$%^'), '#$%^')


class TestSignUp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.signup = SignUp()

    def testValidateUsername(self):
        self.assertTrue(self.signup.valid_username('dfdsjiuoew'))
        self.assertTrue(self.signup.valid_username('dye7210843'))

        self.assertFalse(self.signup.valid_username('#$%^%#ds'))
        self.assertFalse(self.signup.valid_username('djfdu923*&'))
        self.assertFalse(self.signup.valid_username('  '))
        self.assertFalse(self.signup.valid_username(''))
        self.assertFalse(self.signup.valid_username('aa'))
        self.assertFalse(self.signup.valid_username('a' * 21))

    def testValidatePassword(self):
        self.assertTrue(self.signup.valid_password('*(&(*&jkdu'))
        self.assertTrue(self.signup.valid_password('            '))
        self.assertTrue(self.signup.valid_password('80382jkldsa'))

        self.assertFalse(self.signup.valid_username('  '))
        self.assertFalse(self.signup.valid_username(''))
        self.assertFalse(self.signup.valid_username('ab'))
        self.assertFalse(self.signup.valid_username('a' * 21))

    def testValidateEmail(self):
        self.assertTrue(self.signup.valid_email('abc@gma.com'))
        self.assertTrue(self.signup.valid_email('190283@aol.net'))

        self.assertFalse(self.signup.valid_username('aa@gmail'))
        self.assertFalse(self.signup.valid_username('@aol.com'))
        self.assertFalse(self.signup.valid_username('gdjuieow.com'))
        self.assertFalse(self.signup.valid_username(''))

if __name__ == '__main__':
    unittest.main()
