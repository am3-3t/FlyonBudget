#This file gets user credentital if the user is new and adds in the google sheet
#You will need a google sheet with first row: First Name, Last Name & Email in individual column.
import re, requests, os

class NewUser:

    def __init__(self) -> None:
        self.api = os.environ.get('SHEETY_API')
        self. header = {
            'Authorization': os.environ.get('SHEETY_HEADER')
            }
        self.get_post_url = f"https://api.sheety.co/{self.api}/newUser/newUser"
        self.response1 = requests.get(url=self.get_post_url, headers=self.header)
        self.data = self.response1.json()

    def is_valid_email(self,email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None
    
    def check_if_email_exists(self,email):
        if len(self.data['newUser']) != 0:
            for count in range(len(self.data['newUser'])):
                if self.data['newUser'][count]['email'] == email:
                    return True
                else:
                    return False
        else: 
            return False

    def get_user(self):
        first_name = (input("Enter your first name?\n")).title()
        last_name = (input('Enter your Last name?\n')).title()
        while True:
            email = input('Enter your Email\n')
            if self.is_valid_email(email=email):
                if self.check_if_email_exists(email) == False:
                    while True:
                        email2 =  input('Please enter your Email Again\n')
                        if email == email2:
                            print('Thank you for subscribing.')
                            add = {
                                "newUser": {
                                    'firstName': f'{first_name}',
                                    'lastName': f'{last_name}',
                                    'email': f'{email}'
                                }
                            }
                            response = requests.post(url=self.get_post_url,json=add, headers=self.header)
                            print(response.text)
                            break
                    break
                else: 
                    print('You are already subscribed!')
                    break
            else: 
                print('Invalid Email format')

