#Login system: 

valid_username="Hooria" #sets a username
valid_password="htk123" #sets a password 

username=input("Enter a username: ") #asks user to input username
password=input("Enter a password: ") #asks user to input password

if username==valid_username and password==valid_password: #checks if the username and password matches the valid username and password
    print("Login Successful")
else: 
    print("Access Denied")
