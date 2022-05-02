class User:
    def __init__(self, id, To_ID, name, surname, billing_add_street, billing_add_number, billing_add_postal_code,
                 billing_add_city, billing_add_country, delivery_add_street, delivery_add_number,
                 delivery_add_postal_code, delivery_add_city, delivery_add_country, employee, customer):
        self.id = id
        self.To_ID = To_ID
        self.name = name
        self.surname = surname
        self.billing_add_street = billing_add_street
        self.billing_add_number = billing_add_number
        self.billing_add_postal_code = billing_add_postal_code
        self.billing_add_city = billing_add_city
        self.billing_add_country = billing_add_country
        self.delivery_add_street = delivery_add_street
        self.delivery_add_number = delivery_add_number
        self.delivery_add_postal_code = delivery_add_postal_code
        self.delivery_add_city = delivery_add_city
        self.delivery_add_country = delivery_add_country
        self.employee = employee
        self.customer = customer
