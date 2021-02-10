from core.sql import Sql
from core.openfoodfacts import Data

# connection = Sql()
# connection.dbinit()

import_data = Data()
# import_data.get_information_product()
import_data.products_dict_to_query()

# connection.category_mapping()