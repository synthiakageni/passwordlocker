import unittest # Importing the unittest module
from user import User # Importing the user class
class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("kageni","kagenikageni") # create contact object
             
    def tearDown(self):
        '''
        cleans up after each testcase has run
        '''
        User.users_list = []
    def test_init(self):
            '''
            test init test case to test if the object is initialized properly
            '''    
            self.assertEqual(self.new_user.username,"kageni")
            self.assertEqual(self.new_user.password,"kagenikageni")
if __name__ == '__main__':
    unittest.main()    
              