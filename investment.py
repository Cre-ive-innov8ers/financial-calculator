import math
import creativemodule4quotes


#financial calculator by Creative Innovators
while True:
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n________________________________________Financial Calculator________________________________________\n")
    period = input("Welcome to the financial calculator.\nplease be advised to that this calculator takes in the period(n) in either months or years  \nchoose either(1,2 or 3)\n1). Month\n2). Year\n3) Exit\nOption : ")
    print("____________________________________________________________________________________________________\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    ##################################################################################################################
    if period == '1':#Period in Months
        while True:
            print("____________________________________________CREATIVE INNOVATORS______________________________________")
            print("___________________________________________FINANCIAL CALCULATOR_________________________________________")
            print("__________________________________________NB. Period is in months________________________________________")
            choice = input('1). Investment \n2). Home loan \n3). Exit \n(Choose 1, 2 or 3)\n____________________________________________________________________________________________________\n Option :' )
            print("____________________________________________________________________________________________________\n")

            

            if choice == '1':# Investment
                print(f"___________________________________Investment Calculator___________________________________\n")
                while True:
                    option= input('1). Compound Investment \n2). Simple Investment \n3). Exit \n____________________________________________________________________________________________________\n Option :' )
                    if option == '1':#Compound
                        print(f"___________________________________Compound Investment Calculator___________________________________\n")
                        def compound_interest_calculator(initial, rate, time):
                            P =initial
                            r=rate/100
                            t= time/12
                            A = P* math.pow((1+r),t)
                            amount = A
                            return amount
                        
                        while True:
                            # Get user input
                            initial = input("Enter the principal amount (initial amount): R")
                            initial= initial.replace(" ", "").strip()
                            while True:
                                if initial.replace(".","",1).isdigit():
                                    break
                                else:
                                    initial = input("Invalid input!\nRe-Enter the principal amount (initial amount): ")
                    
                            rate = input("Enter the annual interest rate (in percentage): ")
                            rate= rate.replace(" ", "").strip()
                            while True:
                                if rate.replace(".","",1).isdigit() and float(rate)<= 100:
                                    break
                                else:
                                    rate = input("Invalid input!\nRe-Enter the annual interest rate (in percentage): ")
                                    

                            time = input("Enter the time period (in months): ")
                            time = time.replace(" ", "").strip()
                            print("____________________________________________________________________________________________________\n")
                            while True:
                                if time.replace(".","",1).isdigit():
                                    break
                                else:
                                    time = input("Invalid input!\nRe-Enter the time period (in years): ")

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
                                    print(f"Investing R{initial} for {rate}%  after {round(time)} month(s) will be: R{final_amount:.2f}")
                                    print("____________________________________________________________________________________________________\n")
                                    creativemodule4quotes.rand_quote()
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
                                

                    
                    elif option=='2':#simple investment
                        print(f"___________________________________Simple Investment Calculator___________________________________\n")
                        def simple_interest_calculator(initial, rate, time):
                            P = initial
                            r = rate/100
                            t = time/12
                            A = P*(1+r*t)
                            amount = A
                            return amount
                        
                        while True:
                            # Get user input

                            initial = input("Enter the principal amount (initial amount): R")
                            initial= initial.replace(" ", "").strip()
                            while True:
                                if initial.replace(".","",1).isdigit():
                                    break
                                else:
                                    initial = input("Invalid input!\nRe-Enter the principal amount (initial amount): ")
                    
                            rate = input("Enter the annual interest rate (in percentage): ")
                            rate= rate.replace(" ", "").strip()
                            while True:
                                if rate.replace(".","",1).isdigit() and float(rate)<= 100:
                                    break
                                else:
                                    rate = input("Invalid input!\nRe-Enter the annual interest rate (in percentage): ")
                                    

                            time = input("Enter the time period (in months): ")
                            time = time.replace(" ", "").strip()
                            print("____________________________________________________________________________________________________\n")
                            while True:
                                if time.replace(".","",1).isdigit():
                                    break
                                else:
                                    time = input("Invalid input!\nRe-Enter the time period (in years): ")

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
                                    final_amount = simple_interest_calculator(initial, rate, time)
                                    print(f"Investing R{initial} using simple interst after {round(time)} month(s) will be: R{final_amount:.2f}")
                                    print("____________________________________________________________________________________________________\n")
                                    creativemodule4quotes.rand_quote()
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
                    elif option == '3':
                        print("____________________________________________________________________________________________________\n")
                        creativemodule4quotes.rand_quote()
                        print("____________________________________________________________________________________________________\n")
                        break
                    else:
                        print("____________________________________________________________________________________________________\n")
                        print('Invalid Input')
                        print("____________________________________________________________________________________________________\n")
                ###########################################################################################################################################
            elif choice == '2':#home loan
                print("____________________________________________________________________________________________________")
                print(f"_______________________________Home Loan Monthly Payment Calculator_______________________________\n")
                print("____________________________________________________________________________________________________")
                def loan_repayment_calculator(initial, rate, time):
                    monthly_interest = rate / 1200
                    total_payments = time #In month 
                    monthly_payment = (initial * monthly_interest) / (1 - math.pow((1 + monthly_interest),-total_payments))
                    
                    return monthly_payment
                while True:
                    # Get user input
                    print("____________________________________________________________________________________________________")
                    initial = input("Enter the principal amount (initial amount): ")
                    while True:
                        if initial.replace(".","",1).isdigit():
                            break
                        else:
                            initial = input("Invalid input!\nRe-Enter the principal amount (initial amount): ")
            
            
                    rate = input("Enter the annual interest rate (in percentage): ")
                    rate= rate.replace(" ", "").strip()
                    while True:
                        if rate.replace(".","",1).isdigit() and float(rate)<= 100:
                            break
                        else:
                            rate = input("Invalid input!\nRe-Enter the annual interest rate (in percentage): ")
                
                    time = input("Enter the time period (in month(s)): ")
                    print("____________________________________________________________________________________________________")
                    while True:
                        if time.replace(".","",1).isdigit():
                            break
                        else:
                            initial = input("Invalid input!\nRe-Enter the time period (in month(s)): ")
                    
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
                            print(f"You will pay R{monthly_payment:.2f} per month for taking a home loan of R{initial}  for {round(time)} month(s) with an interest of {rate}%")
                            print("____________________________________________________________________________________________________\n")
                            creativemodule4quotes.rand_quote()
                            print("____________________________________________________________________________________________________\n")
                            break
                        else:
                            print(f"Rate can not be more than 100%")
                            print("____________________________________________________________________________________________________\n")
                    else:
                        print("\t\t\tInvalid input!") 
                        print("____________________________________________________________________________________________________\n\n")
                        
                
            elif choice == '3':
                print("Thank you for using our calculator, looking forward to help you calculate other financial problems in future")
                print("____________________________________________________________________________________________________\n")
                creativemodule4quotes.rand_quote()
                print("____________________________________________________________________________________________________\n")
                break
            else:
                print("\t\t\tInvalid input!") 
                print("____________________________________________________________________________________________________\n\n")      
#############################################################################################################################    
    elif period == '2':# period in in years
         while True:
            print("____________________________________________CREATIVE INNOVATORS______________________________________________")
            print("____________________________________________FINANCIAL CALCULATOR_________________________________________________")
            print("____________________________________________NB. Period is in years_________________________________________________")
            choice = input('1). Investment \n2). Home loan \n3). Exit \n(Choose 1, 2 or 3)\n____________________________________________________________________________________________________\n Option :' )
            print("____________________________________________________________________________________________________\n")

            

            if choice == '1':# Investment
                print(f"___________________________________Investment Calculator___________________________________\n")
                while True:
                    option= input('1). Compound Investment \n2). Simple Investment \n3). Exit \n____________________________________________________________________________________________________\n Option :' )
                    if option == '1':#Compound
                        print(f"___________________________________Compound Investment Calculator___________________________________\n")
                        def compound_interest_calculator(initial, rate, time):
                            P =initial
                            r=rate/100
                            t= time
                            A = P* math.pow((1+r),t)
                            amount = A
                            return amount
                        
                        while True:
                            # Get user input
                            initial = input("Enter the principal amount (initial amount): R")
                            initial= initial.replace(" ", "").strip()
                            while True:
                                if initial.replace(".","",1).isdigit():
                                    break
                                else:
                                    initial = input("Invalid input!\nRe-Enter the principal amount (initial amount): ")
                    
                            rate = input("Enter the annual interest rate (in percentage): ")
                            rate= rate.replace(" ", "").strip()
                            while True:
                                if rate.replace(".","",1).isdigit() and float(rate)<= 100:
                                    break
                                else:
                                    rate = input("Invalid input!\nRe-Enter the annual interest rate (in percentage): ")
                                    

                            time = input("Enter the time period (in years): ")
                            time = time.replace(" ", "").strip()
                            print("____________________________________________________________________________________________________\n")
                            while True:
                                if time.replace(".","",1).isdigit():
                                    break
                                else:
                                    time = input("Invalid input!\nRe-Enter the time period (in years): ")

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
                                    print(f"Investing R{initial} using compound interst after {round(time)} year(s) will be: R{final_amount:.2f}")
                                    print("____________________________________________________________________________________________________\n")
                                    creativemodule4quotes.rand_quote()
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
                                

                    
                    elif option=='2':#simple investment
                        print(f"___________________________________Simple Investment Calculator___________________________________\n")
                        def simple_interest_calculator(initial, rate, time):
                            P = initial
                            r = rate/100
                            t = time
                            A = P*(1+r*t)
                            amount = A
                            return amount
                        
                        while True:
                            # Get user input

                            initial = input("Enter the principal amount (initial amount): R")
                            initial= initial.replace(" ", "").strip()
                            while True:
                                if initial.replace(".","",1).isdigit():
                                    break
                                else:
                                    initial = input("Invalid input!\nRe-Enter the principal amount (initial amount): ")
                    
                            rate = input("Enter the annual interest rate (in percentage): ")
                            rate= rate.replace(" ", "").strip()
                            while True:
                                if rate.replace(".","",1).isdigit() and float(rate)<= 100:
                                    break
                                else:
                                    rate = input("Invalid input!\nRe-Enter the annual interest rate (in percentage): ")
                                    

                            time = input("Enter the time period (in years): ")
                            time = time.replace(" ", "").strip()
                            print("____________________________________________________________________________________________________\n")
                            while True:
                                if time.replace(".","",1).isdigit():
                                    break
                                else:
                                    time = input("Invalid input!\nRe-Enter the time period (in years): ")

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
                                    final_amount = simple_interest_calculator(initial, rate, time)
                                    print(f"Investing R{initial} using simple interst after {round(time)} year(s) will be: R{final_amount:.2f}")
                                    print("____________________________________________________________________________________________________\n")
                                    creativemodule4quotes.rand_quote()
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
                    elif option == '3':
                        creativemodule4quotes.rand_quote()
                        break
                    else:
                        print("____________________________________________________________________________________________________\n")
                        print('Invalid Input')
                        print("____________________________________________________________________________________________________\n")
                ###########################################################################################################################################
            elif choice == '2':#home loan
                print("____________________________________________________________________________________________________")
                print(f"_______________________________Home Loan yearly Payment Calculator_______________________________\n")
                print("____________________________________________________________________________________________________")
                def loan_repayment_calculator(initial, rate, time):
                    monthly_interest = rate / 1200
                    total_payments = time * 12
                    monthly_payment = (initial * monthly_interest) / (1 - math.pow((1 + monthly_interest),-total_payments))
                    
                    return monthly_payment
                while True:
                    # Get user input
                    print("____________________________________________________________________________________________________")
                    initial = input("Enter the principal amount (initial amount): ")
                    while True:
                        if initial.replace(".","",1).isdigit():
                            break
                        else:
                            initial = input("Invalid input!\nRe-Enter the principal amount (initial amount): ")
            
            
                    rate = input("Enter the annual interest rate (in percentage): ")
                    rate= rate.replace(" ", "").strip()
                    while True:
                        if rate.replace(".","",1).isdigit() and float(rate)<= 100:
                            break
                        else:
                            rate = input("Invalid input!\nRe-Enter the annual interest rate (in percentage): ")
                
                    time = input("Enter the time period (in year(s)): ")
                    print("____________________________________________________________________________________________________")
                    while True:
                        if time.replace(".","",1).isdigit():
                            break
                        else:
                            initial = input("Invalid input!\nRe-Enter the time period (in year(s)): ")
                    
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
                            print(f"You will pay R{monthly_payment:.2f} per month for taking a home loan of R{initial}  for {round(time)} year(s) with an interest of {rate}%")
                            print("____________________________________________________________________________________________________\n")
                            creativemodule4quotes.rand_quote()
                            print("____________________________________________________________________________________________________\n")
                            break
                        else:
                            print(f"Rate can not be more than 100%")
                            print("____________________________________________________________________________________________________\n")
                    else:
                        print("\t\t\tInvalid input!") 
                        print("____________________________________________________________________________________________________\n\n")
                        
                
            elif choice == '3':
                print("Thank you for using our calculator, looking forward to help you calculate other financial problems in future")
                print("____________________________________________________________________________________________________\n")
                creativemodule4quotes.rand_quote()
                print("____________________________________________________________________________________________________\n")
                break
            else:
                print("\t\t\tInvalid input!") 
                print("____________________________________________________________________________________________________\n\n")    
    elif period == '3':
        creativemodule4quotes.rand_quote()
        print("____________________________________________________________________________________________________\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        break	
    else:#error choice
        print("Invalid input!") 
        #2023 NOVEMBER 09 for 10 Novemebr 2023
        #CAPE TOWN.