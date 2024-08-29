from sequences import print_fibonacci
import io
import sys
import pytest

class TestPrintFibonacci:
    '''function print_fibonacci()'''

    def test_print_fibonacci_zero(self):
        '''prints empty list when length = 0'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(0)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[]\n'

    def test_print_fibonacci_one(self):
        '''prints 0 when length = 1'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(1)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0]\n'

    def test_print_fibonacci_two(self):
        '''prints 0, 1 when length = 2'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(2)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1]\n'

    def test_print_fibonacci_ten(self):
        '''prints 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 when length = 10'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        print_fibonacci(10)
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n'
