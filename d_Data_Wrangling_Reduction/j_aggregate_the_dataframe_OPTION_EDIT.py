import numpy as np

from h_update_columns_values_OPTION_EDIT import df
from a_parameters_EDIT_THIS import control_product, activation_product
from a_Data_Path.a_data_path import data_path

# Update the products that aren't the activation product or the control product.
conditions = [
    ((df["product"] == activation_product) | (df["product"] == control_product)),
    ((df["product"] != activation_product) & (df["product"] != control_product))
    ]
choices = [
    df["product"], "Other product"
    ]
df["product"] = np.select(conditions, choices)

u = df['product'].unique()
print('The unique product values in df are: \n', sorted(u), '\n')


df.to_csv(data_path / "data_reduced_QC.csv", index=False)

# Aggregate the data

df = df.groupby(
    [
        "date",
        "outlet",
        "tenure",
        "segment",
        "region",
        "quality",
        "data_partner",
        "product",
        "product_class",
        "product_group",
    ]
).agg(
 {
        "volume": "sum",
        "value": "sum"
    }
)
df.columns = df.columns.get_level_values(0)
df = df.reset_index()

print(df.head(20))

u = df['product'].unique()
print('The unique product values in df are: \n', sorted(u), '\n')

