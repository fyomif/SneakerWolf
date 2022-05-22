import settings 
import adders as ads

################
def setEmployee(nb,nationalReg,birthday,title,toWork,supervisor):       #supervisor est facultatif  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Employee "
                "(Personnal_number,ID,National_register ,Birthday,Title,To_work_ID,Supervisor_) "
                "VALUES (%(Personnal_number)s,%(ID)s, %(National_register)s,%(Birthday)s,%(Title)s,%(To_work_ID)s,%(Supervisor_)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'Personnal_number': ID,
    'National_register': nationalReg,
    'Birthday': birthday,
    'Title': title,
    'To_work_ID': toWork,
    'Supervisor_': supervisor,
    
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()




def setUser(name,Surname,billingSt,billingN,billingPc,billingCity,billingCou,deliverySt,deliveryN,deliveryPc,deliveryCity,deliveryCou):   

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO User "
                "(Name,Surname,billing_add_Street,billing_add_Number,billing_add_Postal_code,billing_add_City,billing_add_Country,delivery_add_Street,delivery_add_Number,delivery_add_Postal_code,delivery_add_City,delivery_add_Country) "
                "VALUES (%(Name)s,%(Surname)s,%(billing_add_Street)s,%(billing_add_Number)s,%(billing_add_Postal_code)s,%(billing_add_City)s,%(billing_add_Country)s, %(delivery_add_Street)s,%(delivery_add_Number)s,%(delivery_add_Postal_code)s,%(delivery_add_City)s,%(delivery_add_Country)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'Name': name,
    'Surname':Surname,
    'billing_add_Street' : billingSt,
    'billing_add_Number' : billingN,
    'billing_add_Postal_code' : billingPc,
    'billing_add_City' : billingCity,
    'billing_add_Country' : billingCou,
    'delivery_add_Street' : deliverySt,
    'delivery_add_Number' : deliveryN,
    'delivery_add_Postal_code' : deliveryPc,
    'delivery_add_City' : deliveryCity,
    'delivery_add_Country' : deliveryCou
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    
    cursor.close()

    



def setDemand(tpe,startD,toRId,toCId):  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Demand_Return "
                "(Type ,start_date,To_realize_ID,To_concern_ID) "
                "VALUES ( %(Type)s,%(start_date)s,%(To_realize_ID)s,%(To_concern_ID)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'Type': tpe,
    'start_date': startD,
    'To_realize_ID': toRId,
    'To_concern_ID': toDId
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database

    
    cursor.close()

    


def setCart(doId,toId):  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Cart_Detail "
                "(ID, D_C_ID,To__ID) "
                "VALUES (%(ID)s, %(D_C_ID)s,%(Status)s,%(To__ID)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'D_C_ID': doID,
    'To__ID': toId
    }
    cursor.execute(set_salary, data_salary)
    settings.cnx.commit()
    # data is committed to the database
    
    cursor.close()

    




def setOrdered(doId,status,toId):  


    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Ordered_Detail "
                "(ID, D_O_ID,Status,To__ID) "
                "VALUES (%(ID)s, %(D_O_ID)s,%(Status)s,%(To__ID)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'D_O_ID': doID,
    'Status': status,
    'To__ID': toId
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()

    



def setParcelService(name):  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Parcel_Service "
                "(ID, Name) "
                "VALUES (%(ID)s, %(Name)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'Name': name
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()

    



def setDetail(quantity,price,toId):  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Detail "
                "(ID, Quantity,Price,To__ID) "
                "VALUES (%(ID)s, %(Quantity)s,%(Price)s,%(To__ID)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'Quantity': quantity,
    'Price':price,
    'To__ID' : toId
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()

    


