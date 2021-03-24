from pprint import pprint
from .models import Category, Product

class View:
    """
    Regroups all the views that the user is facing
    """
    def hello(self):
        """
        Hello message displayed when the program launch
        """
        welcoming_message = print(
            "\nBonjour et bienvenue ! Je suis un programme qui vous aidera à remplacer des\n"
            "produits alimentaires de mauvaise qualité en vous en proposant des équivalents de \n"
            "meilleure qualité. Je me base sur le Nutri-Score d'un produit allant de A à E :\n\n"
            "- Nutri-Score A : Très bonne qualité nutritionnelle\n"
            "- Nutri-Score B : Bonne qualité nutritionnelle\n"
            "- Nutri-Score C : Qualité nutritionnelle moyenne\n"
            "- Nutri-Score D : Mauvaise qualité nutritionnelle\n"
            "- Nutri-Score E : Très mauvaise qualité nutritionnelle\n\n"
            "Vous pouvez trouver plus d'informations sur le Nutri-Score sur : https://www.mangerbouger.fr/\n"
            "Toutes les informations des produits sont récupérées sur : https://fr.openfoodfacts.org/\n"
            )
        name = input("Quel est votre nom ? ")
        if name == "":
            return None
        
        print(f"\nRavie de vous rencontrer {name} ! C'est parti !")
        input("Vous pouvez appuyer sur 'Entrée' pour commencer...")

        return welcoming_message

    def welcome_menu(self):
        """
        First menu message where the user choose between
        substitute a product, access his history or quit the program
        """
        print("")
        menu_choice = input(
            "Souhaitez-vous:\n"
            "1. Choisir une catégorie pour trouver un produit à substituer\n"
            "2. Accéder aux favoris des produits subtitués\n"
            "3. Quitter le programme\n"
            "\nQuel est votre choix ? (Tapez le numéro correspondant) : "
            )
            
        return menu_choice

    def choosecategory_menu(self, categories):
        """
        Second menu message where the user has to choose the category
        of the product he wants to substitute. Possibilities to go back
        to the welcome menu or quit the program
        """
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
        """
        Third menu message where the user has to choose the product 
        he wants to substitute. Possibilities to go back
        to the welcome menu or quit the program
        """
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

        response = input(
            "\nVeuillez sélectionner un produit à substituer :\n\n"
            f"{menu}"
            "\nQuel est votre choix ? (Tapez le numéro correspondant) : "
            )
        print("")

        return response

    def foodsuggestion(self, selected_product, better_product):
        """
        Last menu message where the selected product and a better one
        is displayed. User can save the products, access his history
        or quit the program
        """
        for product in selected_product:
            product_name_cleaned = product.name.replace('\n', ' ')
            print(
            "-----------Produit à substituer----------\n"
            f"Nom du produit : {product_name_cleaned}\n"
            f"Nutriscore : {product.nutriscore}\n"
            f"Magasin(s) : {product.store}\n"
            f"Lien openfoodfacts : {product.link}\n"
            )

        for product in better_product:
            product_name_cleaned = product.name.replace('\n', ' ')
            print(
            "------------Produit substitut------------\n"
            f"Nom du produit : {product_name_cleaned}\n"
            f"Nutriscore : {product.nutriscore}\n"
            f"Magasin(s) : {product.store}\n"
            f"Lien openfoodfacts : {product.link}\n"
            )
        
        return input(
            "Veuillez sélectionner une action :\n"
            "1. Enregistrer ce substitut dans les favoris\n"
            "2. Accéder aux favoris des produits subtitués\n"
            "3. Revenir à l'acceuil\n"
            "4. Quitter le programme\n"
            "\nQuel est votre choix ? (Tapez le numéro correspondant) : "
             )

    def substitutelisting(self):
        pass

    def quit(self):
        """
        Display a thank you message when the user qui the program
        """
        print("\nMerci d'avoir utilisé ce programme !\n"
        "En espérant que cela vous ai été utile. A bientôt !\n")