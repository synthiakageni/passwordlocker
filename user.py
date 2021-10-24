import random
import string

class User:
    """
    Class that generates new instances of contacts.
    """
users_list = []  # Empty contact list

def __init__(self, username, password):

      # docstring removed for simplicity

        self.username = username
        self.password = password
def save_user(self):
        '''
        method that saves a new instance of a user into the list
        '''
        User.users_list.append(self)
def delete_user(self):
        '''
        method for deleting a saved user from the users list
        '''
        User.users_list.remove(self)    