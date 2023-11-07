
#financial calculator by Creative Innovators
while True:
    print("\n\n____________________________________________CREATIVE INNOVATORS____________________________________")
    print("____________________________________________FINANCIAL CALCULATOR___________________________________")
    print('\t\t\tChoose 1, 2, 3 or 4')
    choice = input('1). Compound Investment \n2). Simple Investment \n3). Home loan \n4). Exit \n Option :' )
    print("____________________________________________________________________________________________________\n")
    if choice == '1':# compound investment
        print(f"___________________________________Compound Investment Calculator___________________________________\n")
        
        def compound_interest_calculator(initial, rate, time):
            amount = initial * ((1 + (rate / 100)) ** time) #compound
            return amount
        
        while True:
            # Get user input
            initial = input("Enter the principal amount (initial amount): R")
            rate = input("Enter the annual interest rate (in percentage): ")
            time = input("Enter the time period (in years): ")
            print("____________________________________________________________________________________________________\n")
            #conversions and validations
            initial = initial.replace(" ","").strip() 
            rate    = rate.replace(" ","").strip() 
            time    = time.replace(" ","").strip() 
            #floating
            # if initial.isdigit() and rate.isdigit() and time.isdigit():
            if initial.replace(".","",1).isdigit() and rate.replace(".","",1).isdigit() and time.replace(".","",1).isdigit() :
                initial = float(initial)
                rate    = float(rate)
                time    = float(time)
                 # Calculate and print the final amount
                if rate <= 100: 
                    final_amount = compound_interest_calculator(initial, rate, time)
                    print(f"Investing R{initial} using compound interst after {round(time)}years will be: R{final_amount:.2f}")
                    print("____________________________________________________________________________________________________\n")
                    break
                else:
                    print(f"Rate can not be more than 100%")
                    print("____________________________________________________________________________________________________\n")
            # else:
            #     print("\t\t\tinvalid input!")
            else:
                print("\t\t\tInvalid input!") 
                print("____________________________________________________________________________________________________\n\n")  
                

           

    elif choice == '2': #simple investment
        print("Hi, you are welcome to a simple investment calculator. \n Shall we start.")
        def simple_interest_calc(initial, rate, time):
            amount = initial * ((1 + ((rate*time) / 100))) #simple
            return amount
        

        # Get user input
        while True:
            # Get user input
            initial = input("Enter the principal amount (initial amount): R")
            rate = input("Enter the annual interest rate (in percentage): ")
            time = input("Enter the time period (in years): ")
            print("____________________________________________________________________________________________________\n")
            #conversions and validations
            initial = initial.replace(" ","").strip() 
            rate    = rate.replace(" ","").strip() 
            time    = time.replace(" ","").strip() 
            #floating
            # if initial.isdigit() and rate.isdigit() and time.isdigit():
            if initial.replace(".","",1).isdigit() and rate.replace(".","",1).isdigit() and time.replace(".","",1).isdigit() :
                initial = float(initial)
                rate    = float(rate)
                time    = float(time)
                # Calculate and print the final amount
                if rate <= 100: 
                    final_amount = simple_interest_calc(initial, rate, time)
                    print(f"Investing R{initial} using Simple interest after {round(time)}years will be: R{final_amount:.2f}")
                    print("____________________________________________________________________________________________________\n")
                    break
                else:
                    print(f"Rate can not be more than 100%")
                    print("____________________________________________________________________________________________________\n")
            # else:
            #     print("\t\t\tinvalid input!")
            else:
                print("\t\t\tInvalid input!") 
                print("____________________________________________________________________________________________________\n\n")
    
    elif choice == '3':#home loan
        print("____________________________________________________________________________________________________")
        print("Hi, you are welcome to a home loan calculator. \n Shall we start.")
        print("____________________________________________________________________________________________________")
        def loan_repayment_calculator(initial, rate, time):
            monthly_interest = (rate / 100) / 12
            total_payments = time * 12
            monthly_payment = (initial * monthly_interest) / (1 - (1 + monthly_interest) ** -total_payments)
            
            return monthly_payment
        while True:
            # Get user input
            print("____________________________________________________________________________________________________")
            initial = input("Enter the principal amount (initial amount): ")
            rate = input("Enter the annual interest rate (in percentage): ")
            time = input("Enter the time period (in years): ")
            print("____________________________________________________________________________________________________")
            
            #conversions and validations
            initial = initial.replace(" ","").strip() 
            rate    = rate.replace(" ","").strip() 
            time    = time.replace(" ","").strip()
            
            if initial.replace(".","",1).isdigit() and rate.replace(".","",1).isdigit() and time.replace(".","",1).isdigit() :
                #floating
                initial = float(initial)
                rate    = float(rate)
                time    = float(time)
                if rate <=100 :
                    # Calculate and print the monthly repayment amount
                    monthly_payment = loan_repayment_calculator(initial, rate, time)
                    print("____________________________________________________________________________________________________")
                    print(f"The monthly repayment amount will be: R{monthly_payment:.2f}")
                    print(f"You will pay R{monthly_payment:.2f} per month for taking a home loan of R{initial}  for {round(time)} years with an interest of {rate}%")
                    print("____________________________________________________________________________________________________")
                    break
                else:
                    print(f"Rate can not be more than 100%")
                    print("____________________________________________________________________________________________________\n")
            else:
                print("\t\t\tInvalid input!") 
                print("____________________________________________________________________________________________________\n\n")
                
        
    elif choice == '4':
        print("Thank you for using our calculator, looking forward to help you calculate other financial problems in future")
        print("____________________________________________________________________________________________________\n")
        break
    else:
        print("\t\t\tInvalid input!") 
        print("____________________________________________________________________________________________________\n\n")      
#2023 NOVEMBER 03
#CAPE TOWN.