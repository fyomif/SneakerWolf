import email
import settings
import observers as obs
import time

"""
CREATE A CUSTOMER
"""

def subscribeCustomer(Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street ,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country, email, password, VIP = 0):


    """needs to generate foreign key before so it first creates a cart, assigns it to a created user and then puts it in the customer table"""
    cursor = settings.cnx.cursor()
   
    query = ("INSERT INTO User "
                "(Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country, Customer, email, password) "
                "VALUES (%(Name)s,%(Surname)s, %(billing_add_Street)s, %(billing_add_Number)s, %(billing_add_Postal_code)s, %(billing_add_City)s, %(billing_add_Country)s, %(delivery_add_Street)s, %(delivery_add_Number)s, %(delivery_add_Postal_code)s, %(delivery_add_City)s, %(delivery_add_Country)s, %(Customer)s,%(email)s, %(password)s)")

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
    'email' : email,
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

    check_stock = ("""SELECT quantity FROM To_stock
                      WHERE T_S_ID = %s
                      AND quantity >= %s""" % (specificationId, quantity))

                      

    cursor.execute(check_stock)
    
    quantityCheck = cursor.fetchone()

    if quantityCheck == None:
        print(specificationId)
        print("sadly we don't have enough stock")
        return None

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
    


def addOrder(userID, date = time.strftime('%Y-%m-%d')):
    cursor = settings.cnx.cursor()
    
    query0 = ("INSERT INTO Ordered"
               "(date, ID)"
               "VALUES (%(date)s, %(ID)s)")

    data_cart = {
    'date' : date,
    'ID' : userID,
    }

    cursor.execute(query0, data_cart)

    orderNumber = cursor.lastrowid

    # Make sure data is committed to the database

    settings.cnx.commit()

    cursor.close()

    return orderNumber

    #settings.cnx.close()


def addOrderDetailToOrder(userID, preFab = False, date = time.strftime('%Y-%m-%d')):
    cursor = settings.cnx.cursor()

    cartDetails = obs.findCartDetailByUserId(userID, preFab)
    
    if cartDetails == None:
        return None
    
    #create order to assosiate the orderedDetails to 
    orderNumber = addOrder(userID, date)

    for cartDetailsTuple in cartDetails:
        

        #deletes cart_detail for exact-1 constraint
        query1 = ("""DELETE FROM Cart_Detail
                    WHERE D_C_ID = %s""" % (cartDetailsTuple[2]))

        cursor.execute(query1)
        

        #due to exact-1 constraint you can't update the bool val of orderedDetail
        #or cartDetail without violating the constraint one way or another
        #so this requires a temporary suppresion of the row and a 
        #re-injection with the same data except for the orderedDetail value
        tupleCpyDetail = obs.findDetailById(cartDetailsTuple[2])

        query2 = ("""DELETE FROM Detail
                    WHERE ID = %s""" % (cartDetailsTuple[2]))

        cursor.execute(query2)

        

        #update details for exact-1 contraint
        query3 = ("INSERT INTO Detail"
                "(ID, Quantity, To__ID, Ordered_Detail)"
                "VALUES (%(ID)s, %(Quantity)s, %(To__ID)s, %(Ordered_Detail)s)")


        data_ordered = {
        'ID' : tupleCpyDetail[0],
        'Quantity' : tupleCpyDetail[1],
        'To__ID' : tupleCpyDetail[2],
        'Ordered_Detail' : 1,
        }
        
        cursor.execute(query3, data_ordered)


        #ads order detail from cart to order
        query4 = ("INSERT INTO Ordered_Detail"
                "(D_O_ID, Status, Order_Number)"
                "VALUES (%(D_O_ID)s, %(Status)s, %(Order_Number)s)")


        data_ordered = {
        'D_O_ID' : cartDetailsTuple[2],
        'Status' : 'p',
        'Order_Number' : orderNumber,
        }

        cursor.execute(query4, data_ordered)
        settings.cnx.commit()


    # Make sure data is committed to the database

    

    cursor.close()

    #settings.cnx.close()

    


def returnShoes(specificationId, userId, orderNumber):

    cursor = settings.cnx.cursor()


    query0 = ("""SELECT * FROM Detail
                WHERE To__ID = %s
                AND ID IN (SELECT D_O_ID FROM Ordered_Detail
                           WHERE Order_Number in (SELECT Order_Number FROM Ordered
                                                  WHERE ID = %s
                                                  AND Order_Number = %s))""" % (specificationId, userId, orderNumber))

    cursor.execute(query0)

    orderedDetails = cursor.fetchone()

    if orderedDetails == None:
        print("It doesn't seem like you've ordered this shoe before\nAre you sure it's the right shoes id?")
        return None


    query1 = ("INSERT INTO Demand_Return"
               "(Type, start_date, To_realize_ID, To_concern_ID)"
               "VALUES (%(Type)s, %(start_date)s, %(To_realize_ID)s, %(To_concern_ID)s)")

    data_return = {
    'Type' : 'Defective exchange',
    'start_date' :  time.strftime('%Y-%m-%d'),
    'To_realize_ID' : userId,
    'To_concern_ID' : orderedDetails[0], 
    }

    cursor.execute(query1, data_return)

    # Make sure data is committed to the database

    settings.cnx.commit()

    cursor.close()

    return "done"



def sendOrders(userId, servicePorviderId):
    cursor = settings.cnx.cursor()


    query0 = ("""SELECT * FROM Detail
                WHERE Ordered_Detail = 1
                AND ID not in (SELECT T_D_ID FROM To_serve)""")

    cursor.execute(query0)

    detailsToDeliver = cursor.fetchall()
    

    if len(detailsToDeliver) == 0 and userId != -1:
        print("No pending orders to deliver \n")
        return None

    for details in detailsToDeliver:

        query1 = ("""SELECT ts.ID, ts.quantity FROM Warehouse as w, To_stock as ts
                     WHERE w.ID = ts.ID  
                     AND ts.T_S_ID = %s
                     AND ts.quantity >= %s""" % (details[2], details[1]))

        cursor.execute(query1)

        warehouseInfo = cursor.fetchone()

        if (warehouseInfo == None):
            print("We need to order more of product number %s to fullfill order!" % details[2])
            continue

        query2 = ("INSERT INTO To_serve"
                "(T_D_ID, ID, T_P_ID)"
                "VALUES (%(T_D_ID)s, %(ID)s, %(T_P_ID)s)")

        data_delivery = {
        'T_D_ID' : details[0],
        'ID' :  warehouseInfo[0],
        'T_P_ID' : servicePorviderId,
        }

        cursor.execute(query2, data_delivery)

        query3 = ("""UPDATE To_stock set quantity = quantity - %s
                     WHERE T_S_ID = %s
                     AND ID = %s""" % (int(details[1]), details[2], warehouseInfo[0]))


        cursor.execute(query3, data_delivery)

        query4 = ("""UPDATE Ordered_Detail set Status = "d"
                     WHERE D_O_ID = %s""" % (details[0]))

        cursor.execute(query4)
        

    # Make sure data is committed to the database

    settings.cnx.commit()

    cursor.close()


    