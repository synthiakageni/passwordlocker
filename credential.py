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