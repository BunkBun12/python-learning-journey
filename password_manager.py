print("==== Password Manager ====")

password_manager = {}


def add_password():
  choices = int(input("enter the nunmber of pass to save -Max'5 :"))

  if choices <= 5:
    for choice in range(choices):
      website = input("enter the website :")
      password = input("enter the password")
          
      password_manager[website] = password

  else :
    print("upgrade to premium!")
    
    


def view_passwords():
    print(f"{password_manager}")

def update_password():
  choice = input("enter the website to change the password:")

  if choice in password_manager:
    newpassword = input("enter the new password to update")

    password_manager[choice] = newpassword
    print("password updated!")

  else :
    print("Website not found!")

def search_password():

  search = input("enter the webiste to search :")

  if search in password_manager:
    print(password_manager[search])

  else :
    print("website not found!")

def delete_password():
  choice = input("enter which password to delete :")

  if choice in password_manager:
    del password_manager[choice]
    print("password delete!")

  else :
    print("password not found!")



choice = None

while choice != 6:
  print("""
1.Add Password
2.View Passwords
3.Search Passwords
4.Update Password
5.Delete Password
6.Exit""")

  choice = int(input("enter a option to access (1 - 6):"))
  match choice:
    case 1:
      add_password()

    case 2:
      view_passwords()

    case 3:
      search_password()

    case 4:
      update_password()

    case 5:
      delete_password()

    case 6:
      print("Exiting ....")

    case _:
      print("invalid option!")
    

    
  
  

