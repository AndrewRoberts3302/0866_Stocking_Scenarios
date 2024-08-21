import pandas as pd

from connection import engine

sql_query = f"""
select distinct  ProductDescription, PT_Segment, PT_SubSegment, ClassificationLevel5Description, ClassificationLevel4Description
from GB_BI_DATA_LIVE.dbo.vw_CUK_PCW_A
where D_DateKey > '2023-03-01'
"""


Spec_beer_products = pd.read_sql(sql_query, engine)