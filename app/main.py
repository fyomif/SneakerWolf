from classes.user import User
from views.login_register_views import *
from views.product_views import *
from views.cart_views import *
from views.user_views import *
from views.accounting_views import *


def isAccountant(user):
    department_id = user.employee.to_work_id
    department_name = ""
    # TODO: Call of function that get the department_name of a user with department_id

    if department_name.lower() == "accounting" or department_name.lower() == "comptabilité":
        return True
    else:
        return False


def Main():
    #currentUser = User('','','','','','','','','','','','','','','','')
    currentUser = None

    print("""Welcome to the SneakerWolf Website!\nWe sell shoes of all kinds but first you\n""")

    print("Let us introduce you to our new products \n")
    # TODO: Function to list the 10 last product in the database
    choice = "",

    while choice != '0':
        print("Our options : \n")
        if currentUser is None:
            print("\t 1 : Create an account or sign in \n")
            print("\t 2 : Consult the list of products\n")
            print("\t 3 : Consult a specific category \n")
            print("\t 4 : Research a specific product \n")
            print("\t 5 : Consult the cart \n")
            print("\t 0 : Exit \n")
            choice = input("Your choice : ")
            notLoggedOption(choice)
        #elif currentUser is not None and isAccountant(currentUser):
        elif currentUser is not None:
            print("\t 1 : Consult your profile \n")
            print("\t 2 : Consult the client list \n")
            print("\t 3 : Consult the employees list \n")
            print("\t 4 : Consult the Annual report \n")
            print("\t 5 : Log out \n")
            print("\t 0 : Exit \n")
            choice = input("Your choice : ")
            accountingOption(choice, currentUser)
        else:
            print("\t 1 : Consult your profile \n")
            print("\t 2 : Consult the list of products \n")
            print("\t 3 : Consult a specific category \n")
            print("\t 4 : Research a specific product \n")
            print("\t 5 : Consult the cart \n")
            print("\t 6 : Log out \n")
            print("\t 0 : Exit \n")
            choice = input("Your choice : ")
            LoggedOption(choice, currentUser)


def notLoggedOption(option):
    if option == '1':
        answer = input("Do you have an account on sneakerwolf ? [Y/N] ")
        if answer.lower() == "y" or answer.lower() == "yes":
            Login()
        else:
            Register()
    elif option == "2":
        Product_listing()
    elif option == "3":
        Product_by_category()
    elif option == "4":
        Research_product()
    elif option == "5":
        Consult_cart()
    else:
        # go out
        print("")


def accountingOption(option, user):
    if option == '1':
        Consult_profile(user)
    elif option == "2":
        Consult_client_list()
    elif option == "3":
        Consult_employee_list()
    elif option == "4":
        Consult_annual_report()
    elif option == "5":
        Logout(user)
    else:
        # go out
        print("")


def LoggedOption(option, user):
    if option == '1':
        Consult_profile(user)
    elif option == "2":
        Product_listing()
    elif option == "3":
        Product_by_category()
    elif option == "4":
        Research_product()
    elif option == "5":
        Consult_cart()
    elif option == "6":
        Logout(user)
    else:
        # go out
        print("")


if __name__ == '__main__':
    Main()
