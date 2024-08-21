import pandas as pd
from connection import engine
from pathlib import Path

query = f""" 
select distinct d.D_DateKey as date,
    d.OT_CGAIdent as outlet,
    o.OT_TenureDescription as tenure,
	o.OT_SL2_Novellus as segment,
	o.OT_TL2_Novellus as region,
	o.OT_Quality_CGA as quality,
	d.PI_ClientDescription as data_partner,
	d.PM_ProductItemId as product_id,
	d.PT_ProductDescription as product,
	d.PT_ClassificationLevel4Description as product_class,
	d.PT_ClassificationLevel5Description as product_group,
	SUM(d.F_SalesVolume_MLS) as volume,
	SUM([F_SalesValue_£]) as value
from WS_LIVE.dbo.vw_Epos_Weekly as d
    inner join OI_LIVE.dbo.vw_outlet as o
	    on d.OT_CGAIdent = o.OT_CGAIdent
where d.D_DateKey >= '20220901'
    and d.D_DateKey < '20231201'
	and d.OT_CGAIdent > 0
	and d.OT_TL5_ISBA = N'GB'
	and o.OT_TL2_Novellus != N'Unknown'
	and d.PT_ProductId > 0
	and d.PT_ClassificationLevel5Description = N'Total Beer'
	and d.PT_AT_Format = N'Draught'
group by d.D_DateKey,
    d.OT_CGAIdent,
    o.OT_TenureDescription,
	o.OT_SL2_Novellus,
	o.OT_TL2_Novellus,
	o.OT_Quality_CGA,
	d.PI_ClientDescription,
	d.PM_ProductItemId,
	d.PT_ProductDescription,
	d.PT_ClassificationLevel4Description,
	d.PT_ClassificationLevel5Description
order by date asc, outlet asc, product_id asc;  -- only in place to help validate duplicate removal in python.
;
"""

EPOS_data = pd.read_sql(query, engine)