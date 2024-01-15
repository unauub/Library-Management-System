class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.available = True

  def display_info (self):
    print(f"Title: {self.title}\tAuthor: {self.author}\tAvailable: {'Yes' if self.available else 'No'}")

  def check_out(self):
    if self.available:
        self.available = False
        return True
    else:
        print("Sorry, the book is not available.")
        return False
  
  def check_in(self):
    self.available = True

class User:
  def __init__(self, name):
      self.name = name
      self.borrowed_books = []

  def display_info(self):
      print(f"User: {self.name}\tBorrowed Books: {', '.join(self.borrowed_books)}")

  def borrow_book(self, book):
      self.borrowed_books.append(book.title)

  def return_book(self, book):
      if book.title in self.borrowed_books:
          self.borrowed_books.remove(book.title)
          book.check_in()
          print("Book returned successfully.")
      else:
          print("You haven't borrowed this book.")


class Library:
  def __init__(self):
      self.books = []
      self.users = []

  def add_book(self, book):
      self.books.append(book)

  def register_user(self, user):
      self.users.append(user)

  def display_available_books(self):
      print("Available Books:")
      for book in self.books:
          if book.available:
              book.display_info()

  def borrow_book(self, user, book_title):
      for book in self.books:
          if book.title == book_title:
              if book.check_out():
                  user.borrow_book(book)
                  print("Book borrowed successfully.")
              else:
                  print("Book is not available for borrowing.")
              return
      print("Book not found.")

  def return_book(self, user, book_title):
      for book in self.books:
          if book.title == book_title:
              user.return_book(book)
              print("Book returned successfully.")
              return
      print("Book not found.")

def main():
  library = Library()

  # Adding books to the library
  book1 = Book("The Catcher in the Rye", "J.D. Salinger")
  book2 = Book("To Kill a Mockingbird", "Harper Lee")
  library.add_book(book1)
  library.add_book(book2)

  # Registering users
  user1 = User("Alice")
  user2 = User("Bob")
  library.register_user(user1)
  library.register_user(user2)

  while True:
      print("\n=== Library Management System ===")
      print("1. Display Available Books")
      print("2. Borrow a Book")
      print("3. Return a Book")
      print("4. Display User Information")
      print("5. Exit")

      choice = input("Enter your choice (1-5): ")

      if choice == '1':
          library.display_available_books()
      elif choice == '2':
          user_name = input("Enter your name: ")
          book_title = input("Enter the title of the book you want to borrow: ")
          user = next((u for u in library.users if u.name == user_name), None)
          if user:
              library.borrow_book(user, book_title)
          else:
              print("User not found.")
      elif choice == '3':
          user_name = input("Enter your name: ")
          book_title = input("Enter the title of the book you want to return: ")
          user = next((u for u in library.users if u.name == user_name), None)
          if user:
              library.return_book(user, book_title)
          else:
              print("User not found.")
      elif choice == '4':
          user_name = input("Enter your name: ")
          user = next((u for u in library.users if u.name == user_name), None)
          if user:
              user.display_info()
          else:
              print("User not found.")
      elif choice == '5':
          print("Exiting the Library Management System. Goodbye!")
          break
      else:
          print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
  main()