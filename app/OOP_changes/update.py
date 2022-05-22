import settings
import adders as ads

"""
DELETE PERSONAL INFORMATION
"""

def unsubrsibeUser(userID):
    userID = str(userID)
    cursor = settings.cnx.cursor()
    update_user = ("""UPDATE User SET Name = 'unsubscribed', Surname = 'unsubscribed', billing_add_Street = 'unsubscribed',billing_add_Number = 0,  billing_add_Postal_code = 'unsubscribed', billing_add_City = 'unsubscribed' ,billing_add_Country = 'unsubscribed', delivery_add_Street = 'unsubscribed',  delivery_add_Number = 0, delivery_add_Postal_code = 'unsubscribed', delivery_add_City = 'unsubscribed', delivery_add_Country = 'unsubscribed', username = 'unsubscribed', password = 'unsubscribed'
                      WHERE ID = %s""" % (userID))

    cursor.execute(update_user)

    settings.cnx.commit()




def updateStockWarehouse(warehouseInfo, quantity):
    cursor = settings.cnx.cursor()
    print(warehouseInfo)
    info_warehouse_quantity = ("""SELECT Quantity FROM To_stock
                                WHERE ID = %s
                                AND T_S_ID = %s""" % (warehouseInfo[1][1], warehouseInfo[0]))

    cursor.execute(info_warehouse_quantity)
    info_warehouse_quantity = cursor.fetchone()

    print(info_warehouse_quantity)
    print("this is the info warehouse")

    if info_warehouse_quantity == None:
        return None

    if int(info_warehouse_quantity[0]) >= int(quantity):



        update_warehouse1 = ("""UPDATE To_stock SET Quantity = %(quantity)s
                            WHERE ID = %(ID)s""")

        new_quantity = int(info_warehouse_quantity[0]) - int(quantity)

        data_update = {
        'quantity': new_quantity,
        'ID' : warehouseInfo[1][1],
        }            
        
        cursor.execute(update_warehouse1, data_update)
        if type(warehouseInfo) == list:
            update_warehouse2 = ("""UPDATE To_stock SET Quantity = %(quantity)s
                            WHERE ID = %(ID)s""")

            new_quantity = int(warehouseInfo[2][2]) + int(quantity)
            print(new_quantity)
            print("THIS IS THE NEW QUANTITY WHICH WONT UPDATE")

            data_update = {
            'quantity': new_quantity,
            'ID' : warehouseInfo[2][1],
            }    

            result = cursor.execute(update_warehouse2, data_update)
        else:
            ads.setWarehouseStock(warehouseInfo[2], warehouseInfo[0], quantity)
            
    else:
        return "not enough quantity in source warehouse"



    settings.cnx.commit()





# Params to be replaced by a tupp
def updateUserInfo(extractedUserInfo):

    #the return is true if 
    
    cursor = settings.cnx.cursor()
    update_user = ("""UPDATE User SET Name = %(Name)s, Surname = %(Surname)s, billing_add_Street = %(billing_add_Street)s,billing_add_Number = %(billing_add_Number)s,  billing_add_Postal_code = %(billing_add_Postal_code)s, billing_add_City = %(billing_add_City)s,billing_add_Country = %(billing_add_Country)s, delivery_add_Street = %(delivery_add_Street)s,  delivery_add_Number = %(delivery_add_Number)s, delivery_add_Postal_code = %(delivery_add_Postal_code)s, delivery_add_City = %(delivery_add_City)s, delivery_add_Country = %(delivery_add_Country)s
                      WHERE ID = %(ID)s""")


    data_update = {
    'Name': extractedUserInfo[1],
    'Surname' : extractedUserInfo[2],
    'billing_add_Street' : extractedUserInfo[3],
    'billing_add_Number' : extractedUserInfo[4],  
    'billing_add_Postal_code' : extractedUserInfo[5], 
    'billing_add_City' : extractedUserInfo[6],
    'billing_add_Country' : extractedUserInfo[7],
    'delivery_add_Street' : extractedUserInfo[8],  
    'delivery_add_Number' : extractedUserInfo[9], 
    'delivery_add_Postal_code' : extractedUserInfo[10], 
    'delivery_add_City' : extractedUserInfo[11], 
    'delivery_add_Country' : extractedUserInfo[12],
    'ID': extractedUserInfo[0],
    }

    cursor.execute(update_user, data_update)

    settings.cnx.commit()
    # In GUI we call based on User status
    # def updateCustInfo

    # def updateEmpInfo

def updateCustInfo(extractedCustomerInfo):
    cursor = settings.cnx.cursor()

    update_customer = ("""UPDATE Customer SET VIP = %(VIP)s
                          WHERE ID = %(ID)s""")

    # Insert Sport information
    data_update = {
    'ID': extractedCustomerInfo[0],
    'VIP': extractedCustomerInfo[1],
    }

    cursor.execute(update_customer, data_update)

    settings.cnx.commit()

def updateEmpInfo(extractedEmployeeInfo):
    cursor = settings.cnx.cursor()

    update_employee = ("""UPDATE Employee SET Title = %(Title)s, To_work_ID = %(workplace)s, Supervisor_ = %(supervisor)s
                      WHERE Personnal_number = %(personalID)s""")

    # Insert Sport information
    data_update = {
    'personalID' : extractedEmployeeInfo[0],
    'Title': extractedEmployeeInfo[4],
    'workplace': extractedEmployeeInfo[5],
    'supervisor' : extractedEmployeeInfo[6]
    }

    cursor.execute(update_employee, data_update)

    settings.cnx.commit()











##################################TO DO 
def updateRemovePurchasedStock():

    cursor = settings.cnx.cursor()

    info_warehouse_quantity = ("""SELECT Quantity FROM To_stock
                                WHERE ID = %s
                                AND T_S_ID = %s""" % (warehouseInfo[1][1], warehouseInfo[0]))

    cursor.execute(info_warehouse_quantity)
    info_warehouse_quantity = cursor.fetchone()

    print(info_warehouse_quantity)
    print("this is the info warehouse")

    if info_warehouse_quantity == None:
        return None

    if int(info_warehouse_quantity[0]) >= int(quantity):



        update_warehouse1 = ("""UPDATE To_stock SET Quantity = %(quantity)s
                            WHERE ID = %(ID)s""")

        new_quantity = int(info_warehouse_quantity[0]) - int(quantity)

        data_update = {
        'quantity': new_quantity,
        'ID' : warehouseInfo[1][1],
        }            
        
        cursor.execute(update_warehouse1, data_update)
        if type(warehouseInfo) == list:
            update_warehouse2 = ("""UPDATE To_stock SET Quantity = %(quantity)s
                            WHERE ID = %(ID)s""")

            new_quantity = int(warehouseInfo[2][2]) + int(quantity)
            print(new_quantity)
            print("THIS IS THE NEW QUANTITY WHICH WONT UPDATE")

            data_update = {
            'quantity': new_quantity,
            'ID' : warehouseInfo[2][1],
            }    

            result = cursor.execute(update_warehouse2, data_update)
        else:
            ads.setWarehouseStock(warehouseInfo[2], warehouseInfo[0], quantity)
            
    else:
        return "not enough quantity in source warehouse"



    settings.cnx.commit()
