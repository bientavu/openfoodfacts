from core.models import Category, Product

class View:

    def hello(self):

        welcoming_message = print(
            # "Hello and welcome ! I'm a program that will help you replace bad\n"
            # "quality food by giving you healthier products. I'm looking into the\n"
            # "openfoodfacts database in order to suggest you the best food ratings.\n"
            "Bonjour et bienvenue ! Je suis un programme qui vous aidera à remplacer\n"
            "des produits alimentaires de mauvaises qualités en vous en proposant des\n"
            "équivalents de meilleures qualitée. Je vais chercher les infos sur openfoodfacts.\n"
            )
        name = input("Quel est votre nom ? ")
        if name == "":
            return None
        
        print("")
        print(f"Ravie de vous rencontrer {name} ! C'est parti !")
        input("Vous pouvez appuyer sur 'Entrée' pour commencer...")

        return welcoming_message

    def welcome_menu(self):

        print("")
        menu_choice = input(
            "Souhaitez-vous:\n"
            "1. Choisir une catégorie pour trouver un produit à substituer\n"
            "2. Accéder à votre historique de produits subtitués\n"
            "3. Quitter le programme\n"
            "\nQuel est votre choix ? (Tapez le numéro correspondant) : "
            )
            
        return menu_choice

    def choosecategory_menu(self, categories):

        menu_options = {}
        for position, category in enumerate(categories, start=1):
            menu_options[position] = category.name_cat
        menu_options[position + 1] = "Revenir à l'acceuil"
        menu_options[position + 2] = "Quitter le programme"

        menu_options_as_string = []
        for key, value in menu_options.items():
            value_string = f"{key}. {value}\n"
            menu_options_as_string.append(value_string)
        
        menu = "".join(menu_options_as_string)

        return input(
            "\nVeuillez sélectionner une catégorie :\n"
            f"{menu}"
            )

    def choosefood_menu(self):
        pass

    def foodsuggestion(self):
        pass

    def substitutelisting(self):
        pass

    def quit(self):
        print("Salut !")