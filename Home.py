import os
import json
from tabulate import tabulate

users_file = r"D:\\Library Managment System\\users.json"
book_file = r"D:\\Library Managment System\\books.json"

class JSONHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r') as f:
                    return json.load(f)
        except json.JSONDecodeError:
            print(f"Error: {self.file_path} contains invalid JSON!")
        return []

    def write(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

class User:
    def __init__(self, user_id, user_name, password, is_active=1):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.status = is_active

    def login(self, login_user_name, login_password):
        db = JSONHandler(users_file)
        users = db.read()
        for user in users:
            if login_user_name.lower() == user['user_name'] and login_password.lower() == user['password']:
                print("Login successfully ......")
                return True
        return "Login information wrong"

    def logout(self):
        print(f"User {self.user_name} logged out.")

class Manager(User):
    def __init__(self, user_name, password, is_active=1):
        super().__init__(None, user_name, password, is_active)
        self.db = JSONHandler(users_file)

    def add_user(self):
        users = self.db.read()
        self.user_id = users[-1]["user_id"] + 1 if users else 1

        new_user = {
            "user_id": self.user_id,
            "user_name": self.user_name.lower(),
            "password": self.password,
            "status": "active" if self.status == 1 else "disactive"
        }

        users.append(new_user)
        self.db.write(users)
        print(f"User {self.user_name} added successfully.")

    def remove_user(self, input_user_id):
        users = self.db.read()
        updated_users = [user for user in users if user['user_id'] != input_user_id]

        if len(updated_users) == len(users):
            print(f"No user found with ID {input_user_id}")
        else:
            self.db.write(updated_users)
            print(f"User ID {input_user_id} removed successfully.")

    def set_state(self, input_user_id, state):
        users = self.db.read()
        user_found = False
        for user in users:
            if user['user_id'] == input_user_id:
                user_found = True
                user['status'] = 'active' if state == 1 else 'disactive'
                user_name = user['user_name']
                break
        if user_found:
            self.db.write(users)
            print(f"{user_name} status updated successfully.")
        else:
            print("No user found with this ID!")

    def display_accounts(self):
        users = self.db.read()
        table = [[u["user_id"], u["user_name"], u["status"]] for u in users]
        headers = ["User ID", "Username", "Status"]
        print(tabulate(table, headers, tablefmt="grid"))

class Librarian(User):
    def __init__(self, user_id, user_name, password, is_active=1):
        super().__init__(user_id, user_name, password, is_active)
        self.db = JSONHandler(book_file)

    def add_book(self, title, author, status):
        books = self.db.read()
        book_id = books[-1]['book_id'] + 1 if books else 1

        new_book = {
            "book_id": book_id,
            "title": title.lower(),
            "author": author,
            "status": "Available" if status == 1 else "Borrowed"
        }

        books.append(new_book)
        self.db.write(books)
        return f"Book '{new_book['title']}' added successfully!"

    def list_books(self):
        books = self.db.read()
        table = [[b["book_id"], b["title"], b["author"], b["status"]] for b in books]
        headers = ["Book ID", "Title", "Author", "Status"]
        print(tabulate(table, headers, tablefmt="grid"))
        return books

    def update_books(self):
        books = self.list_books()
        if not books:
            print("No books to update.")
            return

        while True:
            try:
                book_id = int(input("Enter the book ID to update: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        found = False
        for book in books:
            if book['book_id'] == book_id:
                book["title"] = input("Enter new book title: ")
                book["author"] = input("Enter new author: ")

                while True:
                    state = input("Enter book state (1=Available, 0=Borrowed): ")
                    if state in ("0", "1"):
                        book["status"] = "Available" if state == "1" else "Borrowed"
                        break
                    print("Invalid input! Only 1 or 0 allowed.")

                self.db.write(books)
                print("Book updated successfully!")
                found = True
                break

        if not found:
            print("Book ID not found.")

    def delete_books(self):
        pass

    def search_books(self):
        pass

    def books_state(self):
        pass
  
b1 = Librarian(1, "khalid", "1234", 1)
# print(b1.add_book("poor mom" , "ahmos" , 1))

print(b1.update_books())
