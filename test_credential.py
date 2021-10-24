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
        self.assertEqual(self.new_credential.userName,"kageni")
        self.assertEqual(self.new_credential.passWord,"kagenikageni") 
    def test_save_credential(self):
        '''
        method to test whether new instances are being saved 
        '''   
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),1)
    def test_save_multiple_credential(self):
        '''
        test case for checking the ability to save multiple credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "mumo", "klmnopqrstuv")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
        
        
        