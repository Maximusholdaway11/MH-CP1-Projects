#Max Holdaway What are these numbers?

print("This is a number formater.")

print("")

while True:
    action = input(""" Which of these do you want to do?
                    To Give a number commas for the thousands, type: Comma
                    To make a number a float with 4 decimal places, type: Four
                    To turn a number into a percentage, type: Percent
                    To turn a number into its dollar form, type: Dollar
                    If you want to do all of them at once, type: All
                    Type Exit to exit the number formater\n""")
    if action in ["Comma", "comma"]:
        CommaNumber = float(input("Please give me a number to add thousandth place commas to: "))
        CommaString = "Here is your commafied number {:,}"
        print(CommaString.format(CommaNumber))
        print("")

    elif action in ["Four", "four"]:
        FourDeciNumber = float(input("Please give me a number to turn into a float with 4 decimal places: "))
        FourDeciString = "This is your DeciFormatted number {DeciNumber:.4f}"
        print(FourDeciString.format(DeciNumber = FourDeciNumber))
        print("")

    elif action in ["Percent", "percent"]:
        PercentNumber = float(input("Please give me a number to convert into a percentage: "))
        PercentString = "This is your Percentified number {:%}"
        print(PercentString.format(PercentNumber))
        print("")

    elif action in ["Dollar", "dollar"]:
        DollarNumber = float(input("Please give me the number to convert to dollar form: "))
        DollarString = "This is your dollarified number ${Dollar:.2f}"
        print(DollarString.format(Dollar = DollarNumber))
        print("")

    elif action in ["All", "all"]:
        AllNumber = float(input("Please give me a number to do all the specific tasks to: "))

        print("")

        CommaString = "Here is your commafied number {:,}"
        print(CommaString.format(AllNumber))

        print("")

        FourDeciString = "This is your DeciFormatted number {DeciNumber:.4f}"
        print(FourDeciString.format(DeciNumber = AllNumber))

        print("")

        PercentString = "This is your Percentified number {:%}"
        print(PercentString.format(AllNumber))

        print("")

        DollarString = "This is your dollarified number ${Dollar:.2f}"
        print(DollarString.format(Dollar = AllNumber))

        print("")

    else:
        print("Unexpected Error try again")