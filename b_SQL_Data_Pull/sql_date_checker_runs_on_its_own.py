import pandas as pd

from connection import engine

sql_query_cs_date_check = f"""
select max(D_DateId) as most_recent_cs_date
from CS_LIVE.dbo.vw_CS
where D_DateId >= 20230101
"""

sql_query_di_date_check = f"""
select max(D_DateId) as most_recent_di_date
from DI_LIVE.dbo.vw_DI
where D_DateId >= 20230101
"""

cs = pd.read_sql(sql_query_cs_date_check, engine)
di = pd.read_sql(sql_query_di_date_check, engine)

print("\nThe most recent CS data date is:\n", cs, "\n")
print("\nThe most recent DI data date is:\n", di, "\n")
