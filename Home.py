import os
import json
from tabulate import tabulate

users_file = r"D:\\Library Managment System\\users.json"
book_file = r"D:\\Library Managment System\\books.json"

class User: 
    def __init__(self , user_id , user_name , password , is_active = 1):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.status = is_active
        
        
    def login(self , login_user_name , login_password):
        user_name = self.user_name
        password = self.password
        
        if os.path.exists(users_file):        
            with open(users_file , 'r') as file:
                users = json.load(file)
                for user in users:
                    if login_user_name.lower() == user['user_name'] and login_password.lower() == user['password']:
                        print("Login seccfully ......")
                        return True
                        
            return "Login informations wrong"
        else:
            print("The Database File hasn't made")

            
            
    def logout():
        return 
            
class Manager(User):
    def __init__(self, user_name, password, is_active):
        super().__init__(None, user_name, password, is_active )
        
    def add_user(self):
        if os.path.exists(users_file):
            with open(users_file , 'r') as file:
                users = json.load(file)
        else:
            with open(users_file , 'w'):
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
        
        with open(users_file , 'w') as file:
            json.dump(users , file , indent=4)
            print(f"User {self.user_name.lower()} added successfully.")
    
    def remove_user(self, input_user_id):
        if os.path.exists(users_file):
            with open(users_file, 'r') as file:
                users = json.load(file)

            user_to_delete = None
            for user in users:
                if user['user_id'] == input_user_id:
                    user_to_delete = user
                    break

            if user_to_delete:
                updated_users = [user for user in users if user['user_id'] != input_user_id]

                with open(users_file, 'w') as file:
                    json.dump(updated_users, file, indent=4)

                print(f"User '{user_to_delete['user_name']}' has been deleted successfully.")
            else:
                print(f"No user found with ID {input_user_id}")
        else:
            print("The Database File hasn't been created yet.")
    
    def set_state(self,input_user_id ,state):
        if os.path.exists(users_file):
            with open(users_file, 'r') as file:
                users = json.load(file)
            user_found = False
            for user in users:
                if user['user_id'] == input_user_id:
                    user_found = True
                    user['status'] = 'active' if state == 1 else 'disactive'
                    current_state = user['status'] 
                    user_name = user['user_name']
                    break
                
            if user_found:
                with open(users_file, 'w') as file:
                    json.dump(users , file , indent = 4)
                    return f"{user_name} status has been changed to {current_state} successfully."     
            else:
                return "No user found in this ID!"    
        else:
           "NO database has been found!"               
                    
    def display_accounts(self):
        if os.path.exists(users_file):
            with open(users_file, 'r') as file:
                users = json.load(file)
            table = [[u["user_id"], u["user_name"],  u["status"]] for u in users]
        headers = ["User ID", "Username", "Status"]

        print(tabulate(table, headers, tablefmt="grid"))    
                
class Librarian(User):
    def __init__(self, user_id, user_name, password, is_active=1):
        super().__init__(user_id, user_name, password, is_active )
        # self.emp_id = emp_id
        
    def add_book(self, title, author, status):
        if os.path.exists(book_file):
            with open(book_file, 'r') as file:
                books = json.load(file)
        else:
            books = []

        # Auto-increment book_id
        if books:
            last_id = books[-1]["book_id"]
            book_id = last_id + 1
        else:
            book_id = 1

        new_book = {
            "book_id": book_id,
            "title": title.lower(),
            "author": author,
            "status": "Available" if status == 1 else "Borrowed"
        }

        # ✅ Add the new book to the list
        books.append(new_book)

        # ✅ Save updated list back to file
        with open(book_file, 'w') as file:
            json.dump(books, file, indent=4)

        return f"Book '{new_book['title']}' has been added successfully!"

                
    def update_books():
        pass
    def delete_books():
        pass
    def search_books():
        pass
    def books_state():
        pass
    
b1 = Librarian(1, "khalid", "1234", 1)
print(b1.add_book("Poor Dad", "Ahmed Ali", 1))

