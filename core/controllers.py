from .models import Product, Category, Substitute
from . import input_validators

# product = Product()

class Controller:
    """
    Controls the program by calling methods from the 
    managers, models and views modules
    """
    def __init__(self, view, product):
        """
        view, product, category_choice
        and product_choice initialization
        """
        self.view = view
        self.product = product
        self.category_choice = None
        self.product_choice = None

    def run(self):
        """
        Loop that runs all the next 
        'menu' methods from the controllers
        """
        self.view.hello()
        self.methode_to_execute = self.welcome_menu
        while self.methode_to_execute is not None:
            next_method = self.methode_to_execute()
            self.methode_to_execute = next_method
        
    def welcome_menu(self):
        """
        The first menu for the user.
        Calling a view from view.py and
        the input gets a validation
        """
        while True:
            response = self.view.welcome_menu()
            if input_validators.is_valid_welcome_response(response):
                break
        if response == '1':
            return self.choosecategory_menu
        elif response == '2':
            return self.substitutelisting
        elif response == '3':
            return self.quit

    def choosecategory_menu(self):
        """
        The second menu for the user, where he choose a category
        Calling all the categories from managers.py
        Calling a view from view.py and the input gets a validation
        """
        categories = Category.objects.fetch_all_categories()
        while True:
            response = self.view.choosecategory_menu(categories)
            if input_validators.is_valid_category_response(response, categories):
                break

        if response in [str(index) for index, category in enumerate(categories, start = 1)]:
            self.category_choice = categories[int(response) - 1]
            return self.choosefood_menu
        elif response == str(len(categories) + 1):
            return self.welcome_menu
        elif response == str(len(categories) + 2):
            return self.quit

    def choosefood_menu(self):
        """
        The third menu for the user, where he choose a product
        Calling all the products from managers.py
        Calling a view from view.py and the input gets a validation
        """
        products = Product.objects.fetch_all_products(self.category_choice)
        while True:
            response = self.view.choosefood_menu(products)
            if input_validators.is_valid_product_response(response, products):
                break

        if response in [str(index) for index, category in enumerate(products, start = 1)]:
            self.product_choice = products[int(response) - 1]
            return self.suggested_food
        elif response == str(len(products) + 1):
            return self.welcome_menu
        elif response == str(len(products) + 2):
            return self.quit

    def suggested_food(self):
        """
        The last menu for the user, where he choose to save his product
        or to enter into his products history.
        Calling the product he chose and a random substitute from managers.py
        Calling a view from view.py and the input gets a validation
        """
        selected_product = Product.objects.fetch_selected_product(self.product_choice)
        better_product = Product.objects.fetch_better_product(self.category_choice)
        while True:
            response = self.view.foodsuggestion(selected_product, better_product)
            if input_validators.is_valid_suggested_product_response(response, selected_product):
                break

        # if response in [str(index) for index, category in enumerate(product, start = 1)]:
        #     self.product_choice = product[int(response) - 1]
        #     return self.choosefood_menu
        # elif response == str(len(product) + 1):
        #     return self.welcome_menu
        # elif response == str(len(product) + 2):
        #     return self.quit

    def substitutelisting(self):
        pass

    def quit(self):
        """
        Close the program
        """
        self.view.quit()




        


    
        
