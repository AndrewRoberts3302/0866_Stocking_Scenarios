"""

Run times:
strongbow csdi
from sql_query_lad_csdi import data_lad_csdi : about 1 minute

"""

from a_Data_Path.a_data_path import data_path
# from pathlib import Path

# from sql_query_strongbow_csdi import data_strongbow_csdi # NOT USED
# from sql_query_lad_csdi import data_lad_csdi # NOT USED
from sql_query_lad_cs import data_lad_cs
from sql_query_lad_di import data_lad_di
from sql_mcbc_custom_product_data_pull import mcbc_products
# from sql_cmbc_cuk_product_segments import cmbc_cuk_products
# from sql_mcbc_custom_outlet_data_pull import mcbc_outlets
# from sql_craft_beer import craft_update
# from sql_spec_beer import Spec_beer_products
# from EPOS_data_pull import EPOS_data
# from sql_heineken_data import heineken_products_cs
# from sql_heineken_data2 import heineken_products_di

# cwd = Path(__file__).parent

# data_strongbow_csdi.to_csv(data_path / "data_strongbow.csv", index=False) # NOT USED
# data_lad_csdi.to_csv(data_path / "data_lad_csdi.csv", index=False) # NOT USED
data_lad_cs.to_csv(data_path / "data_cs.csv", index=False)
data_lad_di.to_csv(data_path / "data_di.csv", index=False)
# mcbc_outlets.to_csv(data_path / "mcbc_outlet_data.csv", index=False)
mcbc_products.to_csv(data_path / "mcbc_product_data.csv", index=False)
# cmbc_cuk_products.to_csv(data_path / "cmbc_cuk_product_data.csv", index=False)
# craft_update.to_csv(data_path / "craft_update_data.csv", index=False)
# Spec_beer_products.to_csv(data_path / "Spec_beer_products.csv", index=False)
# EPOS_data.to_csv(data_path / "EPOS_data.csv", index=False)
# heineken_products_cs.to_csv(data_path / "heineken_products_cs.csv", index=False)
# heineken_products_di.to_csv(data_path / "heineken_products_di.csv", index=False)


# print(heineken_products_cs.head(5))
# print(heineken_products_di.head(5))
print(data_lad_cs.head(50))
print(data_lad_di.head(50))

