import pandas as pd

from d_data_enrichment import df

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

# Tenure.
tenure = df[[
    "date", "outlet", "tenure", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"
    ]]
tenure = tenure.rename(
    columns={
        "tenure": "market"
    }
)
tenure["market"] = "Tenure | " + tenure["market"]

# Segment.
segment = df[[
    "date", "outlet", "segment", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"
    ]]
segment = segment.rename(
    columns={
        "segment": "market"
    }
)
segment["market"] = "Segment | " + segment["market"]

# Region.
region = df[[
    "date", "outlet", "region", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"
    ]]
region = region.rename(
    columns={
        "region": "market"
    }
)
region["market"] = "Region | " + region["market"]

# Country.
country = df[[
    "date", "outlet", "country", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"
    ]]
country = country.rename(
    columns={
        "country": "market"
    }
)
country["market"] = "Country | " + country["market"]

# Quality.
quality = df[[
    "date", "outlet", "quality", "data_partner", "product", "product_class", "product_group", "volume", "value", "scenario"
    ]]
quality = quality.rename(
    columns={
        "quality": "market"
    }
)
quality["market"] = "Quality | " + quality["market"]

df = pd.concat([tenure, segment, region, country, quality], axis=0)
