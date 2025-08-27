import os
import json

file_name = r"D:\\Library Managment System\\users.json"

class User: 
    def __init__(self , user_id , user_name , password , is_active = 1):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.status = is_active
        
        
    def login(self , login_user_name , login_password):
        user_name = self.user_name
        password = self.password
        
        if os.path.exists(file_name):        
            with open(file_name , 'r') as file:
                users = json.load(file)
                for user in users:
                    if login_user_name.lower() == user['user_name'] and login_password.lower() == user['password']:
                        print("Login seccfully ......")
                        return True
                        
            return "Login informations wrong"
        else:
            print("The Database File hasn't made")

    def add_user(self):
        if os.path.exists(file_name):
            with open(file_name , 'r') as file:
                users = json.load(file)
        else:
            with open(file_name , 'w'):
                users = []

        if users:
            last_id = users[-1]["user_id"]
            self.user_id = last_id + 1
        else:
            self.user_id = 1
        
        new_user = {
        "user_id" : self.user_id,
        "user_name" : self.user_name.lower(),  # convert username to lowercase
        "password" : self.password,
        "status": "active" if self.status == 1 else "disactive"
        }

        
        users.append(new_user)
        
        with open(file_name , 'w') as file:
            json.dump(users , file , indent=4)
            print(f"User {self.user_name.lower()} added successfully.")
            
class Manager(User):
    def __init__(self, user_name, password, is_active):
        super().__init__(None, user_name, password, is_active )
        

            
m1 = User(None,"sPaRk" , "1234" , 1)
m1.add_user()
# print(m1.login("Khalid" , "1234"))