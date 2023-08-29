import os, requests, smtplib

class Subscribers:

    def __init__(self) -> None:
        self.api = os.environ.get('SHEETY_API')
        self.header = {
            'Authorization': os.environ.get('SHEETY_HEADER')
        }
        self.end_point = f"https://api.sheety.co/{self.api}/newUser/newUser"
        self.response = requests.get(url=self.end_point, headers=self.header)
        self.data = self.response.json()
        self.email = os.environ.get('MY_EMAIL')
        self.passw = os.environ.get('MY_PASS')
    
    def check_subs(self):
        if len(self.data['newUser']) == 0:
            return True
        else:
            return False
        
    def send_email(self, message):
        for items in range(len(self.data['newUser'])):
            email = self.data['newUser'][items]['email']
            with smtplib.SMTP('smtp.gmail.com',port=587) as connection: 
                connection.starttls()
                connection.login(user=self.email, password=self.passw)
                connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=('Subject: Flight Alert\n' + '\n').join([''] + message.split('\n')).encode('utf-8')
                    )