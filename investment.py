name = input('Please enter your name:')
while True:
    choice = input('choose 1, 2, 3 or 4 \n 1). Compound Investment \n 2). Simple Investment \n 3). Home loan \n 4). Exit \n :' )

    if choice == '1':# compound investment
        print(f"Hi {name}, you are welcome to a compound investment calculator. \n Shall we start.")
        
        def investment_calculator(initial, rate, time):
            amount = initial * ((1 + (rate / 100)) ** time) #compound
            return amount
        

        # Get user input
        initial = float(input("Enter the initial amount: "))
        rate = float(input("Enter the annual interest rate (in percentage): "))
        time = float(input("Enter the time period (in years): "))

        # Calculate and print the final amount
        final_amount = investment_calculator(initial, rate, time)
        print(f"The final amount after {time} years will be: R{final_amount:.2f}")
    
    elif choice == '2': #simple investment
        print(f"Hi {name}, you are welcome to a simple investment calculator. \n Shall we start.")
        def investment_calculator(initial, rate, time):
            amount = initial * ((1 + ((rate*time) / 100))) #simple
            return amount
        

        # Get user input
        initial = float(input("Enter the initial amount: "))
        rate = float(input("Enter the annual interest rate (in percentage): "))
        time = float(input("Enter the time period (in years): "))

        # Calculate and print the final amount
        final_amount = investment_calculator(initial, rate, time)
        print(f"The final amount after {time} years will be: R{final_amount:.2f}")
    
    elif choice == '3':
        print(f"Hi {name}, you are welcome to a home loan calculator. \n Shall we start.")
        def loan_repayment_calculator(initial, rate, time):
            monthly_interest = (rate / 100) / 12
            total_payments = time * 12
            monthly_payment = (initial * monthly_interest) / (1 - (1 + monthly_interest) ** -total_payments)
            return monthly_payment

        # Get user input
        initial = float(input("Enter the initial amount of the loan: "))
        rate = float(input("Enter the annual interest rate (in percentage): "))
        time = int(input("Enter the time period of the loan (in years): "))

        # Calculate and print the monthly repayment amount
        monthly_payment = loan_repayment_calculator(initial, rate, time)
        print(f"The monthly repayment amount will be: {monthly_payment:.2f}")
    
    elif choice == '4':
        print(f"{choice}, thank you for using our calculator, looking forward to help you calculate other financial problems in future")
        break
    else:
        print(f"{choice} is an invalid input!, my guy be serious")
