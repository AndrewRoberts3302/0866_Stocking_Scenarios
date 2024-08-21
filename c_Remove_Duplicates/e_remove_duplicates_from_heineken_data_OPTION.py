# import pandas as pd
#
# from a_read_in_the_data_PARAMETERS import h_cs, h_di
#
# # Take the columns required to remove duplicates.
# h_cs = h_cs[["date", "outlet", "product_id", "product2"]]
# h_di = h_di[["date", "outlet", "product_id", "product2"]]
#
# # Merge the data.
# du = h_di.reset_index().merge(
#     h_cs,
#     left_on=["date", "outlet", "product_id", "product2"],
#     right_on=["date", "outlet", "product_id", "product2"],
#     how="inner"
# ).set_index("index")
#
# # Drop the duplicates from the di data.
# h_di = h_di.drop(du.index, axis=0)
#
# # Append the data.
# heineken_csdi = pd.concat([h_cs, h_di], axis=0, ignore_index=True)
#
#
# print(heineken_csdi.head(10))