from core.models import Product
from core.views import View
from core.controllers import Controller

def main():
    """
    Run the program
    """
    view = View()
    product = Product

    program_controller = Controller(view, product)
    program_controller.run()

if __name__ == "__main__":
    main()
