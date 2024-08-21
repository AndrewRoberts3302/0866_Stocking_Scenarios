import pandas as pd

from connection import engine

sql_query = f"""
select distinct CGAIdent as CGAIdent,
  NovellusSegmentationLevel2Id as PT_Segment
from GB_BI_DATA_LIVE.dbo.vw_MCBC_LADDER_A
where D_Datekey >= '2022-09-01'
order by CGAIdent asc;
"""

mcbc_outlets = pd.read_sql(sql_query, engine)
