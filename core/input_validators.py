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
    Otherwise the category message keeps repeating
    """
    if response in [str(number) for number in range(1, len(categories) + 3)]:
        return True
    else:
        return False


def is_valid_product_response(response, products):
    """
    Cheking if the product input is True or False to continue
    Otherwise the product message keeps repeating
    """
    if response in [str(number) for number in range(1, len(products) + 3)]:
        return True
    else:
        return False


def is_valid_suggested_product_response(response):
    """
    Cheking if the input is True or False to continue
    Otherwise the message keeps repeating
    """
    if response in ['1', '2', '3', '4']:
        return True
    else:
        return False


def is_valid_favorites_response(response):
    """
    Cheking if the favorites input is True or False to continue
    Otherwise the favorites message keeps repeating
    """
    if response in ['1', '2', '3']:
        return True
    else:
        return False


def is_valid_favorites_list_response(response, substitutes):
    """
    Cheking if the favorites input is True or False to continue
    Otherwise the favorites message keeps repeating
    """
    if response in [str(number) for number in range(1, len(substitutes) + 3)]:
        return True
    else:
        return False