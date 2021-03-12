

class View:

    def hello(self):

        welcoming_message = print("""Hello and welcome ! I'm a program that will help you replace
        bad quality food by giving you healthier products. I'm looking into the openfoodfacts
        database in order to suggest you the best food ratings.
        """)
        name = input("What is your name ? ")
        if name == "":
            return None
        
        print("")
        print(f"Ok nice to meet you {name} ! Let's start then")
        print("")
        input("You can press Enter to continue...")

        return welcoming_message

    def welcome_menu(self):

        print("")
        menu_choice = input("""Do you want to:
        A) Find an healthier product
        B) Acces your food history
        [A/B]? : """)

        return menu_choice

    def choosecategory(self):
        pass
    
    def choosefood(self):
        pass

    def foodsuggestion(self):
        pass

    def substitutelisting(self):
        pass