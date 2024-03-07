from module1 import *
i=[]
p=[]    
x=0
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
            p1=("Enter your Password")
            if p1==p:
                print("You succesfully entered your account")
            else:
                while p1==p:
                    print("Looks like you forgot your password\nTry again:")
                    p1=input("Repeat your Password:")
                    if x==2:
                        print("Your password confirmation attempts have ended")
                        break
