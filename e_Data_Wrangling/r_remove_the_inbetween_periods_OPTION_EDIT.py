from q_clean_the_data import df

# OPTION - Comment out if not required.

# Limit the data to the two periods of interest and remove the inbetween period.
df = df.loc[
    (df["qtr"].isin([1, 5]))
].copy()

print(df.head(100))