def setWarehouse(name,surface,locationSt,locationN,locationPc,locationCity,locationCou):   

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Warehouse "
                "(ID, Name,Surface_area,location_Street,location_Number,location_Postal_code,location_City,location_Country) "
                "VALUES (%(ID)s, %(Name)s,%(Surface_area)s,%(location_Street)s,%(location_Number)s,%(location_Postal_code)s,%(location_City)s,%(location_Country)s )")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'Name': name,
    'Surface_area':surface,
    'location_Street' : locationSt,
    'location_Number' : locationN,
    'location_Postal_code' : locationPc,
    'location_City' : locationCity,
    'location_Country' : locationCou,
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()

    
def setToStock(specificationId, warehouseId, quantity):  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO To_stock "
                "(T_S_ID, ID , Quantity) "
                "VALUES (%(T_S_ID)s, %(ID)s, %(Quantity)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'T_S_ID': specificationId,
    'ID': warehouseId,
    'Quantity': quantity
    }
    cursor.execute(set_salary, data_salary)

    settings.cnx.commit()
    # data is committed to the database
    
    cursor.close()


def setDepartement(name,typeDep):  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Department "
                "(ID, Name,Type_Departement) "
                "VALUES (%(ID)s, %(Name)s,%(Type_Departement)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'Name': name,
    'Type_Departement':typeDep
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()

    



