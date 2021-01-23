''' This is a simple Random password generator, it can always come handy while making an account 
    Entering the number of the password
    And get your unique strong alphanumeric password'''
import random
passlen = int(input("Enter the length of password :  "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?0123456789"
p = "".join(random.sample(s, passlen))
print(p)
