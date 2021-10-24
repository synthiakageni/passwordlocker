import unittest 
from credential import Credential
import pyperclip
class TestCredential(unittest.TestCase):
    '''
    Test class that defines the test cases for the behaviour of the credential class
    '''
    def setUp(self):
        '''
        method to run before each test case 
        '''
        self.new_credential = Credential("Twitter", "kageni", "kagenikageni")
    def tearDown(self):
        '''
        cleans up after each testcase has run
        '''
        Credential.credentials_list = []
    def test_init(self):
        '''
        test proper initialization
        ''' 
        self.assertEqual(self.new_credential.account,"Twitter")
        self.assertEqual(self.new_credential.userName,"mumo")
        self.assertEqual(self.new_credential.passWord,"klmnopqrstuv")  
        
        