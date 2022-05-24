import observers as obs
import settings
import adders as ads
import update as upd
import interface_extension as iE
import preF as preFab
import mysql.connector
import time

###INITIALISES THE CONNECTION AS A GLOBAL VARIABLE
settings.init()


#First Main attempt 

def Main():

    load = input("Would you like to load data into database y/n (For Mr Loup's eyes only no customer)\n")
    if load == "y" or load == "yes" or load == "Yes":
        preFab.executePreFab()

    print("""\nWelcome to the SneakerWolf Website!\nWe sell shoes of all kinds but first you have to make an account!\n""")
    returningCustomer = input("Do you have an account already? Yes/No ")


    #used to sign up new customer to sneakerWolf
    if returningCustomer == "No" or returningCustomer == "no":
        name = input("\nStart by giving us your name ")
        surname = input("Now your surname ")
        print("\nThank you now we need your address starting with your country ")
        delivery_country = input("The country you're in ")
        delivery_city = input("Your city ")
        delivery_street = input("The street name ")
        streetNumber = False
        while(not streetNumber):
            delivery_number = input("The street number ")
            if delivery_number.isnumeric() == True:
                streetNumber = True
            else:
                print("please enter a numeric value")
        delivery_postCode = input("and finally your post code ")

        same_billing = input("Is your billing address the same? Yes/No ")    

        if same_billing == "Yes" or same_billing == "yes" :
            billing_country = delivery_country
            billing_city = delivery_city
            billing_street = delivery_street
            billing_number =  delivery_number
            billing_postCode = delivery_postCode
        else:
            print("Alright please enter your billing address")
            billing_country = input("The country you're in ")
            billing_city = input("Your city ")
            billing_street = input("The street name ")
            streetNumber = False
            while(not streetNumber):
                delivery_number = input("The street number ")
                if delivery_number.isnumeric() == True:
                    streetNumber = True
                else:
                    print("please enter a numeric value")
            billing_number = input("The street number ")
            billing_postCode = input("and finally your post code ")

        vipYesNo = input("""\nAlso we're an exlusive high level fashin collector\nFor the low-low price of 50$ a month you can get VIP status giving you early access to limited edition stock! WoW ikr\nso Yes/No? """)

        if (vipYesNo == "Yes" or vipYesNo == "yes"):
            vipYesNo = 1
        else:
            vipYesNo = input("""\nAre you sure we have some pretty dope stuff in the back? ಠ__ಠ\nYes I've changed my mind/No """)
            if vipYesNo == "Yes" or vipYesNo == "yes":
                vipYesNo = 1
            else:
                vipYesNo = 0


        while (True):
            email = input("""Finally we need an email adress to connect you: """)
            password = input("""And now your password: """)
            
            ID_user = ads.subscribeCustomer(name, surname, billing_street, billing_number, billing_street, billing_number, billing_postCode, delivery_street, delivery_number, billing_postCode, billing_city, billing_country, email, password, vipYesNo)
            
            if ID_user == False:
                print("email already exists in the database please use another one ")
            else:
                print("You were successfully subscribed! ")
                connected_user = ID_user
                break
    else:
        while(True):
            emailUser = input("please enter your email address ")
            passwordUser = input("please enter your password ")
            succesfulLogin = obs.getUserByEmailPassword(emailUser, passwordUser)
            if (succesfulLogin != None):
                connected_user = succesfulLogin[0][0]
                break
            print("Wrong email or password!\n")
                
    print("\nWelcome to SneakerWolf what would you like to access?\n")
    while (True):
        

        choice = input("\nEnter 1 to see all models, enter 2 to search by sport, enter 3 to searh by gender category, 4 to look by brand\nPress 5 to change your personal info, 6 to view cart or 7 to initiate a return and finally press 8 to quit\n")
        if choice.isnumeric() == False:
            print("That's not an option try again: ")
            continue

        choice = int(choice)
        if choice == 1:
            #obs.getShoesByModel()
            obs.getAllShoesSpecifications()
            purchase = input("\nPress 1 to buy something or 2 to get back to the menu ")
            if purchase.isnumeric() == True:
                purchase = int(purchase)
                if purchase == 1:
                    quantity = input("please input quantity wanted ")
                    specificationId = input("please the specification Id ")
                    ads.createDetail(quantity, specificationId, connected_user)
        elif choice == 2:
            ####need to add input for sport choice
            obs.getSport()
            wantedSport = input("Please enter wanted sport ")
            obs.getShoesBySport(wantedSport)
        elif choice == 3:
            wantedS = input("Choose men, women, unisex")
            if (wantedS != "men" or wantedS != "women" or wantedS != "unisex"):
                obs.getShoesBySex(wantedS)
        elif choice == 4:
            ####we need to make a select here on only the brands istead of a print
            wantedBrand = input("We have nike, asics and adidas ")
            obs.getShoesByBrand(wantedBrand)
        elif choice == 5:
            returnedUserInfo = obs.getUserByID(connected_user)
            if returnedUserInfo != None:
                returnUnsub = iE.changeNewInfo(returnedUserInfo)
                if returnUnsub == "unsub":
                    break

        elif choice == 6:
            print("This is your cart content ")
            obs.findCartDetailByUserId(connected_user)

            saleOrContinue = input("Press 1 to purchase items in cart, press 2 to keep shopping ") 
            if saleOrContinue.isnumeric():
                saleOrContinue = int(saleOrContinue)
                if saleOrContinue == 1:
                    ads.addOrderDetailToOrder(connected_user)
                elif saleOrContinue == 2:
                    print("Enjoy your shopping! ")
                else:
                    print("wrong value try again ")
            else:
                print("You haven't entered a number try again ")
        elif choice == 7:
            print("This is the return menu")
            print("Please enter your shoes Id and your order number\nThis information should be on the papers we sent inside the delivery box ")
            specificationId = input("Please enter shoes Id: ")
            orderNumber = input("Please enter your order number: ")
            returnVal = ads.returnShoes(specificationId, connected_user, orderNumber)
            if returnVal != None:
                print("Your return is being processed!")
        elif choice == 8:
            break 
        else:
            ##################neeeds to be moved was put here for testing
            employeeInfo = obs.findEmployeeById(connected_user)
            if  employeeInfo != None:
                print("welcome to the hidden menu for company users")
                if employeeInfo[4] == "compatable" or employeeInfo[4] == "CEO":
                    choices = input("Press 1 to send pending orders from warehouse, press 2 to move stock from warehouses or press 3 to access accounting view or 4 to quit")
                    accesGranted = True
                else:
                    choices = input("Press 1 to send pending orders from warehouse, press 2 to move stock from warehouses 3 to quit")
                    accesGranted = False

                if choices.isnumeric() == True:
                    choices = int(choices)

                if choices == 1:
                    serviceProvider = input("If you would you like to send with bpost press 1, press 2 to use ups")
                    serviceProvider = int(serviceProvider)
                    if serviceProvider == 1:
                        ads.sendOrders(connected_user, 1)
                    else:
                        ads.sendOrders(connected_user, 2)
                elif choices == 2:
                    load = input("Would you like to move some stock from one warehoues to another? y/n ")
                    if load == "y" or load == "yes" or load == "Yes":
                        iE.changeNewInfoWarehouse()
                elif choices == 3 and accesGranted == True:
                    print("current year revenue")
                    obs.getSalesRevenueAnnually()

                    year_wanted = input("Would you like to see past sales? y/n ")
                    if year_wanted == "y" or year_wanted == "yes" or year_wanted == "Yes":
                        obs.getSalesRevenueAnnually(year_wanted)

                    seeMonthly = input("Would you like to see the monthly revenue of a year? if yes please enter a year ")
                    if seeMonthly.isnumeric():
                        obs.getSalesRevenueMonthly(seeMonthly)

                    seeCountrySale = input("\nWould you like to see the sales by country? y/n ")
                    if seeCountrySale == "y" or seeCountrySale == "yes" or seeCountrySale == "Yes":
                        obs.getSalesRevenueByCountry()

                    addPromotion = input("Would you like to add a new promotion? y/s")
                    if addPromotion == "y" or addPromotion == "yes" or addPromotion == "Yes":
                        name = input("please enter the name of the promotion in less than 10 caracters: ")
                        start_date = input("please enter the start date of the promtion in format xxxx-xx-xx:  ")
                        end_date =input("please enter the end date of the promtion in format xxxx-xx-xx:  ")
                        
                        rateAmount = input("Should it be a percentage or a fixed amount? 1 for percetage 2 for amount ")

                        if rateAmount.isnumeric():
                            rateAmount = int(rateAmount)
                            if rateAmount == 1:
                                rate = input("Please input promotion rate in form 0.x: ")
                                ads.addPromotion(name, start_date, end_date, rate, 0)
                            else:
                                amount = input("Please input promotion amount: ")
                                ads.addPromotion(name, start_date, end_date, 0, amount)


                continue

            print("invalid input please try again ")
            
        # extractedUserInfo = getUserByID(ID_user)
        # name = input("please give your name")
        #appel update updateUserInfo(extractedUserInfo)

    print("Thank you for shopping at sneakerWolf!")
    settings.cnx.close()

Main()

