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
        self.new_credential = Credential("facebook", "kageni", "abcdefgh")
        
    def tearDown(self):
        '''
        cleans up after each testcase has run
        '''
        Credential.credentials_list = []
        
    def test_init(self):
        '''
        test proper initialization
        ''' 
        self.assertEqual(self.new_credential.account,"facebook")
        self.assertEqual(self.new_credential.userName,"kageni")
        self.assertEqual(self.new_credential.passWord,"abcdefgh")  
        
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
        test_credential = Credential("facebook", "kageni", "abcdefgh")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credentials_list),2)
        
    def test_delete_credential(self):
        '''
        test if we can remove a credential from our list
        '''  
        self.new_credential.save_credential()
        test_credential =  self.new_credential = Credential("facebook", "kageni", "abcdefgh")
        test_credential.save_credential()
        
        self.new_credential.delete_credential()
        
        self.assertEqual(len(Credential.credentials_list),1)
        
    def test_find_credential_by_account(self):
        '''
        test to check if we can get a credential by using the account
        '''
        self.new_credential.save_credential()
        test_credential = self.new_credential = Credential("facebook", "kageni", "abcdefgh")
        test_credential.save_credential()
        
        found_credential = Credential.find_by_account("facebook")
        
        self.assertEqual(found_credential.userName, test_credential.userName)
        
    
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''
        self.new_credential.save_credential()
        test_credential = Credential("facebook", "kageni", "abcdefgh")
        test_credential.save_credential()

        my_credential = Credential.find_credential("facebook")

        self.assertEqual(my_credential.account,test_credential.account)
        
    def test_display_credentials(self):
        '''
        method to return all saved credentials
        '''    
        self.assertEqual(Credential.display_credentials(), Credential.credentials_list)
        
    



        
if __name__ == '__main__':
    unittest.main()        
