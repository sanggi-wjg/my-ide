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

        codeOut = StringIO()
        codeErr = StringIO()
        sys.stdout = codeOut
        sys.stderr = codeErr

        sample_code = "print('hello world')"
        exec(sample_code)

        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        print(f"error: {codeErr.getvalue()}")
        print(f"output: {codeOut.getvalue()}")
