import numpy as np

from d_update_custom_segments_OPTION import df

# Check the unique regions.
u = df["region"].unique()
print("\nThe unique regions in the data are:\n", sorted(u), "\n")

# Assign regions.
conditions = [
    (df["region"] == "Central"),
    (df["region"] == "East"),
    (df["region"] == "Lancashire"),
    (df["region"] == "London"),
    (df["region"] == "North East"),
    (df["region"] == "Scotland"),
    (df["region"] == "South & South East"),
    (df["region"] == "South West"),
    (df["region"] == "Wales"),
    (df["region"] == "Yorkshire"),

    (df["region"] == "Rest of GB")  # Added in to accomodate a client request when London is compared to the rest of GB

    ]
choices = [
    "Central / Wales",
    "Central / Wales",
    "North",
    "London",
    "North",
    "Scotland",
    "South",
    "South",
    "Central / Wales",
    "North",

    "Rest of GB"   # Added in to accomodate a client request when London is compared to the rest of GB

    ]
df["region"] = np.select(conditions, choices)

# Check the updated regions.
u = df["region"].unique()
print("\nThe unique regions in the data are now reassigned as:\n", sorted(u), "\n")

print(df.head(100))