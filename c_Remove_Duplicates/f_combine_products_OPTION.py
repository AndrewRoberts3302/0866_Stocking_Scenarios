import pandas as pd
from e_add_value_column import csdi
from a_Data_Path.a_data_path import data_path
print(csdi.head(2))


# Replace "Guinness Draught" with "Guinness"
# csdi['product'] = csdi['product'].replace('Guinness Draught', 'Guinness')


# Reorder and select columns
csdi = csdi[[
    "date",
    "product_id",
    "outlet",
    "tenure",
    "segment",
    "region",
    "quality",
    "data_partner",
    "product",
    "product_class",
    "product_group",
    # "cider_exclusive",
    "volume",
    "value"
]].reset_index(drop=True)  # Reset index without adding a new column

print('CSDI data is')
print(csdi.head(20))
##################################################################################
# # Cider only
# data_outlet= "717_Cider_removal1.csv"
# outlet_keep = pd.read_csv(f"{data_path}/{data_outlet}")
# print(outlet_keep.head(100))
#
# import pandas as pd
#
# # Assuming both dataframes have a column named 'outlet' that contains the outlet IDs
#
# # Perform inner join between 'csdi' and 'outlet_removal' on the 'outlet' column
# csdi = pd.merge(csdi, outlet_keep, on='outlet', how='inner')
#
# # Now, 'filtered_csdi' will contain only the outlets from 'csdi' that are also in 'outlet_removal'
# print(csdi.head(300))






