import settings


"""
Obtain warehouse stock info 
"""

def getWarehouseByID(ID_user):
    cursor = settings.cnx.cursor()

    cursor.execute("""SELECT * FROM To_stock
                      WHERE ID = '%s'""" % ID_user)

    myuser = cursor.fetchone()
   # fetchone 
    print(myuser)  
    print("this is the getwarehousebyid value")

    if myuser == None:
        return ID_user
    

    return myuser

"""
Obtain all warehouses to see info for transfers
"""

def getAllWarehouseByID():
    cursor = settings.cnx.cursor()

    cursor.execute("""SELECT * FROM To_stock""")

    myuser = cursor.fetchall()

    if myuser == None:
        return None

    return myuser





"""
Get user by ID
"""

def getUserByID(ID_user):

    cursor = settings.cnx.cursor()

    cursor.execute("""SELECT * FROM User
                      WHERE ID = '%s'""" % ID_user)

    myuser = cursor.fetchone()
   # fetchone 
    print(myuser)  

    if myuser == None:
        return None
    
    #checks if user is customer or employee and return true if its customer and false if employee

    if myuser[14] == None:
        cursor.execute("""SELECT * FROM Employee
                            WHERE ID = '%s'""" % ID_user)
        customerInfo = cursor.fetchone()
        print(customerInfo)
    else:
        cursor.execute("""SELECT ID, VIP FROM Customer
                            WHERE U_C_ID = '%s'""" % ID_user)
        customerInfo = cursor.fetchone()
        print(customerInfo)

    # Create and return one list of 2 tuples  
    userInfo = []
    userInfo.append(myuser)
    userInfo.append(customerInfo)
    #OR
    #userInfo[0] = myuser
    #userInfo[1] = customerInfo

    print(userInfo)

    return userInfo

#getUserByID(5)

def getUserByEmailPassword(email, password):

    cursor = settings.cnx.cursor()

    cursor.execute("""SELECT * FROM User
                      WHERE email = '%s'
                      AND password = '%s'""" % (email, password))

    myuser = cursor.fetchone()
    #fetchone 
    #print(myuser)  
    

    #checks if input was valid
    if myuser == None:
        return None

    #checks if user is customer or employee and return true if its customer and false if employee

    if myuser[14] == None:
        cursor.execute("""SELECT * FROM Employee
                            WHERE ID = '%s'""" % myuser[0])
        customerInfo = cursor.fetchone()
        print(customerInfo)
    else:
        cursor.execute("""SELECT ID, VIP FROM Customer
                            WHERE U_C_ID = '%s'""" % myuser[0])
        customerInfo = cursor.fetchone()
        print(customerInfo)

    # Create and return one list of 2 tuples  
    userInfo = []
    userInfo.append(myuser)
    userInfo.append(customerInfo)
    #OR
    #userInfo[0] = myuser
    #userInfo[1] = customerInfo

    #print(userInfo)

    return userInfo



"""
Get all shoes in models
"""

def getShoesByModel():

    cursor = settings.cnx.cursor()

    cursor.execute("""SELECT * FROM Model""")

    myresult = cursor.fetchall()

    print(myresult)


"""
Get all shoes by sex
"""

def getShoesBySex(wantedS):

    cursor = settings.cnx.cursor()

    query = """SELECT * FROM Model
                WHERE To__Name = '%s'""" % wantedS 
                    
    cursor.execute(query)

    myresult = cursor.fetchall()

    print(myresult)


#getShoesBySex("men")
#getShoesBySex("unisex")

def getShoesByBrand(wantedBrand):
    
    cursor = settings.cnx.cursor()

    query = """SELECT * FROM Model
                WHERE To__Name_1 IN (SELECT Name FROM Line
                                    WHERE ID IN (SELECT ID FROM Brand
                                                WHERE Name = '%s'))""" % wantedBrand

    cursor.execute(query)

    myresult = cursor.fetchone()

    #for result in myresult:
    print(myresult)

#getShoesByBrand("asics")


def getShoesBySport(wantedSport):
    cursor = settings.cnx.cursor()

    query = """SELECT * FROM Model
                WHERE To__Name_1 IN (SELECT Name FROM Line
                                    WHERE To__ID IN (SELECT ID FROM Sport
                                                WHERE Name = '%s'))""" % wantedSport

    cursor.execute(query)

    myresult = cursor.fetchone()

    #for result in myresult:
    print(myresult)





def getShoesSize():
    cursor = settings.cnx.cursor()

    cursor.execute("""SELECT Size FROM Specification""")

    myresult = cursor.fetchone()

    print(myresult)


def getModelsBySize():
    cursor = settings.cnx.cursor()

    
    #cursor.execute("""SELECT * FROM Released
    #                  WHERE ID = (SELECT To__ID
    #                              FROM Specification)""")

    cursor.execute("""SELECT * FROM Model
                      WHERE To__Name IN (SELECT *
                                        FROM Categorie
                                        WHERE Name IN (SELECT *
                                                       FROM Released
                                                       WHERE Name = 'unisex'))""")

                                                       

    myresult = cursor.fetchall()
    for i in myresult:
        print(i)



def getSpecificationByModel():
    cursor = settings.cnx.cursor()

    
    #cursor.execute("""SELECT * FROM Released
    #                  WHERE ID = (SELECT To__ID
    #                              FROM Specification)""")

    cursor.execute("""SELECT * FROM Model
                      WHERE To__Name IN (SELECT *
                                        FROM Categorie
                                        WHERE Name IN (SELECT *
                                                       FROM Released
                                                       WHERE Name = 'unisex'))""")

                                                       

    myresult = cursor.fetchall()
    for i in myresult:
        print(i)



def getAllShoesSpecifications():
    cursor = settings.cnx.cursor()

    
    #cursor.execute("""SELECT * FROM Released
    #                  WHERE ID = (SELECT To__ID
    #                              FROM Specification)""")

    cursor.execute("""SELECT * FROM Specification, Released, Model
                      WHERE Specification.To__ID = Released.ID
                      AND Released.To__ID = Model.ID""")

                                                       

    myresult = cursor.fetchall()


    for i in myresult:
        print(i)


def printBySpecificationModel(result):
    print("ProductID       Model         Size      Color      Price       Gender        ShoeCode         Limited Edition        Line", end = ' ')
    for i in range(len(result)):
        print("\n")
        for j in range(len(result[i])):
            print("   ", end = ' ')
            print(result[i][j], end = '             ')



def findCartDetailByUserId(userID):
    cursor = settings.cnx.cursor()

    findCartDetail = ("""SELECT * FROM Cart_Detail
                      WHERE To__ID = %s""" % (userID))

    cursor.execute(findCartDetail)

    cartDetails = cursor.fetchall()

    if cartDetails == None:
        print("Your cart is empty!")
        return None

    cartDetailsList =  []
    for i in range(len(cartDetails)):
        cartDetailsList.append(cartDetails[i])

    return cartDetailsList



def findDetailById(detailId):
    cursor = settings.cnx.cursor()

    findDetail = ("""SELECT * FROM Detail
                      WHERE ID = %s""" % (detailId))

    cursor.execute(findDetail)

    cartDetails = cursor.fetchone()

    return cartDetails





