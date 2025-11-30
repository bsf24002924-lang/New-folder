master_pwd = input("Enter the master password ")
def view():
     with open("passwords.txt","r")as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:", user, "| Password:",passw)

        
def add():
    name = input("Enter the account name: ")
    pwd = input("Enter the Password: ")
    with open("passwords.txt","a")as f:
        f.write(name + "|" + pwd + "\n")
while True:
    mode = input("Which mode you like to choose add new password or view the existing one or Quit now: add/view/Q: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue


