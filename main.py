from core.sql import Sql
from core.openfoodfacts import Data

# connection = Sql()
# connection.dbinit()

import_data = Data()
import_data._get_information_product()

#connection.insertdata()