import numpy as np

from p_append_scenarios import df
from d_Data_Wrangling_Reduction.a_parameters_EDIT_THIS import control_product, activation_product

print(df.head(2))

df = df[[
    "qtr",
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
    "volume",
    "value",
    "scenario"
    ]].copy()

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

# Perform a final aggregation.

df = df.groupby(
    [
        "qtr",
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
        "scenario"
        ]
).agg(
    {
        "volume": "sum",
        "value": "sum"
    }
)
df.columns = df.columns.get_level_values(0)
df = df.reset_index()

