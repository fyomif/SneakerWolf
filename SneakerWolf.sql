-- *********************************************
-- * SQL MySQL generation
-- *--------------------------------------------
-- * DB-MAIN version: 11.0.2
-- * Generator date: Sep 14 2021
-- * Generation date: Wed May 18 14:33:58 2022
-- * LUN file: C:\Users\benny\Desktop\UNI\Bases donnees\Projet\newCommand\Sneaker_Wolf_update__v5.lun
-- * Schema: Schema Physique 2/1-1
-- *********************************************


-- Database Section
-- ________________



-- Tables Section
-- _____________

create table Brand (
     ID int not null auto_increment,
     Name varchar(255) not null,
     Founding_year date not null,
     constraint ID_Brand_ID primary key (ID));

create table Cart_Detail (
     ID int not null auto_increment,
     D_C_ID int not null,
     To__ID int not null,
     constraint ID_Cart_Detail_ID primary key (ID),
     constraint FKDet_Car_ID unique (D_C_ID));

create table Categorie (
     Name varchar(255) not null,
     constraint ID_Categorie_ID primary key (Name));

create table Customer (
     ID int not null auto_increment,
     U_C_ID int not null,
     VIP char not null,
     constraint ID_Customer_ID primary key (ID),
     constraint FKUse_Cus_ID unique (U_C_ID));

create table Demand_Return (
     ID int not null auto_increment,
     Type varchar(255) not null,
     start_date date not null,
     To_realize_ID int not null,
     To_concern_ID int not null,
     constraint ID_Demand_Return_ID primary key (ID));

create table Department (
     ID int not null auto_increment,
     Name varchar(255) not null,
     Type_Departement varchar(10) not null,
     constraint ID_Department_ID primary key (ID));

create table Detail (
     ID int not null auto_increment,
     Quantity decimal(10,2) not null,
     Price decimal(10,2) not null,
     To__ID int not null,
     Ordered_Detail int,
     Cart_Detail int,
     constraint ID_Detail_ID primary key (ID));

create table Employee (
     Personnal_number int not null auto_increment,
     ID int not null,
     National_register bigint not null,
     Birthday date not null,
     Title varchar(255) not null,
     To_work_ID int not null,
     Supervisor_ int,
     constraint ID_Employee_ID primary key (Personnal_number),
     constraint FKUse_Emp_ID unique (ID));

create table Ordered (
     Order_Number int not null auto_increment,
     ID int not null,
     constraint ID_Ordered_ID primary key (Order_Number));

create table Line (
     ID int not null,
     Name varchar(255) not null,
     To__ID int,
     constraint ID_Line_ID primary key (ID, Name));

create table Model (
     ID int not null auto_increment,
     ModelName varchar(255) not null,
     Name varchar(255) not null,
     To__ID int not null,
     To__Name varchar(255) not null,
     constraint ID_Model_ID primary key (ID));

create table Ordered_Detail (
     ID int not null auto_increment,
     D_O_ID int not null,
     Status char(1) not null,
     Order_Number int not null,
     constraint ID_Ordered_Detail_ID primary key (ID),
     constraint FKDet_Ord_ID unique (D_O_ID));

create table Parcel_Service (
     ID int not null auto_increment,
     Name varchar(255) not null,
     constraint ID_Parcel_Service_ID primary key (ID));

create table Promotion (
     ID int not null auto_increment,
     Percentage_rate int,
     Percentage_amount decimal(10,2),
     Pro_Name varchar(10) not null,
     Pro_Start_date date not null,
     Pro_End_date date not null,
     constraint ID_Promotion_ID primary key (ID));

create table Released (
     ID int not null auto_increment,
     Release_date date not null,
     Official_name varchar(255) not null,
     Limited_edition char,
     To__ID int not null,
     constraint ID_Released_ID primary key (ID));

create table Specification (
     ID int not null auto_increment,
     Size decimal(10,1) not null,
     Color varchar(255) not null,
     Price decimal(10,2) not null,
     To__ID int not null,
     constraint ID_Specification_ID primary key (ID));

create table Sport (
     ID int not null auto_increment,
     Name varchar(255) not null,
     constraint ID_Sport_ID primary key (ID));

create table Store (
     ID int not null auto_increment,
     Name varchar(255) not null,
     addressStore_Street varchar(255) not null,
     addressStore_Number int not null,
     addressStore_Postal_code varchar(256) not null,
     addressStore_City varchar(244) not null,
     addressStore_Country varchar(255) not null,
     constraint ID_Store_ID primary key (ID));

