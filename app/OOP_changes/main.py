import observers as obs
import settings
import adders as ads
import update as upd
import interface_extension as iE
import mysql.connector
import time

###INITIALISES THE CONNECTION AS A GLOBAL VARIABLE
settings.init()


#First Main attempt 

def Main():

    #opens conection to database
    print("""Welcome to the SneakerWolf Website!\nWe sell shoes of all kinds but first you\nHave to make an account!""")
    returningCustomer = input("Do you have an account already? Yes/No ")


    #used to sign up new customer to sneakerWolf
    if returningCustomer == "No" or returningCustomer == "no":
        name = input("Start by giving us your name")
        surname = input("Now your surname")
        print("Thank you now we need your addrees starting with your country")
        delivery_country = input("The country you're in")
        delivery_city = input("Your city")
        delivery_street = input("The street name")
        delivery_number = input("The street number")
        delivery_postCode = input("and finally your post code")

        same_billing = input("Is your billing address the same? Yes/No")    

        if same_billing == "Yes":
            billing_country = delivery_country
            billing_city = delivery_city
            billing_street = delivery_street
            billing_number =  delivery_number
            billing_postCode = delivery_postCode

        vipYesNo = input("""Also we're an exlusive high level fashin collector\nFor the low-low price of 50$ a month you can get VIP status giving you early access to limited edition stock! WoW ikr\nso Yes/No?""")

        if (vipYesNo == "Yes"):
            vipYesNo = 1
        else:
            vipYesNo = input("""Are you sure we have some pretty dope stuff in the back? ಠ__ಠ\nYes I've changed my mind/No\n""")
            if vipYesNo == "Yes":
                vipYesNo = 1
            else:
                vipYesNo = 0

        username = input("""Finally lets get you a username: """)
        password = input("""And now your password: """)
         

        ID_user = ads.subscribeCustomer(name, surname, billing_street, billing_number, billing_street, billing_number, billing_postCode, delivery_street, delivery_number, billing_postCode, billing_city, billing_country, username, password, vipYesNo)
        print("Your customer id is %d, don't forget it you'll need it to log in!" % ID_user)
        connected_user = ID_user
    else:
        while(True):
            emailUser = input("please enter your email address ")
            passwordUser = input("please enter your password ")
            succesfulLogin = obs.getUserByEmailPassword(emailUser, passwordUser)
            if (succesfulLogin != None):
                connected_user = succesfulLogin[0][0]
                break
            print("Wrong email or password!\n")
                
    #Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country

    while (True):
        print("What would you like to access?")

        choice = input("enter 1 to see all models, enter 2 to search by sport, enter 3 to searh by gender category, 4 to look by brand or 5 to change your personal info\nPress 6 to view cart")
        if choice.isnumeric() == False:
            print("That's not an option try again: ")
            continue

        choice = int(choice)
        if choice == 1:
            #obs.getShoesByModel()
            obs.getAllShoesSpecifications()
            quantity = input("please input quantity wanted")
            specificationId = input("please the specification Id")
            ads.createDetail(quantity, specificationId, 1)
        elif choice == 2:
            ####need to add input for sport choice
            obs.getShoesBySport("running ")
        elif choice == 3:
            wantedS = input("Choose men, women, unisex or child ")
            obs.getShoesBySex(wantedS)
        elif choice == 4:
            ####we need to make a select here on only the brands istead of a print
            wantedBrand = input("We have nike, asics and adidas ")
            obs.getShoesByBrand(wantedBrand)
        elif choice == 5:
            ID_user = input("Please input your ID ")
            returnedUserInfo = obs.getUserByID(ID_user)
            if returnedUserInfo != None:
                iE.changeNewInfo(returnedUserInfo)
            else:
                print("wrong information try again. ")
        elif choice == 6:
            print("This is your cart content")
            print(obs.findCartDetailByUserId(connected_user))

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
        else:
            ##################neeeds to be moved was put here for testing
            iE.changeNewInfoWarehouse()
            print("invalid input please try again ")
            
        # extractedUserInfo = getUserByID(ID_user)
        # name = input("please give your name")
        #appel update updateUserInfo(extractedUserInfo)

    cnx.close()

Main()

