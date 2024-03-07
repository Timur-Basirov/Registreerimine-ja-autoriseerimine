def Register(i:list,p:list)->any:
    """
    i=login
    p=parol
    
    """
    i=input("Create a Login:")
    p=input("Create a Password:")
    p2=input("Repeat your Password:")
    x=0
    while p2!=p:
        x+=1
        print("Looks like you forgot your password\nTry again:")
        p2=input("Repeat your Password:")
        if x==2:
            print("Your password confirmation attempts have ended")
            break
    l1=input("What do you like?\n(This word will be needed for account recovery)")
    print("Thanks for Creating your Account!")
    print("Welcome!",i+"!")
    return i,p,l1

def change(login):
    i=input("Enter new login: ")
    print("Login successfully changed.")
    return login

def password(password):
    p=input("Enter new password: ")
    print("Password successfully changed.")
    return password

def main():
    user="login"
    userpass="password"

    while True:
        print("1. Change Login\n2. Change Password\n3. Cancel")  
        choice=input("Choose action: ")       
        if choice=="1":
            user=change(user)
        elif choice=="2":
            userpass=password(userpass)
        elif choice=="3":
            break
        else:
            print("Please enter 1, 2, or 3")
    