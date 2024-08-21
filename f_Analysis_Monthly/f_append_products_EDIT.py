import pandas as pd

from e_append_market_data_slices_OPTION_1 import df
# from e_dont_append_market_data_slices_GB_only_OPTION_2 import df
from a_import_parameters import control_product, activation_product

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

product = df.loc[df["product"].isin([control_product, activation_product])]  # Limit the data to that which has the products in.
product = product[["date", "outlet", "market", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"]]
product["share_group"] = 1

product_class = df[["date", "outlet", "market", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"]]
product_class["product"] = product_class["product_class"]
# product_class = product_class.rename(columns={"product_class": "product"})
product_class["share_group"] = 2

product_group = df[["date", "outlet", "market", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"]]
product_group["product"] = product_group["product_group"]
product_group["product_class"] = product_group["product_group"]
# product_group = product_group.rename(columns={"product_group": "product"})
product_group["share_group"] = 3

df = pd.concat([product, product_class, product_group], axis=0)

print(df.head(200))

