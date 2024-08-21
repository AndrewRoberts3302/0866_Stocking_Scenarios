import pandas as pd

from b_review_the_data import cs, di

# Take the columns required to remove duplicates.
cs_d = cs[["date", "outlet", "product_id"]]
di_d = di[["date", "outlet", "product_id"]]

# Merge the data.
du = di_d.reset_index().merge(
    cs_d,
    left_on=["date", "outlet", "product_id"],
    right_on=["date", "outlet", "product_id"],
    how="inner"
).set_index("index")

# Drop the duplicates from the di data.
di = di.drop(du.index, axis=0)

# Append the data.
csdi = pd.concat([cs, di], axis=0, ignore_index=True)



