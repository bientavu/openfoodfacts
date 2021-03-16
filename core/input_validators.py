
class Validation:
    def validate_welcome_input(self, value):
        if value == '1' or '2':
            return True
        else:
            return False
        # si c'est bon je retourne True, sinon False