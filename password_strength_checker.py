import re

def check_password_strength(password):
    # Check no. of characters (at least 8 characters)
    if len(password) < 8:
        return "Password should be at least 8 characters long. Try again."
    
    # Check for at least one uppercase letter(A-Z)
    if not re.search(r'[A B C D E F G H I J K L M N O P Q R S T U V W X Y Z]', password):
        return "Password should contain at least one uppercase letter. Try again."
    
    # Check for at least one lowercase letter(a-z)
    if not re.search(r'[a b c d e f g h i j k l m n o p q r s t u v w x y z]', password):
        return "Password should contain at least one lowercase letter. Try again."
    
    # Check for at least one digit(0-9)
    if not re.search(r'[0-9]', password):
        return "Password should contain at least one digit. Try again with a number(0-9)."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special character. Try again with any special character."
    
    # If all conditions are met
    return "Password is strong!"

# Loop until the password is strong
while True:
    password = input("Enter a password: ")
    result = check_password_strength(password)
    print(result)
    
    # If password is strong, break the loop
    if result == "Password is strong!":
        break


#Loop for confirming the password
while True:
    confirmed_password = input("Enter your password to confirm: ")
    
    #Comparing the entered password with the real password
    if confirmed_password != password:
        print("Sorry! This is not your password. Try again.")
    else:
        print("Your password is confirmed successfully.")
        break
        
