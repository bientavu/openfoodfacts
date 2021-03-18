from .models import Product, Category, Substitute
from . import input_validators

# product = Product()

class Controller:
    def __init__(self, view, product):
        self.view = view
        self.product = product
        self.category_choice = None

    def run(self):
        self.view.hello()
        self.methode_to_execute = self.welcome_menu
        while self.methode_to_execute is not None:
            next_method = self.methode_to_execute()
            self.methode_to_execute = next_method
        
    def welcome_menu(self):
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
        categories = Category.objects.fetch_all_category()
        while True:
            response = self.view.choosecategory_menu(categories)
            if input_validators.is_valid_category_response(response, categories):
                break

        if response in [str(index) for index, category in enumerate(categories, start = 1)]:
            self.category_choice = categories [int(response) - 1]
            return self.choosefood_menu
        elif response == str(len(categories) + 1):
            return self.welcome_menu
        elif response == str(len(categories) + 2):
            return self.quit

    def choosefood_menu(self):
        pass

    def substitutelisting(self):
        pass

    def quit(self):
        self.view.quit()

        # si la valeur est A, alors je montre les catégories (while)
        # Si c'était A : en fonction de la catégorie choisie, j'affiche les aliments disponibles de cette dernière
        # Un aliment substitué est alors proposé : affichage des toutes ces informations + proposition de l'enregistrer dans l'historique
        # L'utilisateur est renvoyé à menu d'acceuil
    
        # si la valeur est B, alors je montre l'historique (while)
        # Si c'était B : j'affiche l'historique des aliments substitués --> tables Substitutes
        # L'utilisateur peut alors appuyer sur Entrée pour retourner au menu



        


    
        
