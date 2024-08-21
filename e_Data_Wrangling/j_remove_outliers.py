# Remove outliers based on the product group volumes and the segment for the whole time frame.
# We can't remove outliers based on dates because we're actively looking for outliers in the results.

import numpy as np
import pandas as pd

from i_continuous_stockists_activation_product import df

# Check the outlet counts before removing outliers.
n = len(pd.unique(df["outlet"]))
print("\nThe number of outlets in the data before removing outliers is:", n, "\n")


# Aggregate the columns required.

ag = df.groupby(
    [
        "outlet",
        "segment",
        "region",
        "quality",
        "product_group"
        ]
).agg(
    {
        "volume": ["sum"]
    }
)
ag.columns = ag.columns.get_level_values(0)
ag = ag.reset_index()

# Mean and standard deviations.

msd = ag.groupby(
    [
        "segment",
        "region",
        "quality",
        "product_group"
        ]
).agg(
    {
        "volume": ["mean", np.std],
        "outlet": pd.Series.nunique
    }
)
msd.columns = msd.columns.map("|".join).str.strip("|")
msd = msd.reset_index()
msd = msd.rename(
    columns={
        "outlet|nunique": "outlet|count"
    }
)

# Results with one outlet won't have standard deviations, remove those.
msd = msd.loc[msd["outlet|count"] > 1]

# Merge and calculate z-scores

z = pd.merge(
    ag, msd,
    left_on=[
        "segment",
        "region",
        "quality",
        "product_group"
        ],
    right_on=[
        "segment",
        "region",
        "quality",
        "product_group"
        ],
    how="inner"
)

z["z_score"] = (z["volume"] - z["volume|mean"]) / z["volume|std"]
z["z_score"] = z["z_score"].abs()

# Take the acceptable rows.
z = z.loc[z["z_score"] < 3]

# Take the columns required for merging.
z = z[[
    "outlet",
    "segment",
    "region",
    "quality",
    "product_group"
    ]]

# Merge the acceptable rows with the data.
df = pd.merge(
    df, z,
    left_on=[
        "outlet",
        "segment",
        "region",
        "quality",
        "product_group"
        ],
    right_on=[
        "outlet",
        "segment",
        "region",
        "quality",
        "product_group"
        ],
    how="inner"
)

# Check the outlet counts before removing outliers.
n = len(pd.unique(df["outlet"]))
print("\nThe number of outlets in the data after removing outliers is:", n, "\n")
