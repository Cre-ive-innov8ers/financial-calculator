
#financial calculator by Creative Innovators
while True:
    print("_______________________CREATIVE INNOVATORS____________________")
    print("_______________________FINANCIAL CALCULATOR___________________")
    print('\t\t\tChoose 1, 2, 3 or 4')
    choice = input('1). Compound Investment \n2). Simple Investment \n3). Home loan \n4). Exit \n Option :' )
    print("_____________________________________________________________")
    if choice == '1':# compound investment
        print(f"______________Compound Investment Calculator________________")
    
        def investment_calculator(initial, rate, time):
            amount = initial * ((1 + (rate / 100)) ** time) #compound
            return amount
        
        while True:
            # Get user input
            initial = input("Enter the principal amount (initial amount): ")
            rate = input("Enter the annual interest rate (in percentage): ")
            time = input("Enter the time period (in years): ")
            print("_____________________________________________________________")
            #conversions and validations
            initial = initial.replace(" ","").strip() 
            rate    = rate.replace(" ","").strip() 
            time    = time.replace(" ","").strip() 
            #floating
            # if initial.isdigit() and rate.isdigit() and time.isdigit():
            if initial.isdigit() and rate.isdigit() and time.isdigit():
                initial = float(initial)
                rate    = float(rate)
                time    = float(time)
                 # Calculate and print the final amount
                final_amount = investment_calculator(initial, rate, time)
                print(f"Investing R{initial} after {round(time)}years will be: R{final_amount:.2f}")
                print("_________________________________________________________")
                
            # else:
            #     print("\t\t\tinvalid input!")
            else:
                print("\t\t\tInvalid input!") 
                print("_____________________Test_______________________________________\n\n")  
                

           

    elif choice == '2': #simple investment
        print("Hi, you are welcome to a simple investment calculator. \n Shall we start.")
        def investment_calculator(initial, rate, time):
            amount = initial * ((1 + ((rate*time) / 100))) #simple
            return amount
        

        # Get user input
        print("____________________________________________________________")
        initial = input("Enter the principal amount (initial amount):")
        rate = input("Enter the annual interest rate (in percentage): ")
        time = input("Enter the time period (in years): ")
        print("____________________________________________________________")
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
        print("____________________________________________________________")
        print("Hi, you are welcome to a home loan calculator. \n Shall we start.")
        print("____________________________________________________________")
        def loan_repayment_calculator(initial, rate, time):
            monthly_interest = (rate / 100) / 12
            total_payments = time * 12
            monthly_payment = (initial * monthly_interest) / (1 - (1 + monthly_interest) ** -total_payments)
            
            return monthly_payment

        # Get user input
        print("____________________________________________________________")
        initial = input("Enter the principal amount (initial amount): ")
        rate = input("Enter the annual interest rate (in percentage): ")
        time = input("Enter the time period (in years): ")
        print("____________________________________________________________")
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
        print("____________________________________________________________")
        print(f"The monthly repayment amount will be: {monthly_payment:.2f}")
        print("____________________________________________________________")
    
    elif choice == '4':
        print("Thank you for using our calculator, looking forward to help you calculate other financial problems in future")
        print("____________________________________________________________\n")
        break
    else:
        print("\t\t\tInvalid input!") 
        print("____________________________________________________________\n\n")      
#2023 NOVEMBER 03
#CAPE TOWN.