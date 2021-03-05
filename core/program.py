

class WelcomeMenu():

    def hello(self):

        welcoming_message = print("""Hello and welcome ! I'm a program that will help you replace
        bad quality food by giving you healthier products. I'm looking into the openfoodfacts
        database in order to suggest you the best food ratings.
        """)
        name = input("What is your name ? ")
        
        print(f"Ok nice to meet you {name} ! Let's start then")
        input("You can press Enter to continue...")

        return welcoming_message

class ChooseCategory():
    pass

class ChooseFood():
    pass

class FoodSuggestion():
    pass

class SubstituteListing():
    pass