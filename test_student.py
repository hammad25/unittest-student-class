import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('John', 'Doe')
        self.assertEqual(student.full_name, 'John Doe')
    
    # test
    def test_alert_santa(self):
        student = Student('John', 'Doe')
        # method alret_santa
        student.alert_santa()

        self.assertTrue((student.naughty_list))

if __name__ == "__main__":
    unittest.main()