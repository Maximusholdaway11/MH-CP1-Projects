#Max Holdaway Authorized

print("This is an information vault only authorized users can acess the information this will check if you are authorized. (The authorized users are AppleBanana, OrangeApple, and PineappleCoconut. The admin is BananaPeach)")

AuthorizedList = ["AppleBanana", "OrangeApple", "PineappleCoconut"]

Admin = ["BananaPeach"]

Authorized = False

while True:
    action = str(input("""Are you an authorized user?
                   Type Authorization to check if you are authorized
                   Type Look to look at the information if you are authorized
                   Type Exit to exit the information vault\n """))
    
    print("")

    if action in ["Authorization", "authorization"]:
        AskIfAuthorized = str(input("Please type the name of your authorized account name: "))

        if AskIfAuthorized in AuthorizedList:
            print("Authorization successful welcome back to the vault")
            Authorized = True
            print("")
        elif AskIfAuthorized in Admin:
            print("Welcome back admin")
            Authorized = True
            print("")
        else:
            print("You are not authorized to view the information")
            Authorized = False
            print("")
    
    elif action in ["Look", "look"]:
        if Authorized == True:
            print("Here is the information currently in the vault: BananaPeach is the admin and the vault is nothing more than a secret to keep that safe.")
            print("")
        else:
            print("Not authorized please use our authorization system or you will not be able to see the information. (You also can't see it if you are not authorized)")
            print("")

    elif action in ["exit"]:
        print("Thanks for using our vault see you later.")
        break

    else:
        print("Unexpected Error please try again")
        print("")