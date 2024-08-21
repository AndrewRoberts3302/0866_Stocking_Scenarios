# d_aggregate_data_removing_product_id.py

from c_remove_duplicates import csdi

# Aggregate the data to remove the product id level of granularity

csdi = csdi.groupby(
    [
        "date",
        "product_id",
        "outlet",
        "tenure",
        "segment",
        "region",
        "quality",
        "data_partner",
        "product",
        "product_class",
        "product_group"
        # "cider_exclusive"
        ]
).agg(
    {
        "volume": ["sum"]
    }
)
csdi.columns = csdi.columns.get_level_values(0)
csdi = csdi.reset_index()

