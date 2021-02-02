from core.sql import Sql
from core.openfoodfacts import Data

# connection = Sql()
# connection.dbinit()

grabber = Data()
grabber._get_information_product()

#connection.insertdata()