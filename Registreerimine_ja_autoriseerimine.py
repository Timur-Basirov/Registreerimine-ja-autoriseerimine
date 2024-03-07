from module1 import *
i=[]
p=[]    
x=0
y=0
print("Welcome to the cmd virtual account system")
while True:
    print("\n1-Register\n2-Login")
    o=input("Choose action")
    if o=="1": 
        t=input("Do you want to create an account?").lower()
        if t=="yes":      
            i,p,l1=(Register(i,p))   
        elif t=="no":
            print("")
        else:
            print("Your answer doesnt meet the requirments\nPlease,next time use [yes] or [no] as an answer")
    elif o=="2":
        i1=input("Enter your Login")
        if i1==i:
            p1=input("Enter your Password")
            if p1==p:
                print("You succesfully entered your account")
            else:
                while p1!=p:
                    x+=1
                    print("Looks like you forgot your password\nTry again:")
                    p1=input("Repeat your Password:")
                    if x==2:
                        print("Your password confirmation attempts have ended")
                        break
        else:
            print("Login not found")
            
    elif o == "3":
        while True:
            print("1. Change Login\n2. Change Password\n3. Cancel")  
            choice=input("Choose action: ")       
            if choice=="1":
                user=change(user)
            elif choice=="2":
                userpass=password(userpass)
            elif choice=="3":
                break

            
