import pandas as pd

from connection import engine

from sql_parameters_EDIT_THIS import (
    start_date, end_date, product_class, product_group, serve_format, serve_format_predicate,  product_group_predicate,
    di_database
)

sql_query = f"""
select distinct d.D_DateKey as date,
    d.OT_CGAIdent as outlet,
    o.OT_TenureDescription as tenure,
	o.OT_SL2_Novellus as segment,
	o.OT_TL2_Novellus as region,
	o.OT_Quality_CGA as quality,
	d.PI_ClientDescription as data_partner,
	d.PM_ProductItemId as product_id,
	d.PT_AT_Segment as product,
	d.{product_class} as product_class,
	d.{product_group} as product_group,
	-- d.PT_ClassificationLevel5Description as cider_exclusive,
	sum(d.F_VolumeHL) as volume
from {di_database} as d
    inner join OI_LIVE.dbo.vw_outlet as o
	    on d.OT_CGAIdent = o.OT_CGAIdent
where d.D_DateId >= {start_date}
    and d.D_DateId < {end_date}
	and d.OT_CGAIdent > 0
	and d.OT_TL5_ISBA = N'GB'
	and o.OT_TL2_Novellus != N'Unknown'
	and d.PT_ProductId > 0
	and d.{serve_format} = N'{serve_format_predicate}'
	-- and d.{product_group} = N'{product_group_predicate}'
group by d.D_DateKey,
    d.PT_AT_Segment,
    d.OT_CGAIdent,
    o.OT_TenureDescription,
	o.OT_SL2_Novellus,
	o.OT_TL2_Novellus,
	o.OT_Quality_CGA,
	d.PI_ClientDescription,
	d.PM_ProductItemId,
	d.PT_ClassificationLevel1Description,
	d.{product_class},
	d.{product_group}
	-- d.PT_ClassificationLevel5Description
order by date asc, outlet asc, product_id asc;  -- only in place to help validate d
"""

data_lad_di = pd.read_sql(sql_query, engine)