import pandas as pd

from j_remove_outliers import df

# Reformat the date from dateteime to date.
df["date"] = pd.to_datetime(df["date"]).dt.date

# Add in months.
dk = pd.DataFrame(df[["date"]])
dk = dk.drop_duplicates()
dk = dk.sort_values(by=["date"], ascending=[True])
dk = dk.reset_index()
dk["month"] = dk.index + 1

# Add in quarters.
dk["ref_den_mon"] = dk.index + 3
dk["qtr"] = dk["ref_den_mon"] / 3
dk["qtr"] = dk["qtr"].astype(int)

# Take the columns needed.
dk = dk[["date", "month", "qtr"]]

# Merge with the data.

df = pd.merge(
    df, dk,
    left_on=["date"],
    right_on=["date"],
    how="inner"
)

print("\nThe head of df after date enrichment is:\n", df.head(2), "\n")
