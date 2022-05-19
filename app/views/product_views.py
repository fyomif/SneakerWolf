# TODO: Define the parameters of the function to allow filter dependent display

def Product_listing():
    # TODO: List different products
    print("Product list")

    print("\n If you want to see more about specific product, tap its number, else tap enter : ")
    enter = input()
    if enter.isnumeric():
        product_number = int(enter)
        Product_detail(product_number)
    else:
        print()



def Product_detail(id):
    # TODO: code to display the product detail
    print("Product detail")

    # Display differents options available on the product like buy now and add to cart and add the function to make it
    print("\n --  Do you like this product !?! -- \n Tape : \n")
    print("\t 1: For Buy now")
    print("\t 2: For Add to cart")
    print("\t 0: For Back home")

    answer = input("What do you want ? : ")
    if answer == "1":
        # TODO: Buy now function
        print("")
    elif answer == "2":
        # TODO: Add to cart function
        print("")
    else:
        print("")


def Product_by_category():
    category = input("\n Enter your category : ")
    # TODO: Function to display all product of the category


def Research_product():
    product = input("Enter the product name, model, category or number of the product")
    # TODO: Function for display researched product
