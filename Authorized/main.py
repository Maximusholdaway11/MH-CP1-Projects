#Max Holdaway Authorized

print("This is an information vault only authorized users can acess the information this will check if you are authorized.")

AuthorizedList = ["AppleBanana", "OrangeApple", "PineappleCoconut"]

Admin = ["BananaPeach"]

Authorized = False

while True:
    action = input("""Are you an authorized user?
                   Type 1 to check if you are authorized
                   Type 2 to look at the information if you are authorized
                   Type 3 to exit the information vault\n """)
    
    if action == 1:
        AskIfAuthorized = [input("Please type the name of your authorized account name: ")]
        if AskIfAuthorized in AuthorizedList:
            print("Authorization successful welcome back to the vault")
            Authorized = True
        elif AskIfAuthorized in Admin:
            print("Welcome back admim")
            Authorized = True
        else:
            print("You are not authorized to view the information")
            Authorized = False
    
    if action == 2:
        if Authorized == True:
            print("Here is the information currently in the vault: BananaPeach is the admin and the vault is nothing more than a secret to keep that safe.")
        else:
            print("Not authorized try again.")

    if action == 3:
        print("Thanks for using our vault see you later.")
        break