import settings
import observers as obs

"""
CREATE A CUSTOMER
"""

def subscribeCustomer(Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street ,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country, username, password, VIP = 0):


    """needs to generate foreign key before so it first creates a cart, assigns it to a created user and then puts it in the customer table"""
    cursor = settings.cnx.cursor()
   
    query = ("INSERT INTO User "
                "(Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country, Customer, username, password) "
                "VALUES (%(Name)s,%(Surname)s, %(billing_add_Street)s, %(billing_add_Number)s, %(billing_add_Postal_code)s, %(billing_add_City)s, %(billing_add_Country)s, %(delivery_add_Street)s, %(delivery_add_Number)s, %(delivery_add_Postal_code)s, %(delivery_add_City)s, %(delivery_add_Country)s, %(Customer)s,%(username)s, %(password)s)")

    # Insert salary information
    # if (customerBool == False):  
    data_user = {
    'Name': Name,
    'Surname': Surname,
    'billing_add_Street': billing_add_Street,
    'billing_add_Number': billing_add_Number,
    'billing_add_Postal_code': billing_add_Postal_code,
    'billing_add_City': billing_add_City,
    'billing_add_Country': billing_add_Country,
    'delivery_add_Street': delivery_add_Street,
    'delivery_add_Number': delivery_add_Number,
    'delivery_add_Postal_code': delivery_add_Postal_code,
    'delivery_add_City': delivery_add_City,
    'delivery_add_Country': delivery_add_Country,
    'Customer' : 1,
    'username' : username,
    'password' : password,
    }

    cursor.execute(query, data_user)
    ID_user = cursor.lastrowid

    query1 = ("INSERT INTO Customer"
               "(U_C_ID, VIP)"
               "VALUES (%(U_C_ID)s,  %(VIP)s)")

    data_user1 = {
    'U_C_ID': ID_user,
    'VIP': VIP,
    }

    cursor.execute(query1, data_user1)

    # Make sure data is committed to the database
    settings.cnx.commit()

    cursor.close()

    #settings.cnx.close()

    return ID_user

##subscribeCustomer("barack", "obama", "white house", "1", "1000", "Washington DC", "USA", "white house", "1", "1000", "Washington DC", "USA", 1)






def addShoeToCart(quantity, price, to__specification, userID):
    cursor = settings.cnx.cursor()


    #adds a row into detial
    set_detail = ("INSERT INTO Detail "
                "(Quantity, Price, To__ID, Cart_Detail) "
                "VALUES (%(Quantity)s, %(Price)s, %(To__ID)s, %(Cart_Detail)s)")

 
    # Insert Sport information
    data_detail = {
    'Quantity' :quantity,
    'Price' : price,
    'To__ID' : to__specification,
    'Cart_Detail' : 1,
    }
    #puts the information into the row
    cursor.execute(set_detail, data_detail)
    #sets the integer of the last row of the last table it was inserted to
    ID_detail = cursor.lastrowid


    #adds the detail created to a cart detail
    #userID is int of user placing in cart
    #ID_detail is the last row int of the detail table
    #Last boolean is to determin if the function is called by itself or in combination to deactivate the premature commits
    createCart(ID_detail, userID, False)

    # data is committed to the database
    settings.cnx.commit()
    cursor.close()
    #settings.cnx.close()


def setWarehouseStock(warehouseID, productId, quantity):

    cursor = settings.cnx.cursor()
    set_salary = ("INSERT INTO To_stock "
                "(T_S_ID, ID, Quantity) "
                "VALUES (%(T_S_ID)s, %(ID)s, %(Quantity)s)")
    ID = cursor.lastrowid
    # Insert Sport information
    data_salary = {
    'T_S_ID' : productId,
    'ID': warehouseID,
    'Quantity': quantity,
    }
    cursor.execute(set_salary, data_salary)
    # data is committed to the database
    settings.cnx.commit()



def setSport(sportString):
    cursor = settings.cnx.cursor()
    set_salary = ("INSERT INTO Sport "
                "(ID, Name) "
                "VALUES (%(ID)s, %(Name)s)")
    ID = cursor.lastrowid
    # Insert Sport information
    data_salary = {
    'ID': ID,
    'Name': sportString,
    }
    cursor.execute(set_salary, data_salary)
    # data is committed to the database
    settings.cnx.commit()
    cursor.close()
    #settings.cnx.close()




def createDetail(quantity, specificationId, userId):

    cursor = settings.cnx.cursor()
    
    query0 = ("INSERT INTO Detail"
               "(Quantity, To__ID, Cart_Detail)"
               "VALUES (%(Quantity)s, %(To__ID)s, %(Cart_Detail)s)")

    data_detail = {
    'Quantity': quantity,
    'To__ID' : specificationId,
    'Cart_Detail' : 1,
    }
    cursor.execute(query0, data_detail)

    ID = cursor.lastrowid
    ID_D_C = ID


    query1 = ("INSERT INTO Cart_Detail"
               "(ID, D_C_ID, To__ID)"
               "VALUES (%(ID)s, %(D_C_ID)s, %(To__ID)s)")

    ID = cursor.lastrowid

    data_detail = {
    'ID': ID,
    'D_C_ID' : ID_D_C,
    'To__ID' : userId,
    }

    cursor.execute(query1, data_detail)

    # Make sure data is committed to the database
    settings.cnx.commit()

    cursor.close()

    #settings.cnx.close()


def createCart(detailId, userID, commitVal):

    cursor = settings.cnx.cursor()
    
    query0 = ("INSERT INTO Cart_Detail"
               "(D_C_ID, To__ID)"
               "VALUES (%(D_C_ID)s, %(To__ID)s)")

    ID = cursor.lastrowid

    data_cart = {
    'D_C_ID' : detailId,
    'To__ID' : userID,
    }

    cursor.execute(query0, data_cart)

    # Make sure data is committed to the database

    if commitVal == True:

        settings.cnx.commit()

        cursor.close()

        #settings.cnx.close()



def addToCart(quantity,To__ID, To__ID_User):

    createDetail(quantity, To__ID, To__ID_User)
    

    
