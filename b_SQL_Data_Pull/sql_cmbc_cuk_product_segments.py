import pandas as pd

from connection import engine

sql_query = f"""
select distinct ProductId, ProductDescription, PT_Segment, PT_SubSegment
from GB_BI_DATA_LIVE.dbo.vw_CUK_PCW_B
where D_DateKey > '2023-01-01'
order by ProductId asc;
"""


cmbc_cuk_products = pd.read_sql(sql_query, engine)