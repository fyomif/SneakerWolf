from json.tool import main
from logging import NullHandler
from pickle import TRUE
from venv import create
import mysql.connector
import datetime



#Function that allows to open and close the connection to the database
def establishConnection():


    cnx = mysql.connector.connect(user='admin', password='password',
                                host='127.0.0.1',
                                database='northwind3')
 

    return cnx

#ESTABLISHED CONNECTION AT START OF APP
cnx = establishConnection()

def setSport(sportString):



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
    cnx.commit()
    
    cursor.close()

    cnx.close()



def setBrand(brandString, foundingYear):

    cnx = mysql.connector.connect(user='admin', password='password',
                                host='127.0.0.1',
                                database='northwind')

    cursor = cnx.cursor()

    set_salary = ("INSERT INTO Brand "
                "(ID, Name, Founding_year) "
                "VALUES (%(ID)s, %(Name)s, %(Founding_year)s)")

    ID = cursor.lastrowid

    # Insert brand information
    data_salary = {
    'ID': ID,
    'Name': brandString,
    'Founding_year': foundingYear, 
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    cnx.commit()
    
    cursor.close()

    cnx.close()

    #returns the value of last generated primary key to be used in primary key of Line
    return ID 

def setLine(lineString, IdBrand, IdSport = "1"): #the 1 sets basketball as default value if no sport is given

    cnx = mysql.connector.connect(user='admin', password='password',
                                host='127.0.0.1',
                                database='northwind')

    cursor = cnx.cursor()

    set_salary = ("INSERT INTO Line "
                "(ID, Name, To__ID) "
                "VALUES (%(ID)s, %(Name)s, %(To__ID)s)")

    ID = cursor.lastrowid

    # Insert salary information
    data_salary = {
    'ID': IdBrand,
    'Name': lineString,
    'To__ID': IdSport,
    }
    cursor.execute(set_salary, data_salary)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()

    cnx.close()

def setModel(modelString, IdNameLine = "Airforce", IdLine = "1", IdCategorie = "femme"): #the 1 sets basketball as default value if no sport is given

    cnx = mysql.connector.connect(user='admin', password='password',
                                host='127.0.0.1',
                                database='northwind')

    cursor = cnx.cursor()

    set_model = ("""INSERT INTO Model 
                (ID, Name, To__Name, To__ID, To__Name_1) 
                VALUES (%(ID)s, %(Name)s,%(To__Name)s, %(To__ID)s, %(To__Name_1)s)""")

    ID = cursor.lastrowid

    # Insert salary information
    data_model = {
    'ID': ID,
    'Name': modelString,
    'To__Name': IdCategorie,
    'To__ID': IdLine,
    'To__Name_1': IdNameLine,
    }
    cursor.execute(set_model, data_model)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()

    cnx.close()



def setReleased(realaseDate, officalName, categorieName = "unisex", limitedEdition = False):

    cnx = mysql.connector.connect(user='admin', password='password',
                                host='127.0.0.1',
                                database='northwind')

    cursor = cnx.cursor()



    ID = cursor.lastrowid

    # Insert Sport information

    if limitedEdition == False:

        set_release = ("INSERT INTO Released"
            "(ID, Release_date, Official_name, Name) "
            "VALUES (%(ID)s,%(Release_date)s, %(Official_name)s, %(Name)s)")


        data_release = {
        'ID': ID,
        'Release_date': realaseDate,
        'Official_name': officalName,
        'Name': categorieName,
        }
    else:
        set_release = ("INSERT INTO Released"
        "(ID, Release_date, Official_name, Limited_edition, Name) "
            "VALUES (%(ID)s,%(Release_date)s, %(Official_name)s,%(Limited_edition)s,  %(Name)s)")


        data_release = {
        'ID': ID,
        'Release_date': realaseDate,
        'Official_name': officalName,
        'Limited_edition': limitedEdition,
        'Name': categorieName,
        }

    cursor.execute(set_release, data_release)

    # data is committed to the database
    cnx.commit()
    
    cursor.close()

    cnx.close()



def setSpecification(size, color, price, idReleased = "1"):

    cnx = mysql.connector.connect(user='admin', password='password',
                                host='127.0.0.1',
                                database='northwind')

    cursor = cnx.cursor()

    ID = cursor.lastrowid

    # Insert Sport information



    set_release = ("INSERT INTO Specification"
        "(ID, size, color, price, To__ID) "
        "VALUES (%(ID)s,%(Size)s, %(Color)s, %(Price)s, %(To__ID)s)")

    data_release = {
    'ID': ID,
    'Size': size,
    'Color': color,
    'Price': price,
    'To__ID': idReleased,
    }


    cursor.execute(set_release, data_release)

    # data is committed to the database
    cnx.commit()
    
    cursor.close()

    cnx.close()

#setLine(lineString, IdBrand, IdSport = "1")
#setModel(modelString, IdNameLine = "Airforce", IdLine = "1", IdCategorie = "femme"):
#def setReleased(realaseDate, officalName, categorieName = "unisex", limitedEdition = False):
#setSpecification(size, color, price, idReleased = "1"):
#def setShoe(size, color, price, releaseDate, officialName,modelString, lineString, IdBrand, categorieName = "unisex", limitedEdition = False, idReleased = "1", IdNameLine = "Airforce", IdLine = "1"):
    #IdCategorie = "femme" is euqal to categorieName
    

#setModel("AirForce1")
#setReleased(datetime.date(2022, 6, 14), "NWA256")
#setSpecification(7, "bleu", 140)


def setLineBrand():
    setBrand("Nike", datetime.date(1977, 6, 14))
    setLine("AirForce", 1)





def getShoesSize():
    cursor = cnx.cursor()

    cursor.execute("""SELECT Size FROM Specification""")

    myresult = cursor.fetchone()

    print(myresult)


def getModelsBySize():
    cursor = cnx.cursor()

    
    #cursor.execute("""SELECT * FROM Released
    #                  WHERE ID = (SELECT To__ID
    #                              FROM Specification)""")

    cursor.execute("""SELECT * FROM Model
                      WHERE To__Name IN (SELECT *
                                        FROM Categorie
                                        WHERE Name IN (SELECT *
                                                       FROM Released
                                                       WHERE Name = 'unisex'))""")

                                                       
                                        
    """(SELECT *
                    FROM Released
                    WHERE ID = (SELECT To__ID
                            FROM Specification)))"""

    myresult = cursor.fetchall()
    for i in myresult:
        print(i)





def createDetail(quantity, price, To__ID):

    cursor = cnx.cursor()
    
    query0 = ("INSERT INTO Detail"
               "(Quantity, Price, To__ID, Cart)"
               "VALUES (%(Quantity)s, %(Price)s, %(To__ID)s, %(Cart)s)")

    data_detail = {
    'Quantity': quantity,
    'Price': price,
    'To__ID' : To__ID,
    'Cart' : 1,
    }
    cursor.execute(query0, data_detail)

    ID = cursor.lastrowid
    ID_D_C = ID

    myresult = cursor.fetchall()
    print(myresult)

    query1 = ("INSERT INTO Cart"
               "(ID, D_C_ID)"
               "VALUES (%(ID)s, %(D_C_ID)s)")

    ID = cursor.lastrowid

    data_detail = {
    'ID': ID,
    'D_C_ID' : ID_D_C,
    }

    cursor.execute(query1, data_detail)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()

    cnx.close()

#createDetail(0, 0, 3)





#createCart(0)









def setSport(sportString):
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
    cnx.commit()
    cursor.close()
    cnx.close()

#getShoes()
#getShoesSize()
#getModelsBySize()




############################################ UPDATES

def updateUserInfo(ID_user, Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street ,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country, VIP = 0):

    #the return is true if 
    customer = getUserByID(ID_user)








############################################ SETTERS


"""
CREATE A CUSTOMER
"""

def subscribeCustomer(Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street ,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country, VIP = 0):


    """needs to generate foreign key before so it first creates a cart, assigns it to a created user and then puts it in the customer table"""
    cursor = cnx.cursor()
   
    query = ("INSERT INTO User "
                "(Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country, delivery_add_Street,delivery_add_Number, delivery_add_Postal_code, delivery_add_City, delivery_add_Country, Customer) "
                "VALUES (%(Name)s,%(Surname)s, %(billing_add_Street)s, %(billing_add_Number)s, %(billing_add_Postal_code)s, %(billing_add_City)s, %(billing_add_Country)s, %(delivery_add_Street)s, %(delivery_add_Number)s, %(delivery_add_Postal_code)s, %(delivery_add_City)s, %(delivery_add_Country)s, %(Customer)s)")

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
    cnx.commit()

    cursor.close()

    #cnx.close()

    return ID_user

##subscribeCustomer("barack", "obama", "white house", "1", "1000", "Washington DC", "USA", "white house", "1", "1000", "Washington DC", "USA", 1)


def createCart(detailId, userID, commitVal):

    cursor = cnx.cursor()
    
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

        cnx.commit()

        cursor.close()

        #cnx.close()



def addShoeToCart(quantity, price, to__specification, userID):
    cursor = cnx.cursor()


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
    cnx.commit()
    cursor.close()
    #cnx.close()


##addShoeToCart(1, 130, 1)








############################################ OBSERVERS


"""
Get user by ID
"""

def getUserByID(ID_user):

    cursor = cnx.cursor()

    cursor.execute("""SELECT * FROM User
                      WHERE ID = '%s'""" % ID_user)

    myuser = cursor.fetchone()
   # fetchone 
    print(myuser)  
    
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


    userInfo = []
    userInfo.append(myuser)
    userInfo.append(customerInfo)

    print(userInfo)

    return customerInfo

getUserByID(5)


    







"""
Get all shoes in models
"""

def getShoesByModel():

    cursor = cnx.cursor()

    cursor.execute("""SELECT * FROM Model""")

    myresult = cursor.fetchall()

    print(myresult)


"""
Get all shoes by sex
"""

def getShoesBySex(wantedS):

    cursor = cnx.cursor()

    query = """SELECT * FROM Model
                WHERE To__Name = '%s'""" % wantedS 
                    
    cursor.execute(query)

    myresult = cursor.fetchall()

    print(myresult)


#getShoesBySex("men")
#getShoesBySex("unisex")

def getShoesByBrand(wantedBrand):
    
    cursor = cnx.cursor()

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
    cursor = cnx.cursor()

    query = """SELECT * FROM Model
                WHERE To__Name_1 IN (SELECT Name FROM Line
                                    WHERE To__ID IN (SELECT ID FROM Sport
                                                WHERE Name = '%s'))""" % wantedSport

    cursor.execute(query)

    myresult = cursor.fetchone()

    #for result in myresult:
    print(myresult)

#getShoesBySport("running")



#First Main attempt 

def Main():

    #opens conection to database

    print("""Welcome to the SneakerWolf Website!\nWe sell shoes of all kinds but first you\nHave to make an account!""")
    returningCustomer = input("Are you a returning customer? Yes/No ")


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
            vipYesNo = input("""Are you sure we have some pretty dope stuff in the back? ಠ__ಠ\nYes I've changed my mind/No""")
            if vipYesNo == "Yes":
                vipYesNo = 1
            else:
                vipYesNo = 0

        ID_user = subscribeCustomer(name, surname, billing_street, billing_number, billing_street, billing_number, billing_postCode, delivery_street, delivery_number, billing_postCode, billing_city, billing_country, vipYesNo)
        print("Your customer id is %d, don't forget it you'll need it to log in!" % ID_user)
    #Name, Surname, billing_add_Street,billing_add_Number, billing_add_Postal_code, billing_add_City, billing_add_Country

    while (True):
        print("What would you like to access?")

        choice = input("enter 1 to see all models, enter 2 to search by sport, enter 3 to searh by gender category or 4 to look by brand")

        choice = int(choice)
        if choice == 1:
            getShoesByModel()
        elif choice == 2:
            ####need to add input for sport choice
            getShoesBySport("running")
        elif choice == 3:
            wantedS = input("Choose men, women, unisex or child")
            getShoesBySex(wantedS)
        elif choice == 4:
            ####we need to make a select here on only the brands istead of a print
            wantedBrand = input("We have nike, asics and adidas")
            getShoesByBrand(wantedBrand)
        else:
            print("invalid input please try again")


    cnx.close()

Main()