create table To_attach (
     T_P_ID int not null,
     ID int not null,
     constraint ID_To_attach_ID primary key (ID, T_P_ID));

create table To_relate (
     ID int not null auto_increment,
     T_D_ID int not null,
     Related_to__1_ int,
     Related_to__1__1 int,
     constraint ID_To_relate_ID primary key (ID));

create table To_sale (
     T_S_ID int not null,
     ID int not null,
     Quantity char(1) not null,
     constraint ID_To_sale_ID primary key (ID, T_S_ID));

create table To_serve (
     T_D_ID int not null,
     ID int not null,
     T_P_ID int not null,
     constraint FKTo__Det_ID primary key (T_D_ID));

create table To_stock (
     T_S_ID int not null,
     ID int not null,
     Quantity int not null,
     constraint ID_To_stock_ID primary key (ID, T_S_ID));

create table User (
     ID int not null auto_increment,
     Name varchar(255) not null,
     Surname varchar(255) not null,
     billing_add_Street varchar(255) not null,
     billing_add_Number int not null,
     billing_add_Postal_code varchar(255) not null,
     billing_add_City varchar(255) not null,
     billing_add_Country varchar(255) not null,
     delivery_add_Street varchar(255) not null,
     delivery_add_Number int not null,
     delivery_add_Postal_code varchar(255) not null,
     delivery_add_City varchar(255) not null,
     delivery_add_Country varchar(255) not null,
     username varchar(255) not null,
     password varchar(20) not null,
     Employee int,
     Customer int,
     constraint ID_User_ID primary key (ID));

create table Warehouse (
     ID int not null auto_increment,
     Name varchar(255) not null,
     Surface_area int not null,
     location_Street varchar(255) not null,
     location_Number int not null,
     location_Postal_code varchar(244) not null,
     location_City varchar(255) not null,
     location_Country varchar(255) not null,
     constraint ID_Warehouse_ID primary key (ID));


-- Constraints Section
-- ___________________

alter table Cart_Detail add constraint FKTo_own_FK
     foreign key (To__ID)
     references User (ID);

alter table Cart_Detail add constraint FKDet_Car_FK
     foreign key (D_C_ID)
     references Detail (ID);

alter table Customer add constraint FKUse_Cus_FK
     foreign key (U_C_ID)
     references User (ID);

alter table Demand_Return add constraint FKTo_realize_FK
     foreign key (To_realize_ID)
     references User (ID);

alter table Demand_Return add constraint FKTo_concern_FK
     foreign key (To_concern_ID)
     references Detail (ID);

alter table Detail add constraint EXTONE_Detail
     check((Ordered_Detail is not null and Cart_Detail is null)
           or (Ordered_Detail is null and Cart_Detail is not null));

alter table Detail add constraint FKTo_bind_FK
     foreign key (To__ID)
     references Specification (ID);

alter table Employee add constraint FKUse_Emp_FK
     foreign key (ID)
     references User (ID);

alter table Employee add constraint FKTo_work_FK
     foreign key (To_work_ID)
     references Department (ID);

alter table Employee add constraint FKTo_supervise_FK
     foreign key (Supervisor_)
     references Employee (Personnal_number);

-- Not implemented
-- alter table Ordered add constraint ID_Ordered_CHK
--     check(exists(select * from Ordered_Detail
--                  where Ordered_Detail.Order_Number = Order_Number));

alter table Ordered add constraint FKTo_pass_FK
     foreign key (ID)
     references User (ID);

alter table Line add constraint FKTo_have
     foreign key (ID)
     references Brand (ID);

alter table Line add constraint FKTo_belong_FK
     foreign key (To__ID)
     references Sport (ID);

-- Not implemented
-- alter table Model add constraint ID_Model_CHK
--     check(exists(select * from Released
--                  where Released.To__ID = ID));

alter table Model add constraint FKTo_link_FK
     foreign key (Name)
     references Categorie (Name);

alter table Model add constraint FKTo_possess_FK
     foreign key (To__ID, To__Name)
     references Line (ID, Name);

alter table Ordered_Detail add constraint FKTo_make_FK
     foreign key (Order_Number)
     references Ordered (Order_Number);

alter table Ordered_Detail add constraint FKDet_Ord_FK
     foreign key (D_O_ID)
     references Detail (ID);

