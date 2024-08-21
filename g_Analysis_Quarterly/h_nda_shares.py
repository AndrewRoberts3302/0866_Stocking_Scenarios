import pandas as pd

from g_ros import df

print(df.head(2))

dp_volumes = df.groupby(
    [
        "qtr", "market", "product", "data_partner", "scenario"
        ]
).agg(
    {
        "volume": ["sum"]
    }
)
dp_volumes.columns = dp_volumes.columns.get_level_values(0)
dp_volumes = dp_volumes.reset_index()
dp_volumes = dp_volumes.rename(
    columns={
        "volume": "dp_volume"
    }
)

total_volumes = dp_volumes.groupby(
    [
        "qtr", "market", "product", "scenario"
        ]
).agg(
    {
        "dp_volume": ["sum"]
    }
)
total_volumes.columns = total_volumes.columns.get_level_values(0)
total_volumes = total_volumes.reset_index()
total_volumes = total_volumes.rename(
    columns={
        "dp_volume": "total_volume"
    }
)

dp_volumes = pd.merge(
    dp_volumes, total_volumes,
    left_on=[
        "qtr", "market", "product", "scenario"
    ],
    right_on=[
        "qtr", "market", "product", "scenario"
    ],
    how="inner"
)

dp_volumes["dp_share"] = dp_volumes["dp_volume"] / dp_volumes["total_volume"]

dp_volumes["rank"] = dp_volumes.groupby(
    [
        "qtr", "market", "product", "scenario"
    ])["dp_share"].rank(ascending=False, method="first")

# dp_volumes["rank"] = dp_volumes["rank"].astype(int)

u = dp_volumes['rank'].unique()
print('The unique values in df rank are: \n', sorted(u), '\n')

dp_volumes = dp_volumes.loc[dp_volumes["rank"] == 1]

dp_volumes = dp_volumes.rename(
    columns={
        "data_partner": "nda_max_share_data_partner",
        "dp_share": "nda_max_data_partner_volume_share"
    }
)

nda = dp_volumes[[
    "qtr", "market", "product", "scenario",
    "nda_max_data_partner_volume_share",
    "nda_max_share_data_partner"
]]
