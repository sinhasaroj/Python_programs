# setUpClass(cls) and tearDownClass(cls) --- class methods---> used for running all the test cases and these 
# methods will run only once.

import unittest

class TestCase_Demo_Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f'set up class method excuted')

    def setUp(self):
        print('setUp method excuted')

    def test_1(self):
        print('Ran 1st test case ')


    def test_2(self):
        print('Ran 2nd test case')
        # print(10/0) -----> if we uncomment this the program 
        #                    excution won't stop but we will get the 
        #                    message as fail indicating the method name.


    def tearDown(self):
        print('tear down excuted')

    def test_3(self):
        print('Ran 3rd test case')

    def test_4(self):
        print('Ran 4th test case')

    @classmethod
    def tearDownClass(cls):
        print(f'Tear Down class method excuted')

unittest.main()