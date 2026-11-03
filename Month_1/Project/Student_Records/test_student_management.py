import unittest

from Month_1.Project.Student_Records.student_management import (
    add_student_record,
    calculate_average,
    find_student,
    letter_grade,
)


class StudentManagementTests(unittest.TestCase):
    def test_calculate_average(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90)

    def test_calculate_average_rejects_empty_scores(self):
        with self.assertRaises(ValueError):
            calculate_average([])

    def test_letter_grade_boundaries(self):
        expected = {
            90: "A",
            80: "B",
            70: "C",
            60: "D",
            59.9: "F",
        }
        for score, grade in expected.items():
            with self.subTest(score=score):
                self.assertEqual(letter_grade(score), grade)

    def test_add_student_record_strips_text_and_stores_scores(self):
        students = []
        student = add_student_record(students, " S1 ", " Ada ", [80, 90, 100])
        self.assertEqual(student["student_id"], "S1")
        self.assertEqual(student["name"], "Ada")
        self.assertEqual(student["scores"], [80, 90, 100])
        self.assertIs(students[0], student)

    def test_add_student_record_rejects_blank_fields(self):
        for student_id, name in [("", "Ada"), ("S1", "  ")]:
            with self.subTest(student_id=student_id, name=name):
                with self.assertRaises(ValueError):
                    add_student_record([], student_id, name, [80, 90, 100])

    def test_add_student_record_rejects_duplicate_id(self):
        students = []
        add_student_record(students, "S1", "Ada", [80, 90, 100])
        with self.assertRaises(ValueError):
            add_student_record(students, "S1", "Grace", [70, 80, 90])
        self.assertEqual(len(students), 1)

    def test_add_student_record_rejects_invalid_scores(self):
        for scores in ([80, 90], [80, 90, 101], [-1, 90, 100]):
            with self.subTest(scores=scores):
                with self.assertRaises(ValueError):
                    add_student_record([], "S1", "Ada", scores)

    def test_find_student(self):
        students = []
        add_student_record(students, "S1", "Ada", [80, 90, 100])
        self.assertEqual(find_student(students, "S1")["name"], "Ada")
        self.assertIsNone(find_student(students, "missing"))


if __name__ == "__main__":
    unittest.main()
