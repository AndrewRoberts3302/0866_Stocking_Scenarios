import pandas as pd

from f_eda import df

# Check the outlet counts before continuous supply.
n = len(pd.unique(df["outlet"]))
print("\nThe number of outlets in the data before enforcing continuous supply on the outlets is:", n, "\n")

# Count the number of dates in the data.
u = len(pd.unique(df["date"]))
print("\nThe number of unique dates in the data is:\n", u, "\n")

# Find outlets with continuous data feeds.

cs = df[["outlet", "date"]]
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

df = pd.merge(
    df, cs,
    left_on=["outlet"],
    right_on=["outlet"],
    how="inner"
)

# Check the outlet counts after continuous supply.
n = len(pd.unique(df["outlet"]))
print("\nThe number of outlets in the data after enforcing continuous supply on the outlets is:", n, "\n")

print(df.head(20))