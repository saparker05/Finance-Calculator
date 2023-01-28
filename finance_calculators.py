# This program consists of two different financial calcualtors.
# The user can select from an investment calcualator and a home loan repayment calculator. 

import math 


user_choice = input('''\nChoose either 'investment' or 'bond' from the menu below to proceed:\n
investment    -      to calculate the amount of interest you'll earn on your investment
bond          -      to calculate the amount you'll have to pay on a home loan\n\n''')


# First check if the user has correctly selected an option and if not return an error. 
if user_choice.lower() != "investment" and user_choice.lower() != "bond":
    print("\nError: selection has not been made correctly. Please try again.\n")

else:

    # The next section of code is the investment calculator. This runs if the user selects investment from the start menu. 
    if user_choice.lower() == "investment":

        money_deposited = float(input("\nPlease enter the amount of money that you are depositing: £"))

        interest_rate = float(input("Please enter the interest rate: "))

        investment_years = int(input("Please enter the number of years that you plan on investing for: "))

        interest = int(input('''\nPlease select the type of interest you would like: 
1. simple
2. compound 
        
Enter 1 or 2 to make your selection: '''))


        # If the user selects simple interest, this section uses the simple interest formula to calculate the amount at the end of the investment period. 
        if interest == 1:
            return_amount = round(money_deposited*(1 + (interest_rate/100)*investment_years), 2)
            print(f"\nAt the end of the investment period you will have £{return_amount}.\n")


        # If the user selects compound interest, this section uses the compound interest formula to calculate the amount at the end of the investment period. 
        elif interest == 2:
            return_amount = round(money_deposited*(math.pow(1+(interest_rate/100), investment_years)), 2)
            print(f"\nAt the end of the investment period you will have £{return_amount}.\n")

        # If the user does not select a type of interest this will print an error message. 
        else:
            print("\nError: the type of interest was not selected correctly. Please try again.\n")


    
    # The section of code below is the home repayment calculator and runs if the user selects bond from the start menu. 
    else: 

        current_value = float(input("\nPlease enter the current value of the house £"))

        interest_rate = float(input("Please enter the interest rate: "))

        months = int(input("How many months do you plan to take to repay the bond? "))

        # Calculate the monthly interest rate
        monthly_interest_rate = (interest_rate/100)/12

        # Use the bond repayment formula to calculate the monthly repayment amount for the values inputted by the user. 
        monthly_repayment = round((monthly_interest_rate*current_value)/(1 - 1/(math.pow(1 + monthly_interest_rate, months))), 2)

        print(f"\nYour monthly repayments will be £{monthly_repayment}.\n")


