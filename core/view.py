

class View:

    def hello(self):

        welcoming_message = print(
            "Hello and welcome ! I'm a program that will help you replace bad\n"
            "quality food by giving you healthier products. I'm looking into the\n"
            "openfoodfacts database in order to suggest you the best food ratings.\n"
            )
        name = input("What is your name ? ")
        if name == "":
            return None
        
        print("")
        print(f"Ok nice to meet you {name} ! Let's start then")
        input("You can press Enter to continue...")

        return welcoming_message

    def welcome_menu(self):

        print("")
        menu_choice = input(
            "Do you want to:\n"
            "1) Find an healthier product\n"
            "2) Acces your food history\n"
            "[1/2]? : "
            )
            
        return menu_choice

    def choosecategory(self):
        pass
    
    def choosefood(self):
        pass

    def foodsuggestion(self):
        pass

    def substitutelisting(self):
        pass