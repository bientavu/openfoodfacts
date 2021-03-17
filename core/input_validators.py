

def is_valid_welcome_response(response):
        """
        Cheking if the welcome input is True or False to continue
        Otherwise the welcome message keeps repeating
        """
        if response in ['1', '2', '3']:
            return True
        else:
            return False

def is_valid_category_response(response, categories):
        """
        Cheking if the category input is True or False to continue
        Otherwise the welcome message keeps repeating
        """
        if response in [str(number) for number in range(1, len(categories) + 3)]:
            return True
        else:
            return False