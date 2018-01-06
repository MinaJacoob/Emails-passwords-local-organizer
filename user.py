import base64
import os

class User:
    user_data = []

    def register(self, username, password):
        self.user_data.append(username)
        self.user_data.append(password)

    def save_data(self):
        try:
            f = open('user_data', 'w')
        except IOError:
            return False
        for word in self.user_data:
            f.write(self.encrypt_data(word) + '\n')
        del self.user_data[:] #delete all element in list
        f.close()
        return True

    def login(self,username,password):
        try:
            f = open('user_data', 'r')
        except IOError:
            return False
        data = f.readlines()
        data = [x.strip() for x in data]
        if self.encrypt_data(username) == data[0] and self.encrypt_data(password) == data[1]:
                return "valid"
        else:
                return "Invalid"
    def add_email(self,category,email,password):
        try:
            f = open('user_mails', 'a')
            os.chmod('user_mails',000)
        except IOError:
            return False
        data = category.strip()+'\t'+email.strip()+'\t'+password.strip()+'\n'
        f.write(data)
        f.close()
        return True

    def encrypt_data(self, str):
        return base64.b64encode(str)