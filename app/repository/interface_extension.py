import settings
import observers as obs
import update as upd

def changeNewInfoWarehouse():

    result = obs.getAllWarehouseByID()

    print("Product ID    Warehouse ID      Available stock", end = ' ')
    for i in range(len(result)):
        print("\n")
        for j in range(len(result[i])):
            print("   ", end = ' ')
            print(result[i][j], end = '             ')

    productId = input("\nPlease enter a productId to move: ")
    quantity = input("Please enter quantity: ")
    sourceId = input("Please enter source warehouse")
    arrivalId = input("Please enter destination warehouse")
    warehouseSource = obs.getWarehouseByID(sourceId)
    warehouseArrival = obs.getWarehouseByID(arrivalId)
    warehouseInfo = []
    if warehouseArrival == None:
        warehouseInfo.append(productId)
        warehouseInfo.append(warehouseSource) 
        #this option passes only the warehouse id of the arrival as it doesnt have the shoe in stock at all and needs to be created in to_stock
        warehouseInfo.append(warehouseArrival)
    else:
        warehouseInfo.append(productId)
        #this version passes two tuples containing the infos of the warehouses
        warehouseInfo.append(warehouseSource) 
        warehouseInfo.append(warehouseArrival)
    upd.updateStockWarehouse(warehouseInfo, quantity)


def changeNewInfo(extractedUserInfo):

    extractedUserInfoCopy = []
    userInfoList = []
    userCustEmpList = []
    extractedUserInfoCopy.append(userInfoList)
    extractedUserInfoCopy.append(userCustEmpList)

    for i in range(len(extractedUserInfo[0])):
        extractedUserInfoCopy[0].append(extractedUserInfo[0][i])
    
    for j in range(len(extractedUserInfo[1])):
        extractedUserInfoCopy[1].append(extractedUserInfo[1][j])


#ID_user, Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street ,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country
    choice = 0
    
    while(choice != 7):

        if (extractedUserInfo[0][14] == None):
            choice = input("Press 1 to change name , press 2 to change surname\npress 3 to change billing address, press 4 to change delievery address\npress 5 to change employee info, \n6 to delete your account\n press 7 to apply")
            customer = False
        else:
            choice = input("Press 1 to change name , press 2 to change surname\npress 3 to change billing address, press 4 to change delievery address\npress 5 to change Customer info, \n6 to delete your account\n press 7 to apply")
            customer = True
        choice = int(choice)

        if choice == 1:
            extractedUserInfoCopy[0][1] = input("enter new name: ")
        elif choice == 2:
            extractedUserInfoCopy[0][2] = input("enter new surname: ")
        elif choice == 3:
            choiceBilling = input("Press 1 to change Country , press 2 to change City\npress 3 to change Postal Code, press 4 to change Street\npress 5 to number: ")
            if choiceBilling == 1:
                extractedUserInfoCopy[0][7] =  input("enter new country: ")
            elif choiceBilling == 2:
                extractedUserInfoCopy[0][6] =  input("enter new city: ")
            elif choiceBilling == 3:
                extractedUserInfoCopy[0][5] =  input("enter new postal code: ")
            elif choiceBilling == 4:
                extractedUserInfoCopy[0][3] =  input("enter new street: ")
            elif choiceBilling == 5:
                extractedUserInfoCopy[0][4] =  input("enter new number: ")
        elif choice == 4:
            choiceDelivery = input("Press 1 to change Country , press 2 to change City\npress 3 to change Postal Code, press 4 to change Street\npress 5 to number: ")
            if choiceDelivery == 1:
                extractedUserInfoCopy[0][12] =  input("enter new country: ")
            elif choiceDelivery == 2:
                extractedUserInfoCopy[0][11] =  input("enter new city: ")
            elif choiceDelivery == 3:
                extractedUserInfoCopy[0][10] =  input("enter new postal code: ")
            elif choiceDelivery == 4:
                extractedUserInfoCopy[0][8] =  input("enter new street: ")
            elif choiceDelivery == 5:
                extractedUserInfoCopy[0][9] =  input("enter new number: ")
        elif choice == 5 and customer == False:
            choiceEmployee = input("Press 1 to change Title , press 2 to change departement Id\npress 3 to change your supervisor: ")
            if choiceEmployee == 1:
                extractedUserInfoCopy[1][4] = input("enter your new title, I hope it was a promotion!: ")
            elif choiceEmployee == 2:
                extractedUserInfoCopy[1][5] = input("enter your new departement id: ")
            elif choiceEmployee == 3:
                extractedUserInfoCopy[1][6] = input("enter the personal number of your new supervisor: ")
        elif choice == 5 and customer == True:
            extractedUserInfoCopy[1][1] = input("Please enter 1 if you would like to become VIP or 0 to unsubsribe")
        elif choice == 6:
            usernameEntry = input("please enter username (cap sensitive): ")
            passwordEntry = input("and now you password: ")
            confirmation = input("Are you sure? Yes/No ")
            if confirmation == "yes" or confirmation == "Yes":
                userInfo = obs.getUserByUsernamePassword(usernameEntry, passwordEntry)
                if userInfo != None:
                    upd.unsubrsibeUser(userInfo[0][0])
                else:
                    print("wrong password nice try. ")

    upd.updateUserInfo(extractedUserInfoCopy[0])

    if (customer == False):
        upd.updateEmpInfo(extractedUserInfoCopy[1])
    elif (customer == True):
        upd.updateCustInfo(extractedUserInfoCopy[1])