import numpy as np

from e_update_custom_regions_OPTION import df

# Check the unique qualities.
u = df["quality"].unique()
print("\nThe unique qualities in the data are:\n", sorted(u), "\n")

# Assign qualities.
conditions = [
    (df["quality"] == "Bronze"),
    (df["quality"] == "Gold"),
    (df["quality"] == "Platinum"),
    (df["quality"] == "Silver"),
    (df["quality"] == "Unknown")
    ]
choices = [
    "Value",
    "Premium",
    "Premium",
    "Mainstream",
    "Unknown"
    ]
df["quality"] = np.select(conditions, choices)

# Check the updated qualities.
u = df["quality"].unique()
print("\nThe unique qualities in the data are now reassigned as:\n", sorted(u), "\n")

print(df.head(100))