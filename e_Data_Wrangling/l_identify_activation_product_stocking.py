import pandas as pd
import numpy as np

# Identify outlets which stock the activation product.

from d_Data_Wrangling_Reduction.a_parameters_EDIT_THIS import activation_product

from k_date_enrichments import df

print(df.shape)

# Identify the month counts in each quarter.

a = df.loc[df["product"] == activation_product]  # Limit the data to that which has the product in.

a = a.groupby(
    [
        "outlet", "qtr"
        ]
).agg(
    {
        "month": pd.Series.nunique
    }
)
a.columns = a.columns.get_level_values(0)
a = a.reset_index()

# Identify the stocking status in the comp period.

c = a.loc[a["qtr"] == 1].copy()

conditions = [
    (c["month"] == 3),
    (c["month"] < 3)

]
choices = [
    "comp_cont",  # Outlet continually stocked the product in the comparison period.
    "comp_non_cont",  # Outlet stocked (but not continuously) the product in the comparison period.
]

c["product_comp_stocks_activation_product"] = np.select(conditions, choices)

# Reduce the columns.
c = c[["outlet", "product_comp_stocks_activation_product"]]

# Merge back with the data.

df = pd.merge(
    df, c,
    left_on=["outlet"],
    right_on=["outlet"],
    how="left"
)

# Identify the stocking status in the act period.

c = a.loc[a["qtr"] == 5].copy()

conditions = [
    (c["month"] == 3),
    (c["month"] < 3)

]
choices = [
    "act_cont",  # Outlet continually stocked the product in the comparison period.
    "act_non_cont",  # Outlet stocked (but not continuously) the product in the comparison period.
]

c["product_act_stocks_activation_product"] = np.select(conditions, choices)

# Reduce the columns.
c = c[["outlet", "product_act_stocks_activation_product"]]

# Merge back with the data.

df = pd.merge(
    df, c,
    left_on=["outlet"],
    right_on=["outlet"],
    how="left"
)
