import pandas as pd

from d_Data_Wrangling_Reduction.a_parameters_EDIT_THIS import control_product
from g_continuous_outlet_data import df

# Count the number of dates in the data.

u = len(pd.unique(df["date"]))
print("\nThe number of unique dates in the data is:\n", u, "\n")

# Find outlets with continuous supply of the control product

cs = df.loc[df["product"] == control_product]

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

cs["is_continuous_control"] = 1

df = pd.merge(
    df, cs,
    left_on=["outlet"],
    right_on=["outlet"],
    how="left"
)

df[["is_continuous_control"]] = df[["is_continuous_control"]].fillna(value=0)
