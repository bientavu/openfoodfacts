from core.models import Product, Category, Substitute
from core.input_validators import Validation

# product = Product()
validation = Validation()

class Controller:
    def __init__(self, view, product):
        self.view = view
        self.product = product

    def run(self):
        self.view.hello()
        while True:
            response = self.view.welcome_menu()
            if validation.validate_welcome_input(response) == True:
                break
        self.view.welcome_menu()
                    # sinon le menu réapparait



        # si la valeur est A, alors je montre les catégories (while)
        # Si c'était A : en fonction de la catégorie choisie, j'affiche les aliments disponibles de cette dernière
        # Un aliment substitué est alors proposé : affichage des toutes ces informations + proposition de l'enregistrer dans l'historique
        # L'utilisateur est renvoyé à menu d'acceuil
    
        # si la valeur est B, alors je montre l'historique (while)
        # Si c'était B : j'affiche l'historique des aliments substitués --> tables Substitutes
        # L'utilisateur peut alors appuyer sur Entrée pour retourner au menu



        


    
        
