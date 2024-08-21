import pandas as pd

from f_append_products_EDIT import df

# We need to import a dataframe before the products are appended.

# Products

sh = df.loc[df["share_group"] == 2].copy()

sh = sh.groupby(
    [
        "qtr", "market", "product", "product_class", "product_group", "scenario"
    ]
).agg(
    {
        "volume": "sum",
        "value": "sum"
    }
)
sh.columns = sh.columns.get_level_values(0)
sh = sh.reset_index()
sh = sh.rename(
    columns={
        "volume": "product_volume",
        "value": "product_value"
    }
)


# Product class

pc = df.loc[df["share_group"] == 2]
pc = pc.groupby(
    [
        "qtr", "market", "product_class", "scenario"
    ]
).agg(
    {
        "volume": "sum",
        "value": "sum"
    }
)
pc.columns = pc.columns.get_level_values(0)
pc = pc.reset_index()
pc = pc.rename(
    columns={
        "volume": "product_class_volume",
        "value": "product_class_value"
    }
)

# Product group

pg = df.loc[df["share_group"] == 3]
pg = pg.groupby(
    [
        "qtr", "market", "product_group", "scenario"
    ]
).agg(
    {
        "volume": "sum",
        "value": "sum"
    }
)
pg.columns = pg.columns.get_level_values(0)
pg = pg.reset_index()
pg = pg.rename(
    columns={
        "volume": "product_group_volume",
        "value": "product_group_value"
    }
)

sh = pd.merge(
    sh, pc,
    left_on=["qtr", "market", "product_class", "scenario"],
    right_on=["qtr", "market", "product_class", "scenario"],
    how="inner"
)

sh = pd.merge(
    sh, pg,
    left_on=["qtr", "market", "product_group", "scenario"],
    right_on=["qtr", "market", "product_group", "scenario"],
    how="inner"
)

sh["share_in_class_volume"] = sh["product_volume"] / sh["product_class_volume"]
sh["share_in_group_volume"] = sh["product_volume"] / sh["product_group_volume"]
sh["share_in_class_value"] = sh["product_value"] / sh["product_class_value"]
sh["share_in_group_value"] = sh["product_value"] / sh["product_group_value"]

sh_2 = sh[[
    "qtr", "market", "product", "scenario",
    "share_in_class_volume", "share_in_group_volume",
    "share_in_class_value", "share_in_group_value"
    ]]
