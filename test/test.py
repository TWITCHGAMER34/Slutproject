"""
Run all tests in the tests folder
"""
import unittest as ut


if __name__ == '__main__':
    testsuite = ut.TestLoader().discover('tests')
    ut.TextTestRunner(verbosity=2).run(testsuite)