import pandas as pd

from connection import engine

sql_query = f"""
select distinct ProductId as product_id, 
  ProductDescription as product_description,
  ClassificationLevel3Description as product_ladder
from GB_BI_DATA_LIVE.dbo.vw_MCBC_LADDER_A
where D_Datekey >= '2023-05-01'
order by product_id asc;
"""

mcbc_products = pd.read_sql(sql_query, engine)
print(mcbc_products.head())