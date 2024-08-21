import pandas as pd

from connection import engine

sql_query = f"""
with c as 
(
select distinct coalesce(PT_AT_CraftBeer, N'Unknown') as product_class, 
  PT_ProductDescription as product
from PL_LIVE.dbo.vw_Product
where PT_ClassificationLevel5Description = N'Total Beer'
) 
select distinct
case when product_class = N'N/A' then N'Unknown'
  else product_class
  end as product_class,
    product
from c;
"""

craft_update = pd.read_sql(sql_query, engine)
print(craft_update.head(5))