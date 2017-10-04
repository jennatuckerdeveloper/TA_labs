import unittest

from Python.inheritance import Student, Classroom, Course


class TestStudent(unittest.TestCase):
    def setUp(self):
        print(self._testMethodDoc)
        self.student0001 = Student("West", "Jane", "Enrolled, Full-Time", 0, "Paid In Full")
        self.student0002 = Student("Parker", "Sam", "Enrolled, Part-Time", 0, "Pending", "ADA")
        self.student0003 = Student("Vole", "Jennifer", "Hiatus", 0, "Hiatus")
        self.westhall = Classroom("Samstead", "189B", 2)
        self.foodjustice = Course("Interdisciplinary Studies", "Food Justice", 4, None, 4)
        self.foodjustice.room = self.westhall


    def test_add_course(self):
        self.assertEqual(self.student0001.add_course(self.foodjustice), "Course added to student schedule.")
        self.assertEqual(self.student0002.add_course(self.foodjustice), "Course added to student schedule.")
        self.assertEqual(self.student0003.add_course(self.foodjustice), "Course enrollment full.")

    # def test_hand(self):
    #     self.assertEqual(self.player.score_hand(), 21)
    #
    # def test_hand_hit(self):
    #     self.assertEqual(len(self.player.hand), 2)


if __name__ == '__main__':
    unittest.main()