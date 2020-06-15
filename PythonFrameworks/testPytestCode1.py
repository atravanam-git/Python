"""
# PyTest be default executes all file names of format test_*.py or *_test.py in the current module or directory
# if a specified filename is NOT mentioned.
# PyTest will pick only those test function names of format test*.
# In the output 'F' represents a test failure and dot(.) represents a test success.

# PyTest Execution Modes:
# 1. pytest -k <substring> -v
    ==> all the tests matching the substring will be picked for execution
# 2.pytest -m <markername>
    ==> -m <markername> represents the marker name of the tests to be executed.
    ==> <markername> can be user defined or predefined name"""
from math import sqrt
import pytest


@pytest.yield_fixture()
def setup():
    print("Setup method executes before every test method")
    yield
    print("prints after every test method")


@pytest.mark.sqr
def testSqrt():
    num = 25
    assert math.sqrt(num) == 625


@pytest.mark.sqr
def testAreaofSquare():
    side = 4
    assert math.sqrt(side) == 16


@pytest.mark.others
def testAreaofCircle():
    radius = 5
    assert (22 / 7 * (radius * radius))=30
