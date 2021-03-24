from pprint import pprint
from .models import Category, Product

class View:

    def hello(self):

        welcoming_message = print(
            "Bonjour et bienvenue ! Je suis un programme qui vous aidera à remplacer\n"
            "des produits alimentaires de mauvaises qualités en vous en proposant des\n"
            "équivalents de meilleures qualitée. Je vais chercher les infos sur openfoodfacts.\n"
            )
        name = input("Quel est votre nom ? ")
        if name == "":
            return None
        
        print(f"\nRavie de vous rencontrer {name} ! C'est parti !")
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
            menu_options[position] = f"{category.name_cat.capitalize().replace('-', ' ')}\n"
        menu_options[position + 1] = "Revenir à l'acceuil"
        menu_options[position + 2] = "Quitter le programme"

        menu_options_as_string = []
        for key, value in menu_options.items():
            value_string = f"{key}. {value}\n"
            menu_options_as_string.append(value_string)
        
        menu = "".join(menu_options_as_string)

        return input(
            "\nVeuillez sélectionner une catégorie :\n\n"
            f"{menu}"
            "\nQuel est votre choix ? (Tapez le numéro correspondant) : "
            )

    def choosefood_menu(self, products):

        menu_options = {}
        for position, product in enumerate(products, start=1):
            if product.nutriscore == 'e' or product.nutriscore == 'd':
                product_name_cleaned = product.name.replace('\n', ' ')
                menu_options[position] = f"{product_name_cleaned} | Nutriscore : {product.nutriscore} | Magasin(s) : {product.store}\n"
        menu_options[position + 1] = "Revenir à l'acceuil"
        menu_options[position + 2] = "Quitter le programme"

        menu_options_as_string = []
        for key, value in menu_options.items():
            value_string = f"{key}. {value}\n"
            menu_options_as_string.append(value_string)
        
        menu = "".join(menu_options_as_string)

        return input(
            "\nVeuillez sélectionner un produit à substituer :\n"
            f"{menu}"
            "\nQuel est votre choix ? (Tapez le numéro correspondant) : "
            )

    def foodsuggestion(self, selected_product, better_product):

        for product in selected_product:
            product_name_cleaned = product.name.replace('\n', ' ')
            print(f"""
            ###### Produit à substituer ######
            Nom du produit : {product_name_cleaned}
            Nutriscore : {product.nutriscore}
            Magasin(s) : {product.store}
            Lien openfoodfacts : {product.link}
            """)

        for product in better_product:
            product_name_cleaned = product.name.replace('\n', ' ')
            print(f"""
            ###### Substitut proposé ######
            Nom du produit : {product_name_cleaned}
            Nutriscore : {product.nutriscore}
            Magasin(s) : {product.store}
            Lien openfoodfacts : {product.link}
            """)
        
        return input(
            "Veuillez sélectionner une action :\n"
            "1. Enregistrer ce substitut dans l'historique\n"
            "2. Accéder à votre historique de produits subtitués\n"
            "3. Revenir à l'acceuil\n"
            "4. Quitter le programme\n"
            "\nQuel est votre choix ? (Tapez le numéro correspondant) : "
             )

    def substitutelisting(self):
        pass

    def quit(self):
        print("\nMerci d'avoir utilisé ce programme !\n"
        "En espérant que cela vous ai été utile. A bientôt !\n")