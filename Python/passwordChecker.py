"""
To check the password strength.
    1-Should have integers 
    2-Capital and lower case
    3-Atleast one special symbol 
"""
def passInput():
    passKey = input("Enter your password: ")
    return passKey

def lenCheck(passKey):
    if passKey>=8:
        return True
    else:
        return False

def charCheck(passKey):
    upperCase = 0
    lowerCase = 0
    number = 0
    for i in passKey:
        if(i.is)
            if i.isupper():
            upperCase+=1 
        

def passChecker():
    passKey = passInput()
    
    if lenCheck(passKey) and charCheck(passKey):
        print("Password passes")
    else :
        print("Make a stronger password")