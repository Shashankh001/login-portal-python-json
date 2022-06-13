import json

while True:
    x = input("Do you want to sign in or log in?\nEnter 'sign' to sign in and 'login' to log in: ")#determining wether to login or sign in
    print("")

    if x == 'sign':
        #giving details
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        re_password = input("Re-Enter your password: ")
        print("")

        #checking if both passwords are the same
        if password != re_password:
            print("Whoops! The passwords dont match. Try Again.\n")
            continue
        
        #reading the json file
        with open('logger.json','r') as f:
            data = json.load(f)

        new_user_data = {"username":username,"password":password}
        data.append(new_user_data) #appending the json file with new user data

        with open('logger.json','w') as f:
            json.dump(data, f, indent = 4) #dumping the new user data

        print("Congratulations! You have now created an account! You can now login.\n")

    if x == 'login':
        print("Welcome!! Please enter your username and password to login.\n")

        #taking credentials
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("")

        #reading the json file
        with open('logger.json','r') as f:
            data = json.load(f)

        index = None
        
        #performing a log check
        for i in range(0, len(data)):
            if username == data[i]["username"] and password == data[i]["password"]:
                print(f"Welcome back {username}!")
                index = i
                quit()

        
        if index == None:
            print("Uh oh, Invalid login, try again.\n")
            continue
        
