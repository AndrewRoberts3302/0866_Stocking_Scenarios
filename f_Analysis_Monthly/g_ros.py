import pandas as pd

from f_append_products_EDIT import df

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

ros = df.groupby(
    [
        "date", "market", "product", "scenario"
        ]
).agg(
    {
        "volume": "sum",
        "value": "sum",
        "outlet": pd.Series.nunique,
        "data_partner": pd.Series.nunique
    }
)
ros.columns = ros.columns.get_level_values(0)
ros = ros.reset_index()

ros = ros.rename(
    columns={
        "outlet": "nda_outlet_count",
        "data_partner": "nda_data_partner_count"
    }
)
ros["ros_volume"] = ros["volume"] / ros["nda_outlet_count"]
ros["ros_value"] = ros["value"] / ros["nda_outlet_count"]

ros = ros[[
    "date", "market", "product", "scenario",
    "ros_volume", "ros_value",
    "nda_outlet_count", "nda_data_partner_count"
    ]]

