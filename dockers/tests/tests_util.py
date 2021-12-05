from django.test import TestCase


class ExecuteCodeTestCase(TestCase):
    """
    python manage.py test docker.tests.tests_util
    """

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_code_execute(self):
        from io import StringIO
        import sys

        code_output = StringIO()
        code_error = StringIO()
        sys.stdout = code_output
        sys.stderr = code_error

        sample_code = "print('hello world')"
        exec(sample_code)

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        print(f"error: {code_error.getvalue()}")
        print(f"output: {code_output.getvalue()}")
