import settings
import prettytable as pt


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
    #fetchone 
    #print(myuser)  

    if myuser == None:
        return None

    tableFormat = pt.PrettyTable(["Name", "Surname", "billing Street", "Number", "Post code", "city", "country", "email"])
    tableFormat0 = pt.PrettyTable(["delivery Street", "d Number", "d Post code", "d city"])

    tmpList = []
    for j in range(1, 8):
        tmpList.append(myuser[j])
    tmpList.append(myuser[13])
    tableFormat.add_row(tmpList)
    print(tableFormat)

    tmpList = []
    for j in range(8, 12):
        tmpList.append(myuser[j])

    tableFormat0.add_row(tmpList)
    print(tableFormat0)
    
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
        tableFormat1 = pt.PrettyTable(["VIP"])
        tmpList = []
        if customerInfo[1] == '0':
            tmpList.append(False)
        else:
            tmpList.append(True)
        tableFormat1.add_row(tmpList)
        print(tableFormat1)
        #print(customerInfo)

    # Create and return one list of 2 tuples  
    userInfo = []
    userInfo.append(myuser)
    userInfo.append(customerInfo)
    #OR
    #userInfo[0] = myuser
    #userInfo[1] = customerInfo

    #print(userInfo)

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
        #print(customerInfo)
    else:
        cursor.execute("""SELECT ID, VIP FROM Customer
                            WHERE U_C_ID = '%s'""" % myuser[0])
        customerInfo = cursor.fetchone()
        #print(customerInfo)

    # Create and return one list of 2 tuples  
    userInfo = []
    userInfo.append(myuser)
    userInfo.append(customerInfo)

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
                WHERE Name = '%s'""" % wantedS 
                    
    cursor.execute(query)

    myresult = cursor.fetchall()

    tableFormat = pt.PrettyTable(["ID", "Name", "Sex", "Line"])
 
    for indexSubList in range(len(myresult)):
        #print("\n")
        toPrint = [0, 1, 2, 4]
        tmpList = []
        for j in toPrint:
            tmpList.append(myresult[indexSubList][j])
        tableFormat.add_row(tmpList)
    print(tableFormat)
    #print(myresult)


#getShoesBySex("men")
#getShoesBySex("unisex")

def getShoesByBrand(wantedBrand):
    
    cursor = settings.cnx.cursor()

    query = """SELECT * FROM Model
                WHERE To__Name IN (SELECT Name FROM Line
                                    WHERE ID IN (SELECT ID FROM Brand
                                                WHERE Name = '%s'))""" % wantedBrand

    cursor.execute(query)

    myresult = cursor.fetchall()

    tableFormat = pt.PrettyTable(["ID", "Name", "Sex", "Line"])
 
    for indexSubList in range(len(myresult)):
        #print("\n")
        toPrint = [0, 1, 2, 4]
        tmpList = []
        for j in toPrint:
            tmpList.append(myresult[indexSubList][j])
        tableFormat.add_row(tmpList)
    print(tableFormat)

    #for result in myresult:
    #print(myresult)

#getShoesByBrand("asics")


def getSport():
    cursor = settings.cnx.cursor()

    query = """SELECT * FROM Sport""" 

    cursor.execute(query)

    myresult = cursor.fetchall()


    tableFormat = pt.PrettyTable(["Sport"])
    
    for SubList in myresult:
        tmpList = []
        tmpList.append(SubList[1])
        tableFormat.add_row(tmpList)
    print(tableFormat)

def getShoesBySport(wantedSport):
    cursor = settings.cnx.cursor()

    query = """SELECT * FROM Model
                WHERE To__Name IN (SELECT Name FROM Line
                                    WHERE To__ID IN (SELECT ID FROM Sport
                                                    WHERE Name = '%s'))""" % wantedSport

    cursor.execute(query)

    myresult = cursor.fetchall()

    tableFormat = pt.PrettyTable(["ID", "Name", "Sex", "Line"])
 
    for indexSubList in range(len(myresult)):
        #print("\n")
        toPrint = [0, 1, 2, 4]
        tmpList = []
        for j in toPrint:
            tmpList.append(myresult[indexSubList][j])
        tableFormat.add_row(tmpList)
    print(tableFormat)

    #for result in myresult:
    #print(myresult)





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
                                                       FROM Released))""")

                                                       

    myresult = cursor.fetchall()
    for i in myresult:
        print(i)

def getModelBySpecification(specificationId):
    cursor = settings.cnx.cursor()

    print(specificationId)
    cursor.execute("""SELECT * FROM Specification, Released, Model
                      WHERE Specification.To__ID = Released.ID
                      AND Released.To__ID = Model.ID
                      AND Specification.ID = %s"""%specificationId)                       

    myresult = cursor.fetchone()

    toPrint = [0, 11, 1, 2, 3, 12, 13, 6, 7]
    tmpList = []
    for j in toPrint:
        tmpList.append(myresult[j])
    
 
    if myresult == None:
        return None
    
    return tmpList


def getAllShoesSpecifications():
    cursor = settings.cnx.cursor()

    
    #cursor.execute("""SELECT * FROM Released
    #                  WHERE ID = (SELECT To__ID
    #                              FROM Specification)""")

    cursor.execute("""SELECT * FROM Specification, Released, Model
                      WHERE Specification.To__ID = Released.ID
                      AND Released.To__ID = Model.ID""")

                                                       

    myresult = cursor.fetchall()

    tableFormat = pt.PrettyTable(["ID", "Name", "Sizes", "Color", "Price", "Sex", "Line", "Release Date", "Offical code"])
 
    for indexSubList in range(len(myresult)):
        #print("\n")
        toPrint = [0, 11, 1, 2, 3, 12, 13, 6, 7]
        tmpList = []
        for j in toPrint:
            tmpList.append(myresult[indexSubList][j])

            #print("   ", end = '')
            #print(subList[j], end = '     ')
        tableFormat.add_row(tmpList)
    print(tableFormat)


def printBySpecificationModel(result):
    print("ProductID       Model         Size      Color      Price       Gender        ShoeCode         Limited Edition        Line", end = ' ')
    for i in range(len(result)):
        print("\n")
        for j in range(len(result[i])):
            print("   ", end = ' ')
            print(result[i][j], end = '             ')



def findCartDetailByUserId(userID):
    cursor = settings.cnx.cursor()

    findCartDetail = ("""SELECT To__ID, quantity FROM Detail
                      WHERE ID in (SELECT D_C_ID FROM Cart_Detail
                                   Where To__ID in (SELECT ID FROM User
                                                    WHERE ID = %s))""" % (userID))

    cursor.execute(findCartDetail)

    cartDetails = cursor.fetchall()

    print(cartDetails)
    if cartDetails == None:
        print("Your cart is empty!")
        return None


    tableFormat = pt.PrettyTable(["ID", "Name", "Sizes", "Color", "Price", "Sex", "Line", "Release Date", "Offical code", "quantity", "Total per Model"])
    
    for specificationId in cartDetails:
        print(specificationId[0])
        tmpList = getModelBySpecification(specificationId[0])
        tmpList.append(specificationId[1])
        tmpList.append(int(tmpList[4]*int(tmpList[-1])))
        tableFormat.add_row(tmpList)

    #print("\n")
    


    print(tableFormat)
    #return cartDetailsList



def findDetailById(detailId):
    cursor = settings.cnx.cursor()

    findDetail = ("""SELECT * FROM Detail
                      WHERE ID = %s""" % (detailId))

    cursor.execute(findDetail)

    cartDetails = cursor.fetchone()

    return cartDetails





