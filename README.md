# login-portal-python-json

A small simple program using python with json to demonstrate a login portal where you can sign in and log in.

Let us break down the python code and understand it better.

`main.py`

For communication with the `json` file, we will be using a pre-installed module from python called json and import it as follows:
```py
import json
```

Since we want to let the user decide wether he wants to login or sign in, lets run our code in an infinite loop with 2 `if` statements.
```
while True:
    x = input("Do you want to sign in or log in?(login/sign): ")#determining wether to login or sign in
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
```

Now that our code is finished, let us have a look at our output:

#Output
```
Do you want to sign in or log in?(login/sign): 
```

Lets try creating an account and use the `sign` feature and answering the required questions.
```
Enter a username: Shashankh001
Enter a password: Password345
Re-Enter your password: Password345

Congratulations! You have now created an account! You can now login.
```
Perfect! We have now created our own account. To verify this, lets open our `logger.json` file and notice the changes.

Your json file should look something like this:
```
[
    {
        "username": "Shashankh001",
        "password": "Password345"
    }
]
```

How about we try and login to this account?

Instead of the `sign` feature lets use the `login` feature with our previously generated account credentials.
```
Do you want to sign in or log in?(login/sign): login

Welcome!! Please enter your username and password to login.

Enter your username: Shashankh001
Enter your password: Password345

Welcome back Shashankh001!
```
