# There are two types of testing...
# Unit test - The process of testing whether a particular unit is working properly or not is called Unit test.
# Integration test - end to end testing (total application testing) called integration testing. 


# How to perform unit test in Python

# module test : unittest
# class name : TestCase
# instance methods : 3 methods---> 1. setUp() 2. test() 3. tearDown() 

import unittest

class TestCase_Demo_Test(unittest.TestCase):
    def setUp(self):
        print('setUp method excuted')

    def test_1(self):
        print('test method excuted')


    def test_2(self):
        print('Ran 2 test case')


    def tearDown(self):
        print('tear down excuted')

unittest.main()

