from credential import Credential
from user import User
def create_new_user(username, password):
    '''
    Function that creates a user
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    function to save user
    '''
    user.save_user()
    
def del_user(user):
    '''
    Function that deletes a user
    '''  
    user.delete_user()
    
def user_login(username, password):
    '''
    check user authentication
    '''  
    authentic_user =  User.authenticate_user(username, password)
    return authentic_user

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()
    
def delete_credential(credential):
    '''
    Function to delete credential
    '''    
    credential.delete_credential()
    
def find_a_credential(account):  
      '''
      Function that searches for credentials
      '''
      return Credential.find_by_account(account)

def check_credential_existence(account):
    '''
    Function that checks the existence of a credential
    '''
    return Credential.find_credential(account)

def display_my_credentials():
    '''
    Function to display my credentials
    '''
    return Credential.display_credentials()

def generate_password():
    '''
    generates random passwords
    '''
    get_password = User.gen_password(8)
    return get_password
    
    

def main():
    password = None
    print("Hi.. Welcome to Password Locker  your modern passwords store! What is your name? ")
    name = input()
    
    print('\n')
    
    while True:
                    print(f"Hello { name},\n Use the following short codes to perform your operation:\n CA - create a new user account, \n LG - login to your user account  ")
                    
                    short_code = input("").lower().strip()
                    
                    if short_code == "ca":
                        print("Create An Account")
                        print('*' * 50)
                        username = input("Username: ")
                        while True:
                            print(" \n TP - To input your own password: \n  GP - To get an autogenerated random password")
                            my_choice = input().lower().strip()
                            if my_choice == 'tp':
                                password = input("Enter Password\n")
                                break
                            elif my_choice == 'gp':
                                password =  generate_password()
                                break
                            else:
                                    print("We are sorry, that was an invalid choice, Try Again!") 
                        save_user((create_new_user(username,password)))
                        print("*"*85)
                        print(f"Hello {name} , Your Account has been created successfully. Your password is: {password}")
                        print("*"*85)
                        
                    elif short_code == "lg":  
                        print("*"*50)
                        print("Enter your username and password to login")
                        print("*"*50)
                        username = input("Username: ")
                        password = input("password: ")
                        login = user_login(username, password)
                        if user_login == login:
                            print(f"Hello {username}.Welcome To PassWord Locker Manager")
                            print('\n')
                            
                    while True: 
                         print("Use these shortcodes:\n CC - Create a new credential \n DC - Display Credentials  \n FC - Find a credential  \n  GP - Generate a random password  \n D-Delete  credential \n EX - Exit the application")  
                         
                         short_code = input().lower().strip() 
                         if short_code == "cc":
                             print("Create New Credential")
                             print("."*20)
                             print("Account Name: ")  
                             account = input().lower()
                             print("Your account username")
                             username = input()
                             while True:
                                 print(" \n TP - To input your own password: \n  GP - To get an autogenerated random password")
                                 the_choice = input().lower().strip()
                                 if the_choice == 'tp':
                                     password = input("Enter Your password\n")
                                     break
                                 elif the_choice == 'gp':
                                     password = generate_password()
                                 else:
                                     print("Invalid entry, try again")      
                             save_user((create_new_user(username,password)))
                             print('\n')
                             print(f"Account Credential for: {account} - UserName: {username} - Password:{password} created succesfully")
                             print('\n')
                         elif short_code == "dc":
                             if display_my_credentials():
                                 print("Here is your list of accounts: ")
                                 
                                 print("*"* 30)
                                 print('_'*30)
                                 for account in display_my_credentials():
                                        print(f"Account:{account.account} \n Username:{username}\n Password:{password}")
                                        print('_'* 30)
                                 print('*' * 30)   
                             else:
                                 print("You don't have any credentials saved yet..........")
                         elif short_code == "fc":
                             print("Enter the Account name you want to search for  ")  
                             search_name = input().lower()
                             if find_a_credential(search_name):
                                   search_credential = find_a_credential(search_name) 
                                   print(f"Account  : {search_credential.account}")
                                   print('-' * 50)
                                   print(f"Username: {search_credential.username} Password :{search_credential.password}")
                                   print('-' * 50)
                             else:
                                  print("That Credential does not exist")
                                  print('\n')   
                         elif short_code == "d":
                             print("Enter the account name of the Credentials you want to delete")
                             cred_name = input().lower()
                             if find_a_credential(cred_name):
                                 search_cred = find_a_credential(cred_name)
                                 print("_"*50)
                                 search_cred.delete_credential()
                                 print('\n')
                                 print(f"Your stored credentials for : {search_cred.account} successfully deleted!!!")
                                 print('\n')
                             else:
                                 print("That Credential you want to delete does not exist in your store yet")    
                         elif short_code == 'gp':
                             
                             password = generate_password()  
                             print(f" {password} Has been generated succesfull. You can proceed to use it to your account")  
                         elif short_code == 'ex':
                             print("Thanks for using passwords store manager.. See you next time!")
                             break  
                         else:
                             print("Wrong entry... Check your entry again and let it match those in the menu")
                    else:
                        print("Please enter a valid input to continue")    
if __name__ == '__main__':
    main()                                   