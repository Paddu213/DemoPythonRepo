from student import Student                   ##from file name ..import class name##
import unittest

class TestStudent(unittest.TestCase):
    def setUp(self):
        print("\nsetup")
    def tearDown(self):
        print("\nteardown")
    def test_email(self):
        print("Test email")
        self.objstu=Student("devandla","padmavathi",65)
        self.assertEqual(self.objstu.email,"devandla.padmavathi@gmail.com")
    def test_fullname(self):
        print("Test full name")
        self.objstu=Student("devandla","padmavathi",80)
        self.assertEqual(self.objstu.fullname,"devandla padmavathi")
        self.objstu.first="paddu"
        self.assertEqual(self.objstu.fullname,"paddu padmavathi")
    def test_apply_bonus(self):
        print("Test apply bonus")
        self.objstu = Student("devandla", "padmavathi", 70)
        self.assertEqual(self.objstu.marks,70,70)
        self.objstu.apply_bonus()
        self.assertEqual(self.objstu.marks,105)
        self.objstu.marks=65
        self.assertEqual(self.objstu.marks,65,65)
    def test_something(self):
        objstu = Student("devandla", "padmavathi", 65)
        self.assertEqual(objstu.somevalue,"")
        objstu.something("hi")
        self.assertEqual(objstu.somevalue,"devandla.padmavathi@gmail.comdevandla padmavathihi")




if __name__=="__main__":
    unittest.main()