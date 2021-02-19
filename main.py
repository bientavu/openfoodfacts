from core.database import Sql
from core.managers import CategoryManager

# connection = Sql()
# connection.dbinit()

import_data = CategoryManager()
import_data.category_table_mapping()
# import_data.get_information_product3()
# import_data.products_dict_to_query()

# connection.category_mapping()