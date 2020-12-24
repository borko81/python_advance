import unittest
from work_with_testing.employee import *


class TestEmployee1(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee('Boris', 'St', 50000)
        emp_2 = Employee('Sue', 'Meg', 60000)

        self.assertEqual(emp_1.email, 'Boris.St@email.com')
        self.assertEqual(emp_2.email, 'Sue.Meg@email.com')

    def test_fullname(self):
        emp_1 = Employee('Boris', 'St', 50000)
        emp_2 = Employee('Sue', 'Meg', 60000)

        self.assertEqual(emp_1.fullname, 'Boris St')
        self.assertEqual(emp_2.fullname, 'Sue Meg')

    def test_apply_raise(self):
        emp_1 = Employee('Boris', 'St', 50000)
        emp_2 = Employee('Sue', 'Meg', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setup Class')

    @classmethod
    def tearDownClass(cls) -> str:
        print('TearDown class')

    def setUp(self):
        self.emp_1 = Employee('Boris', 'St', 50000)
        self.emp_2 = Employee('Sue', 'Meg', 60000)

    def earDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Boris.St@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Meg@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Boris St')
        self.assertEqual(self.emp_2.fullname, 'Sue Meg')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

if __name__ == '__main__':
    unittest.main()