alter table Promotion add constraint EXTONE_Promotion
     check((Percentage_amount is not null and Percentage_rate is null)
           or (Percentage_amount is null and Percentage_rate is not null));

-- Not implemented
-- alter table Released add constraint ID_Released_CHK
--     check(exists(select * from Specification
--                  where Specification.To__ID = ID));

alter table Released add constraint FKTo_connect_FK
     foreign key (To__ID)
     references Model (ID);

alter table Specification add constraint FKTo_Get_FK
     foreign key (To__ID)
     references Released (ID);

alter table To_attach add constraint FKTo__Spe_2
     foreign key (ID)
     references Specification (ID);

alter table To_attach add constraint FKTo__Pro_FK
     foreign key (T_P_ID)
     references Promotion (ID);

alter table To_relate add constraint EXTONE_To_relate
     check((Related_to__1__1 is not null and Related_to__1_ is null)
           or (Related_to__1__1 is null and Related_to__1_ is not null));

alter table To_relate add constraint FKTo__Dep_FK
     foreign key (T_D_ID)
     references Department (ID);

alter table To_relate add constraint FKrelated_to_2_FK
     foreign key (Related_to__1_)
     references Warehouse (ID);

alter table To_relate add constraint FKrelated_to_1_FK
     foreign key (Related_to__1__1)
     references Store (ID);

alter table To_sale add constraint FKTo__Sto
     foreign key (ID)
     references Store (ID);

alter table To_sale add constraint FKTo__Spe_1_FK
     foreign key (T_S_ID)
     references Specification (ID);

alter table To_serve add constraint FKTo__War_1_FK
     foreign key (ID)
     references Warehouse (ID);

alter table To_serve add constraint FKTo__Par_FK
     foreign key (T_P_ID)
     references Parcel_Service (ID);

alter table To_serve add constraint FKTo__Det_FK
     foreign key (T_D_ID)
     references Detail (ID);

alter table To_stock add constraint FKTo__War
     foreign key (ID)
     references Warehouse (ID);

alter table To_stock add constraint FKTo__Spe_FK
     foreign key (T_S_ID)
     references Specification (ID);

alter table User add constraint EXTONE_User
     check((Customer is not null and Employee is null)
           or (Customer is null and Employee is not null));


-- Index Section
-- _____________

create unique index ID_Brand_IND
     on Brand (ID);

create unique index ID_Cart_Detail_IND
     on Cart_Detail (ID);

create index FKTo_own_IND
     on Cart_Detail (To__ID);

create unique index FKDet_Car_IND
     on Cart_Detail (D_C_ID);

create unique index ID_Categorie_IND
     on Categorie (Name);

create unique index ID_Customer_IND
     on Customer (ID);

create unique index FKUse_Cus_IND
     on Customer (U_C_ID);

create unique index ID_Demand_Return_IND
     on Demand_Return (ID);

create index FKTo_realize_IND
     on Demand_Return (To_realize_ID);

create index FKTo_concern_IND
     on Demand_Return (To_concern_ID);

create unique index ID_Department_IND
     on Department (ID);

create unique index ID_Detail_IND
     on Detail (ID);

create index FKTo_bind_IND
     on Detail (To__ID);

create unique index ID_Employee_IND
     on Employee (Personnal_number);

create unique index FKUse_Emp_IND
     on Employee (ID);

create index FKTo_work_IND
     on Employee (To_work_ID);

create index FKTo_supervise_IND
     on Employee (Supervisor_);

create unique index ID_Ordered_IND
     on Ordered (Order_Number);

create index FKTo_pass_IND
     on Ordered (ID);

create unique index ID_Line_IND
     on Line (ID, Name);

create index FKTo_belong_IND
     on Line (To__ID);

create unique index ID_Model_IND
     on Model (ID);

create index FKTo_link_IND
     on Model (Name);

create index FKTo_possess_IND
     on Model (To__ID, To__Name);

create unique index ID_Ordered_Detail_IND
     on Ordered_Detail (ID);

create index FKTo_make_IND
     on Ordered_Detail (Order_Number);

create unique index FKDet_Ord_IND
     on Ordered_Detail (D_O_ID);

create unique index ID_Parcel_Service_IND
     on Parcel_Service (ID);

create unique index ID_Promotion_IND
     on Promotion (ID);

create unique index ID_Released_IND
     on Released (ID);

create index FKTo_connect_IND
     on Released (To__ID);

create unique index ID_Specification_IND
     on Specification (ID);

