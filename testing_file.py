import unittest
from final import*
class Testing(unittest.TestCase):

    def test_case(self):
        login = Gui()
        result = login.login_user('11', '11')
        self.assertTrue(result)

    def test_case1(self):
        login = Gui()
        result = login.login_user('ram', '23')
        self.assertFalse(result)


    def test_case3(self):
        register = Gui()
        result = register.register_user('','ads','dsad','sad','da','a')
        self.assertFalse(result)

    def test_case4(self):
        register = Gui()
        result = register.register_user('sdf','ads','dsad','sad','da','d')
        self.assertTrue(result)

    def test_case5(self):
        ad_student = Student()
        result = ad_student.student_user('', '', '', '', '')
        self.assertFalse(result)

    def test_case6(self):
        ad_student = Student()
        result = ad_student.student_user('sd', 'sadw', 'wdqwdwd', 'dsads', 'cscsc')
        self.assertFalse(result)

    def test_case7(self):
        ad_student = Student()
        result = ad_student.student_delete('id')
        self.assertTrue(result)


    def test_case8(self):
        ad_student = Student()
        result = ad_student.student_delete('')
        self.assertFalse(result)

    def test_case9(self):
        ad_student = Student()
        result = ad_student.student_update('', '', '', '', '','')
        self.assertFalse(result)

    def test_case10(self):
        ad_student = Student()
        result = ad_student.student_update('sfsa', 'sda', 'cdscef', 'fdf', 'reeef','thth')
        self.assertFalse(result)

















