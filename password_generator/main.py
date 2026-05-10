import random
import string

def password_generator(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ""
    
    for i in range(length):   
        password += random.choice(char)
    
    return password   

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = password_generator(length)
    print("Generated password:", password)

    