def setStore(name,addressSt,addressN,addressPc,addressCity,addressCou):  

    cursor = settings.cnx.cursor()

    set_salary = ("INSERT INTO Store "
                "(ID, Name,addressStore_Street,addressStore_Number,addressStore_Postal_code,addressStore_City,addressStore_Country) "
                "VALUES (%(ID)s, %(Name)s,%(addressStore_Street)s,%(addressStore_Number)s,%(addressStore_Postal_code)s,%(addressStore_City)s,%(addressStore_Country)s)")

    ID = cursor.lastrowid

    # Insert Sport information
    data_salary = {
    'ID': ID,
    'Name': name,
    'addressStore_Street':addressSt,
    'addressStore_Number':addressN,
    'addressStore_Postal_code':addressPc,
    'addressStore_City':addressCity,
    'addressStore_Country':addressCou,
    }
    cursor.execute(set_salary, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()



def setBrand(brandString, foundingYear):

    cursor = settings.cnx.cursor()

    set_brand = ("INSERT INTO Brand "
                "(Name, Founding_year) "
                "VALUES (%(Name)s, %(Founding_year)s)")

    ID = cursor.lastrowid

    # Insert brand information
    data_salary = {
    'Name': brandString,
    'Founding_year': foundingYear, 
    }
    cursor.execute(set_brand, data_salary)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()

    #returns the value of last generated primary key to be used in primary key of Line
    return ID 

def setLine(lineString, IdBrand, IdSport = "1"): #the 1 sets basketball as default value if no sport is given

    cursor = settings.cnx.cursor()

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
    settings.cnx.commit()

    cursor.close()

    

def setModel(modelString,IdCategorie = "women", IdLine = "1", IdNameLine = "Airforce"): #the 1 sets basketball as default value if no sport is given

    cursor = settings.cnx.cursor()  

    set_model = ("""INSERT INTO Model 
                (ModelName, Name, To__ID, To__Name) 
                VALUES (%(ModelName)s,%(Name)s, %(To__ID)s, %(To__Name)s)""")

    # Insert salary information
    data_model = {
    'ModelName': modelString,
    'Name': IdCategorie,
    'To__ID': IdLine,
    'To__Name': IdNameLine,
    }
    cursor.execute(set_model, data_model)

    # Make sure data is committed to the database
    settings.cnx.commit()

    cursor.close()




def setReleased(realaseDate, officalName, limitedEdition, modelId):

    cursor = settings.cnx.cursor()

    # Insert Sport information

    if limitedEdition == False:

        set_release = ("INSERT INTO Released"
            "(Release_date, Official_name, Limited_edition, To__ID) "
            "VALUES (%(Release_date)s,%(Official_name)s, %(Limited_edition)s, %(To__ID)s)")


        data_release = {
        'Release_date': realaseDate,
        'Official_name': officalName,
        'Limited_edition': 0,
        'To__ID': modelId,
        }
    else:
        set_release = ("INSERT INTO Released"
        "(Release_date, Official_name, Limited_edition, To__ID) "
        "VALUES (%(Release_date)s,%(Official_name)s, %(Limited_edition)s, %(To__ID)s)")


        data_release = {
        'Release_date': realaseDate,
        'Official_name': officalName,
        'Limited_edition': 1,
        'To__ID': modelId,
        }

    cursor.execute(set_release, data_release)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()



def setSpecification(size, color, price, ReleaseID):

    cursor = settings.cnx.cursor()


    set_release = ("INSERT INTO Specification"
        "(size, color, price, To__ID) "
        "VALUES (%(Size)s, %(Color)s, %(Price)s, %(To__ID)s)")

    data_release = {
    'Size': size,
    'Color': color,
    'Price': price,
    'To__ID': ReleaseID,
    }


    cursor.execute(set_release, data_release)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()



    cursor.execute(set_release, data_release)

    # data is committed to the database
    settings.cnx.commit()
    
    cursor.close()




def getShoesSize():
    cursor = settings.cnx.cursor()

    cursor.execute("""SELECT Size FROM Specification""")

    myresult = cursor.fetchone()

    print(myresult)



def createDetail(quantity, price, To__ID):

    cursor = settings.cnx.cursor()
    
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
    settings.cnx.commit()

    cursor.close()

    
def setCategorie(genderCat):

    cursor = settings.cnx.cursor()
    set_gender = ("INSERT INTO Categorie "
                "(Name) "
                "VALUES (%(Name)s)")
                
    # Insert Sport information
    data_gender = {
    'Name': genderCat,
    }
    cursor.execute(set_gender, data_gender)
    # data is committed to the database
    settings.cnx.commit()
    cursor.close()




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

#getShoes()
#getShoesSize()
#getModelsBySize()



"""

#   def setEmployee(nb,nationalReg,birthday,title,toWork,supervisor):
setEmployee(1,"20011998123",20011998,"AAA",11,False)
setEmployee(2,"20011998444",20011998,"BBB",11,False)
setEmployee(3,"20011998357",20011998,"CCC",11,False)
setEmployee(4,"20011998768",20011998,"DDD",11,False)
setEmployee(5,"20011998978",20011998,"EEE",11,False)
setEmployee(6,"20011998499",20011998,"FFF",11,False)


#   def setUser(name,surname,billingSt,billingN,billingPc,billingCity,billingCou,deliverySt,deliveryN,deliveryPc,deliveryCity,deliveryCou): 
setUser("Dupont","Paul","JohnF",22,9855,"Namur","Belgique","GeorgeB",11,9655,"Liege","Belgique")
setUser("Herve","Jean","Saint Pierre",15,9655,"Namur","Belgique","La montagne",19,9300,"Bastogne","Belgique")
setUser("Laby","Olivier","rue du moulin",40,9850,"Bruxelle","Belgique","rue de mersch",30,9631,"Gemmenich","Belgique")
setUser("Dacosta","Steven","rue Scheerbach",59,9355,"Liege","Belgique","route d'Arlon",11,9555,"Liege","Belgique")



#   def setDemand(tpe,startD,toRId,toCId):
setDemand("mauvaise taille","20/01/2022",1,5)
setDemand("mauvaise couleur","23/01/2022",2,6)
setDemand("mauvaise taille","27/01/2022",3,7)
setDemand("mauvaise couleur","16/01/2022",4,6)



#   def setCart(doId,toId):
setCart(1,2)
setCart(2,3)
setCart(3,4)
setCart(4,5)


#   def setOrdered(doId,status,toId):
setOrdered(11,"livré",12)
setOrdered(12,"livré",13)
setOrdered(13,"livré",14)
setOrdered(14,"livré",15)

#   def setDetail(quantity,price,toId):
setDetail(3,99.99,2)
setDetail(3,119.99,3)
setDetail(1,199.99,12)
setDetail(2,39.99,4)
setDetail(1,99.99,11)
"""


def executePreFab():
        
    #   def setParcelService(name):
    #DONE
    setParcelService("bpost")
    setParcelService("ups")


    #   def setWarehouse(name,surface,locationSt,locationN,locationPc,locationCity,locationCou):
    #DONE
    setWarehouse("Entrepot Chaussure",300,"rue de la sagesse",55,9876,"Arlon","Belgique")
    setWarehouse("Entrepot Chaussure XXL",305,"rue des Meuniers",7,5766,"Thionville","France")
    setWarehouse("Entrepot Chaussure",233,"rue de Wiltz",24,6689,"PommerLoch","Luxembourg")
    setWarehouse("Entrepot Chaussure",44,"RotwandStrasse",5,3876,"Munich","Allemagne")

    #   def setDepartement(name,typeDep):
    #Done
    setDepartement("A","Comptable")
    setDepartement("B","GestionStk")
    setDepartement("C","HR")

    #   def setStore(name,addressSt,addressN,addressPc,addressCity,addressCou):
    #DONE
    setStore("Sneaker Wolf Namur","Avenue des croix du Feu",3,9977,"Namur","Belgique")
    setStore("Sneaker Wolf Paris","Avenue des anges",55,9900,"Paris","France")
    setStore("Sneaker Wolf Bxl","rue Jean-Pascal",17,8877,"Bruxelles","Belgique")
    setStore("Sneaker Wolf Jambes","rue Henri Burniaux",3,9557,"Jambes","Belgique")
    setStore("Sneaker Wolf Luxo","rue de Strassen",70,5177,"Capellen","Luxembourg")
    setStore("Sneaker Wolf Liege","Avenue des Montagnes",37,9227,"Liège","Belgique")
    setStore("Sneaker Wolf Trier","Bergstrasse",1,6887,"Trèves","Allemagne")



    ###################################################

    #   def setSport(sportString):
    #DONE
    setSport("running")
    setSport("basketball")
    setSport("football")
    setSport("skateboard")

    #   def setBrand(brandString, foundingYear):
    # DONE
    setBrand("Asics", "1977-05-12")
    setBrand("Nike", "1964-05-12")
    setBrand("Adidas", "1949-07-18")
    #setBrand("Reebok", "1958-01-01")

    #setBrand("Jordan", 1984)
    #setBrand("Converse", 1908)
    #setBrand("Vans", 2004)
    #setBrand("New Balance", 1906)
    #setBrand("Oasics", 1949)

    #   def setLine(lineString, IdBrand, IdSport = "1"):
    #DONE
    setLine("Sportstyle", 1, 1)
    setLine("supernova", 3, 3)
    setLine("airforce", 2, 2)
    setLine("airgriffey", 2, 2)
    #setLine("Nano", 3, 4)



    setCategorie("men")
    setCategorie("women")
    setCategorie("unisex")



    #DONE
    setModel("gel-kryos","unisex",1,"sportstyle") #1
    setModel("gel-lyte III OG","women",1,"sportstyle") #2
    setModel("premium gel-1130","men",1,"sportstyle") #3
    setModel("air Force 1 Boot","women",2,"airforce") #4
    setModel("air Force 1 Ultra Flyknit","men",2,"airgriffey") #5
    setModel("air Force 1 High","men",2,"airforce") #6
    setModel("air Force 1 Low","women",2,"airforce") #7
    setModel("air Force 1 Mid","women",2,"airforce") #8

    setModel("supernova+ Shoes","women",3,"supernova") #9
    setModel("supernova+ Shoes","men",3,"supernova") #10
    setModel("supernova+ Shoes","unisex",3,"supernova") #11
    setModel("supernova Shoes","women",3,"supernova") #12
    setModel("supernova Shoes","men",3,"supernova") #13
    setModel("supernova Shoes","unisex",3,"supernova") #14

    #   def setReleased(realaseDate, officalName, categorieName = "unisex", limitedEdition = False):
    #Done
    setReleased("2020-08-27", "A335", False, 1)
    setReleased("2019-05-17","A050",False,2)
    setReleased("2021-05-14","A255",True,3)

    setReleased("2013-05-27", "NB244", False, 4)
    setReleased("2011-02-15","NB212",False,5)
    setReleased("2022-01-02","NB423",True,6)
    setReleased("1970-07-01","NB444",False,7)
    setReleased("2020-03-07","NB412",True,8)

    setReleased("2018-05-27", "AD213", False, 9)
    setReleased("2018-05-27","AD222",False,10)
    setReleased("2018-05-27","AD234",True,11)
    setReleased("2020-07-01","AD345",False,12)
    setReleased("2020-07-01","AD552",True,13)
    setReleased("2020-07-01","AD112",True,14)



    #setSpecification(size, color, price, ReleaseID)
    #Done
    setSpecification(38, "black", 130, 1)
    setSpecification(39, "black", 130, 1)
    setSpecification(40, "black", 130, 1)
    setSpecification(41, "black", 130, 1)
    setSpecification(42, "black", 130, 1)
    setSpecification(43, "black", 130, 1)

    setSpecification(38, "black", 100, 2)
    setSpecification(39, "black", 100, 2)
    setSpecification(40, "black", 100, 2)
    setSpecification(41, "black", 100, 2)
    setSpecification(42, "black", 100, 2)
    setSpecification(43, "black", 100, 2)

    setSpecification(38, "blue-white", 150, 3)
    setSpecification(39, "blue-white", 150, 3)
    setSpecification(40, "blue-white", 150, 3)
    setSpecification(41, "blue-white", 150, 3)
    setSpecification(42, "blue-white", 150, 3)
    setSpecification(43, "blue-white", 150, 3)

    setSpecification(38, "grey", 210, 4)
    setSpecification(39, "grey", 210, 4)
    setSpecification(40, "grey", 210, 4)
    setSpecification(41, "grey", 210, 4)
    setSpecification(42, "grey", 210, 4)
    setSpecification(43, "grey", 210, 4)

    setSpecification(38, "Black", 99, 5)
    setSpecification(39, "Black", 99, 5)
    setSpecification(40, "Black", 99, 5)
    setSpecification(41, "Black", 99, 5)
    setSpecification(42, "Black", 99, 5)
    setSpecification(43, "Black", 99, 5)

    setSpecification(38, "yellow", 160, 6)
    setSpecification(39, "yellow", 160, 6)
    setSpecification(40, "yellow", 160, 6)
    setSpecification(41, "yellow", 160, 6)
    setSpecification(42, "yellow", 160, 6)
    setSpecification(43, "yellow", 160, 6)

    setSpecification(38, "red-white", 88, 7)
    setSpecification(39, "red-white", 88, 7)
    setSpecification(40, "red-white", 88, 7)
    setSpecification(41, "red-white", 88, 7)
    setSpecification(42, "red-white", 88, 7)
    setSpecification(43, "red-white", 88, 7)

    setSpecification(38, "orange", 130, 8)
    setSpecification(39, "orange", 130, 8)
    setSpecification(40, "orange", 130, 8)
    setSpecification(41, "orange", 130, 8)
    setSpecification(42, "orange", 130, 8)
    setSpecification(43, "orange", 130, 8)

    setSpecification(38, "orange-matt", 149, 9)
    setSpecification(39, "orange-matt", 149, 9)
    setSpecification(40, "orange-matt", 149, 9)
    setSpecification(41, "orange-matt", 149, 9)
    setSpecification(42, "orange-matt", 149, 9)
    setSpecification(43, "orange-matt", 149, 9)

    setSpecification(38, "white", 150, 10)
    setSpecification(39, "white", 150, 10)
    setSpecification(40, "white", 150, 10)
    setSpecification(41, "white", 150, 10)
    setSpecification(42, "white", 150, 10)
    setSpecification(43, "white", 150, 10)

    setSpecification(38, "black", 170, 11)
    setSpecification(39, "black", 170, 11)
    setSpecification(40, "black", 170, 11)
    setSpecification(41, "black", 170, 11)
    setSpecification(42, "black", 170, 11)
    setSpecification(43, "black", 170, 11)

    setSpecification(38, "grey", 100, 12)
    setSpecification(39, "grey", 100, 12)
    setSpecification(40, "grey", 100, 12)
    setSpecification(41, "grey", 100, 12)
    setSpecification(42, "grey", 100, 12)
    setSpecification(43, "grey", 100, 12)

    setSpecification(38, "velvet", 340, 13)
    setSpecification(39, "velvet", 340, 13)
    setSpecification(40, "velvet", 340, 13)
    setSpecification(41, "velvet", 340, 13)
    setSpecification(42, "velvet", 340, 13)
    setSpecification(43, "velvet", 340, 13)

    setSpecification(38, "cassis", 70, 14)
    setSpecification(39, "cassis", 70, 14)
    setSpecification(40, "cassis", 70, 14)
    setSpecification(41, "cassis", 70, 14)
    setSpecification(42, "cassis", 70, 14)
    setSpecification(43, "cassis", 70, 14)


    #def setToStock(specificationId, warehouseId, quantity):
    #DONE
    setToStock(1, 1, 100)
    setToStock(2, 1, 23)
    setToStock(3, 1, 34)
    setToStock(4, 1, 333)
    setToStock(5, 1, 140)
    setToStock(6, 1, 32)

    setToStock(7, 2, 100)
    setToStock(8, 2, 23)
    setToStock(9, 2, 34)
    setToStock(10, 2, 333)
    setToStock(11, 2, 140)
    setToStock(12, 2, 32)

    setToStock(13, 3, 100)
    setToStock(14, 3, 23)
    setToStock(15, 3, 34)
    setToStock(16, 3, 333)
    setToStock(17, 3, 140)
    setToStock(18, 3, 32)

    setToStock(19, 4, 100)
    setToStock(20, 4, 23)
    setToStock(21, 4, 34)
    setToStock(22, 4, 333)
    setToStock(23, 4, 140)
    setToStock(24, 4, 32)

    setToStock(25, 1, 100)
    setToStock(26, 1, 23)
    setToStock(27, 1, 34)
    setToStock(28, 1, 333)
    setToStock(29, 1, 140)
    setToStock(30, 1, 32)

    setToStock(31, 1, 100)
    setToStock(32, 1, 23)
    setToStock(33, 1, 34)
    setToStock(34, 1, 333)
    setToStock(35, 1, 140)
    setToStock(36, 1, 32)

    setToStock(37, 2, 100)
    setToStock(38, 2, 23)
    setToStock(39, 2, 34)
    setToStock(40, 2, 333)
    setToStock(41, 2, 140)
    setToStock(42, 2, 32)

    setToStock(43, 4, 100)
    setToStock(44, 4, 23)
    setToStock(45, 4, 34)
    setToStock(46, 4, 333)
    setToStock(47, 4, 140)
    setToStock(48, 4, 32)

    setToStock(49, 3, 100)
    setToStock(50, 3, 23)
    setToStock(51, 3, 34)
    setToStock(52, 3, 333)
    setToStock(53, 3, 140)
    setToStock(54, 3, 32)

    setToStock(55, 1, 100)
    setToStock(56, 1, 23)
    setToStock(57, 1, 34)
    setToStock(58, 1, 333)
    setToStock(59, 1, 140)
    setToStock(60, 1, 32)

    setToStock(61, 2, 100)
    setToStock(62, 2, 23)
    setToStock(63, 2, 34)
    setToStock(64, 2, 333)
    setToStock(65, 2, 140)
    setToStock(66, 2, 32)

    setToStock(67, 3, 100)
    setToStock(68, 3, 23)
    setToStock(69, 3, 34)
    setToStock(70, 3, 333)
    setToStock(71, 3, 140)
    setToStock(72, 3, 32)

    setToStock(73, 1, 100)
    setToStock(74, 1, 23)
    setToStock(75, 1, 34)
    setToStock(76, 1, 333)
    setToStock(77, 1, 140)
    setToStock(78, 1, 32)

    setToStock(79, 3, 100)
    setToStock(80, 3, 23)
    setToStock(81, 3, 34)
    setToStock(82, 3, 333)
    setToStock(83, 3, 140)
    setToStock(84, 3, 32)


