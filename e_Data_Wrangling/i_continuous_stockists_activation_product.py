import pandas as pd

from d_Data_Wrangling_Reduction.a_parameters_EDIT_THIS import activation_product
from h_continuous_stockists_control_product import df

# Count the number of dates in the data.

u = len(pd.unique(df["date"]))
print("\nThe number of unique dates in the data is:\n", u, "\n")

# Find outlets with continuous supply of the control product

cs = df.loc[df["product"] == activation_product]

cs = cs[["outlet", "date"]]
cs = cs.drop_duplicates()

cs = cs.groupby(
    [
        "outlet"
        ]
).agg(
    {"date": "nunique"}
)
cs.columns = cs.columns.get_level_values(0)
cs = cs.reset_index()

cs = cs[(cs["date"] == u)]

cs = cs[["outlet"]].copy()

# Add the is_continuous_control column.

cs["is_continuous_activation"] = 1

df = pd.merge(
    df, cs,
    left_on=["outlet"],
    right_on=["outlet"],
    how="left"
)

df[["is_continuous_activation"]] = df[["is_continuous_activation"]].fillna(value=0)
