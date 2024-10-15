#Max Holdaway Authorized

print("This is an information vault only authorized users can acess the information this will check if you are authorized.")

Admin = ["BananaPeach"]

Authorized = False

while True:
    action = input("""Are you an authorized user?
                   Type Authorization to check if you are authorized
                   Type Look to look at the information if you are authorized
                   Type Exit to exit the information vault\n """)
    
    if action in ["Authorization", "authorization"]:
        AskIfAuthorized = [input("Please type the name of your authorized account name: ")]
        if AskIfAuthorized in ["AppleBanana", "OrangeApple", "PineappleCoconut"]:
            print("Authorization successful welcome back to the vault")
            Authorized = True
        elif AskIfAuthorized in [Admin]:
            print("Welcome back admim")
            Authorized = True
        else:
            print("You are not authorized to view the information")
            Authorized = False
    
    elif action in ["Look", "look"]:
        if Authorized == True:
            print("Here is the information currently in the vault: BananaPeach is the admin and the vault is nothing more than a secret to keep that safe.")
        else:
            print("Not authorized try again.")

    elif action in ["exit"]:
        print("Thanks for using our vault see you later.")
        break

    else:
        print("Unexpected Error please try again")