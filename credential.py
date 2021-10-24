import pyperclip
from user import User
class Credential:
    '''
    the blueprint for creating new objects for credentials
    '''
    credentials_list = []
    @classmethod
    def authenticate_user(cls, username, password):
        '''
        classmethod
        check whether the user is in our list
        '''
        firstuser = ""
        for user in User.users_list:
            if (user.username == username and user.password == password):
                firstuser == user.username
        return firstuser
    def __init__(self, account, userName, passWord):
        '''
        method that initializes the credentials to be stored
        '''
        self.account = account
        self.userName = userName
        self.passWord = passWord
    def save_credential(self):
        '''
        method to save credentials
        '''
        Credential.credentials_list.append(self)