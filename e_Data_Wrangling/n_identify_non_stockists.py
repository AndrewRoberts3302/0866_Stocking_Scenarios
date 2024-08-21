import pandas as pd
import numpy as np

from m_identify_control_product_stocking import df

from d_Data_Wrangling_Reduction.a_parameters_EDIT_THIS import activation_product, control_product

# Count the number of dates in the data.


# Identify continuous stockists of the activation product

print(df.head(2))

# Take the outlet list.
o = df[["outlet"]].drop_duplicates()

# Identify outlets stocking date count of the activation product
a = df.loc[df["product"] == activation_product]  # Limit the data to that which has the product in.

a = a.groupby(
    [
        "outlet"
        ]
).agg(
    {
        "date": pd.Series.nunique
    }
)
a.columns = a.columns.get_level_values(0)
a = a.reset_index()

o = pd.merge(
    o, a,
    left_on=["outlet"],
    right_on=["outlet"],
    how="left"
)

o = o.fillna(0)

o = o.rename(columns={"date": "date_count_of_activation_product_stocks"})

df = pd.merge(
    df, o,
    left_on=["outlet"],
    right_on=["outlet"],
    how="inner"
)

# Identify outlets stocking date count of the control product

o = df[["outlet"]].drop_duplicates()

a = df.loc[df["product"] == control_product]  # Limit the data to that which has the product in.

a = a.groupby(
    [
        "outlet"
        ]
).agg(
    {
        "date": pd.Series.nunique
    }
)
a.columns = a.columns.get_level_values(0)
a = a.reset_index()

o = pd.merge(
    o, a,
    left_on=["outlet"],
    right_on=["outlet"],
    how="left"
)

o = o.fillna(0)

o = o.rename(columns={"date": "date_count_of_control_product_stocks"})

df = pd.merge(
    df, o,
    left_on=["outlet"],
    right_on=["outlet"],
    how="inner"
)

# Fill the nulls.
df[
    [
        "product_comp_stocks_activation_product",
        "product_act_stocks_activation_product",
        "product_comp_stocks_control_product",
        "product_act_stocks_control_product"
    ]
] = df[
    [
        "product_comp_stocks_activation_product",
        "product_act_stocks_activation_product",
        "product_comp_stocks_control_product",
        "product_act_stocks_control_product"
    ]
].fillna(value="non_stockist")
