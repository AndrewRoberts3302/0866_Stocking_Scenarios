import pandas as pd

from connection import engine

sql_query = f"""
	select distinct D_DateKey as date,
    OT_CGAIdent as outlet,
    PM_ProductItemId as product_id,
    PT_ClassificationLevel1Description as product2
    from DI_LIVE.dbo.vw_DI_Heineken
	where D_DateKey >= N'2024-04-01'

"""

heineken_products_di = pd.read_sql(sql_query, engine)
print(heineken_products_di.head(2))

