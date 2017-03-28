import server
import unittest

class ServerTestAnyname(unittest.TestCase):

    def setUp(self):
        #this name has to be setup
        #each time the test run, any one of them this will run with it.

        # sample test variable
        self.melon =

        #Data base connection open so that you can test  
        

    def test_methodNameCanBeAnyting(self):
        # the name has to start with "test" d
        self.assertEqual(function_that_tests(variable_from_setUp), result_value)
        # check list of the methods that you can use "assert something"


    def tearDown()
    # runs after each test
    # DB closed so that you can test  

if __name__ == '__main__':

    # This runs all of or tests
    unittest.main()

#when wanted, run the test file to check everhting
#import pdb; pdb.set_trace() # once in the terminal there are PDB commands
#