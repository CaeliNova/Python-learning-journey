username =["John","Alenere","David"]
password = ["abc123","123abc","hahatdog"]

usernameInput = input("Enter your username: ")
passwordInput = input("Enter your password: ")

for i in range(len(username)):
    if usernameInput == username[i] and passwordInput == password[i]:
            print("Welcome " + usernameInput)
            break
else:
            print("Account Not Found")
