"""
Because the process reports on value data when epos data is used,
we need to add in a value column.
In this case we just duplicate the volume column.
"""
from d_aggregate_data_removing_product_id import csdi

csdi["value"] = csdi["volume"]