create index FKTo_Get_IND
     on Specification (To__ID);

create unique index ID_Sport_IND
     on Sport (ID);

create unique index ID_Store_IND
     on Store (ID);

create unique index ID_To_attach_IND
     on To_attach (ID, T_P_ID);

create index FKTo__Pro_IND
     on To_attach (T_P_ID);

create unique index ID_To_relate_IND
     on To_relate (ID);

create index FKTo__Dep_IND
     on To_relate (T_D_ID);

create index FKrelated_to_2_IND
     on To_relate (Related_to__1_);

create index FKrelated_to_1_IND
     on To_relate (Related_to__1__1);

create unique index ID_To_sale_IND
     on To_sale (ID, T_S_ID);

create index FKTo__Spe_1_IND
     on To_sale (T_S_ID);

create index FKTo__War_1_IND
     on To_serve (ID);

create index FKTo__Par_IND
     on To_serve (T_P_ID);

create unique index FKTo__Det_IND
     on To_serve (T_D_ID);

create unique index ID_To_stock_IND
     on To_stock (ID, T_S_ID);

create index FKTo__Spe_IND
     on To_stock (T_S_ID);

create unique index ID_User_IND
     on User (ID);

create unique index ID_Warehouse_IND
     on Warehouse (ID);


-- Procedure Section
-- _________________
DELIMITER $$

CREATE PROCEDURE CheckPromoDate(startDate DATE, endDate DATE)
BEGIN
 IF startDate >= endDate THEN
      SIGNAL SQLSTATE '45000'
         SET MESSAGE_TEXT = 'Promotion end date must be after start date';
 END IF;
END $$

DELIMITER ;

-- Trigger Section
-- _____________
DELIMITER $$

CREATE TRIGGER verif_date_promo_insert
BEFORE INSERT
ON Promotion FOR EACH ROW
BEGIN
CALL CheckPromoDate (
     NEW.Pro_Start_date,
     NEW.Pro_End_date
 );
END$$


CREATE TRIGGER verif_date_promo_update
BEFORE UPDATE
ON Promotion FOR EACH ROW
BEGIN
CALL CheckPromoDate (
     NEW.Pro_Start_date,
     NEW.Pro_End_date
 );
END$$





CREATE TRIGGER verif_return_user_equals_order_user
BEFORE INSERT
ON Demand_Return FOR EACH ROW
BEGIN

    SET @user_id := (SELECT ID FROM Ordered WHERE Order_Number IN
      (SELECT Order_Number FROM Ordered_Detail WHERE D_O_ID = NEW.To_concern_ID));

    IF not(NEW.To_realize_ID = @user_id) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'constraint: the user making the return demand must be the one who ordered the item';
    END IF;

END$$

CREATE TRIGGER applypromo
BEFORE INSERT
ON Detail FOR EACH ROW
BEGIN
    DECLARE finished INTEGER DEFAULT 0;
    DECLARE promo_id integer;

    -- declare cursor for promo_id
    DEClARE curPromoID
        CURSOR FOR
            SELECT T_P_ID FROM To_attach WHERE To_attach.ID = NEW.To__ID AND (CURDATE() BETWEEN (SELECT Pro_Start_date FROM Promotion WHERE ID = T_P_ID limit 1) AND (SELECT Pro_End_date FROM Promotion WHERE ID = T_P_ID limit 1));


    -- declare NOT FOUND handler
    DECLARE CONTINUE HANDLER
        FOR NOT FOUND SET finished = 1;

      OPEN curPromoID;

    getPromo: LOOP
        FETCH curPromoID INTO promo_id;
        IF finished = 1 THEN
            LEAVE getPromo;
        END IF;

        SET @percentage_amount := (SELECT Percentage_amount
                from Promotion
                 WHERE Promotion.ID = promo_id
                limit 1);

        SET @percentage_rate := (SELECT Percentage_rate
                from Promotion
                 WHERE Promotion.ID = promo_id
                limit 1);

        IF(@percentage_rate IS NULL) THEN
            SET NEW.Price = (NEW.Price - @percentage_amount);
        END IF;

        IF(@percentage_amount IS NULL) THEN
            SET NEW.Price = (NEW.price - ((@percentage_rate * NEW.Price) / 100));
        END IF;

        SET @percentage_rate := NULL;
        SET @percentage_amount := NULL;

    END LOOP getPromo;
    CLOSE curPromoID;
END$$

DELIMITER ;
