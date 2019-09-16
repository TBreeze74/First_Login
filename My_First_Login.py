import hashlib


def create():
    print("\n"+"Creating New Account: ")
    
    a=str(hash(input("Enter username: ")))
    b=str(hash(input("password: ")))
    
    with open('testtest.py','a+') as f:
        f.write(a)
        f.write(" ")
        f.write(b)
        f.write(" \n ")
        f.seek(0)
    print("Completed! \n")
    print("Now log in! \n")
    login();
    
#--------------------------------------------------------
    
def login():
    found=False
    a=str(hash(input("Enter username: ")))
    b=str(hash(input("Enter password: ")))
    
    with open('testtest.py','r+') as f:
        for line in f:
            if a in line:
                if b in line:
                    found = True
                    break
    
    if  found == True:
        print("Welcome!");
    else:
        create();
        
#--------------------------------------------------------
        
login();
