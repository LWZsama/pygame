def check(a):
    if len(a) < 6 or len(a) > 8:
        return False
    else:
        return True

def getPWD(attempt):
    if attempt == 1:
        pwd = str(input("enter your pwd\n"))
        while check(pwd) == False:
            print("error, pwd must be 6-8 characters long\nenter your pwd again")
            pwd = str(input())
        print("pwd changed successfully")
    if attempt == 2:
        pwd_1 = str(input("enter your pwd\n"))
        while check(pwd_1) == False:
            print("error, pwd must be 6-8 characters long")
            pwd_1 = str(input("enter your pwd again\n"))
        pwd_2 = str(input("enter your pwd again\n"))
        while pwd_2 != pwd_1:
            print("error, pwd does not match")
            pwd_2 = str(input("enter your pwd again\n·"))
        print("pwd changed successfully")
        
getPWD(2)

