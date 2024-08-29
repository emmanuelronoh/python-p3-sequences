from sequences import print_fibonacci
import io
import sys
import pytest

class TestPrintFibonacci:
    '''Tests for the print_fibonacci() function'''

    def capture_output(self, func, *args):
        '''Helper function to capture the output of a function'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        try:
            func(*args)
        finally:
            sys.stdout = sys.__stdout__
        return captured_out.getvalue()

    def test_print_fibonacci_zero(self):
        '''Tests if the function prints an empty list when length = 0'''
        result = self.capture_output(print_fibonacci, 0)
        assert result == '[]\n'

    def test_print_fibonacci_one(self):
        '''Tests if the function prints [0] when length = 1'''
        result = self.capture_output(print_fibonacci, 1)
        assert result == '[0]\n'

    def test_print_fibonacci_two(self):
        '''Tests if the function prints [0, 1] when length = 2'''
        result = self.capture_output(print_fibonacci, 2)
        assert result == '[0, 1]\n'

    def test_print_fibonacci_ten(self):
        '''Tests if the function prints [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] when length = 10'''
        result = self.capture_output(print_fibonacci, 10)
        assert result == '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n'
