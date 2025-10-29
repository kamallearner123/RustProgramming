from django.test import TestCase
from .models import Course

class CourseModelTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title="Introduction to Rust",
            description="A beginner's course on Rust programming.",
            duration=10
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Introduction to Rust")
        self.assertEqual(self.course.description, "A beginner's course on Rust programming.")
        self.assertEqual(self.course.duration, 10)

    def test_course_str(self):
        self.assertEqual(str(self.course), "Introduction to Rust")