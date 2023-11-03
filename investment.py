
while True:
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    choice = input('choose 1, 2, 3 or 4 \n 1). Compound Investment \n 2). Simple Investment \n 3). Home loan \n 4). Exit \n :' )
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    if choice == '1':# compound investment
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(f"Hi, you are welcome to a compound investment calculator. \n Shall we start.")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        
        def investment_calculator(initial, rate, time):
            amount = initial * ((1 + (rate / 100.0)) ** time) #compound
            return amount
        

        # Get user input
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        initial = input("Enter the principal amount: ")
        rate = input("Enter the annual interest rate (in percentage): ")
        time = input("Enter the time period (in years): ")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        #conversions and validations
        initial = initial.replace(" ","").strip() 
        rate    = rate.replace(" ","").strip() 
        time    = time.replace(" ","").strip() 
        #floating
        initial = float(initial)
        rate    = float(rate)
        time    = float(time)

        # Calculate and print the final amount
        final_amount = investment_calculator(initial, rate, time)
        print(f"The final amount after {time} years will be: R{final_amount:.2f}")
    
    elif choice == '2': #simple investment
        print("Hi, you are welcome to a simple investment calculator. \n Shall we start.")
        def investment_calculator(initial, rate, time):
            amount = initial * ((1 + ((rate*time) / 100))) #simple
            return amount
        

        # Get user input
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        initial = input("Enter the principal amount: ")
        rate = input("Enter the annual interest rate (in percentage): ")
        time = input("Enter the time period (in years): ")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        #conversions and validations
        initial = initial.replace(" ","").strip() 
        rate    = rate.replace(" ","").strip() 
        time    = time.replace(" ","").strip()
         
        #floating
        initial = float(initial)
        rate    = float(rate)
        time    = float(time)
        # Calculate and print the final amount
        final_amount = investment_calculator(initial, rate, time)
        print(f"The final amount after {time} years will be: R{final_amount:.2f}")
    
    elif choice == '3':#home loan
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print("Hi, you are welcome to a home loan calculator. \n Shall we start.")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        def loan_repayment_calculator(initial, rate, time):
            monthly_interest = (rate / 100) / 12
            total_payments = time * 12
            monthly_payment = (initial * monthly_interest) / (1 - (1 + monthly_interest) ** -total_payments)
            
            return monthly_payment

         # Get user input
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        initial = input("Enter the principal amount: ")
        rate = input("Enter the annual interest rate (in percentage): ")
        time = input("Enter the time period (in years): ")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        #conversions and validations
        initial = initial.replace(" ","").strip() 
        rate    = rate.replace(" ","").strip() 
        time    = time.replace(" ","").strip() 
        #floating
        initial = float(initial)
        rate    = float(rate)
        time    = float(time)

        # Calculate and print the monthly repayment amount
        monthly_payment = loan_repayment_calculator(initial, rate, time)
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        print(f"The monthly repayment amount will be: {monthly_payment:.2f}")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    
    elif choice == '4':
        print("Thank you for using our calculator, looking forward to help you calculate other financial problems in future")
        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
        break
    else:
        print("Invalid input!")
        
