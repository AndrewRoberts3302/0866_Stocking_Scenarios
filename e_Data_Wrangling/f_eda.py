import pandas as pd

from d_Data_Wrangling_Reduction.a_parameters_EDIT_THIS import control_product
from a_read_in_the_data import df

# Check the head of the data.
print("\nThe head of df, the csdi data is:\n", df.head(2), "\n")

# Check the dates in the data.
u = df["date"].unique()
print("\nThe unique dates in the data are:\n", sorted(u), "\n")

# Count the number of outlets in the data.
n = len(pd.unique(df["outlet"]))
print("\nThe number of outlets in the data is:", n, "\n")

a = df.loc[df["product"] == control_product]
n = len(pd.unique(a["outlet"]))
print("\nThe number of outlets with the product in the data is:", n, "\n")

# Check the segments in the data.
u = df["segment"].unique()
print("\nThe unique segments in the data are:\n", sorted(u), "\n")

# Check the regions in the data.
u = df["region"].unique()
print("\nThe unique regions in the data are:\n", sorted(u), "\n")

print(df.head(20))
