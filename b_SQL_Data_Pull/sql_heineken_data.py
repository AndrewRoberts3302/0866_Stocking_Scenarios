import pandas as pd

from connection import engine

sql_query = f"""
select distinct D_DateKey as date,
    OT_CGAIdent as outlet,
    PM_ProductItemId as product_id,
    PT_ClassificationLevel1Description as product2
    from CS_LIVE.dbo.vw_CS_HUK
    where D_DateKey >= N'2024-04-01'

"""

heineken_products_cs = pd.read_sql(sql_query, engine)
print(heineken_products_cs.head(2))



