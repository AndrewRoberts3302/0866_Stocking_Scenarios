import pandas as pd

from g_ros import ros
from h_nda_shares import nda
from l_append_share_results import sh

# Check the heads of the results before merging.

print("\nCheck the results before merging.\n")
print("\nThe head of ros is:\n", ros.head(2), "\n")
print("\nThe head of nda is:\n", nda.head(2), "\n")
print("\nThe head of sh is:\n", sh.head(2), "\n")

results = pd.merge(
    ros, nda,
    left_on=["qtr", "market", "scenario", "product"],
    right_on=["qtr", "market", "scenario", "product"],
    how="inner"
)

results = pd.merge(
    results, sh,
    left_on=["qtr", "market", "scenario", "product"],
    right_on=["qtr", "market", "scenario", "product"],
    how="left"
)

# Change the order of the columns.
results = results[[
    "qtr",
    "market",
    "scenario",
    "product",
    "ros_volume",
    "ros_value",
    "nda_outlet_count",
    "nda_data_partner_count",
    "nda_max_data_partner_volume_share",
    "nda_max_share_data_partner",
    "share_in_class_volume",
    "share_in_group_volume",
    "share_in_class_value",
    "share_in_group_value"
    ]]

######################################################
# cider only
#
# results = results.groupby([
#     "qtr", "market", "scenario", "product",
#     "ros_volume", "ros_value", "nda_outlet_count", "nda_data_partner_count",
#     "nda_max_data_partner_volume_share", "nda_max_share_data_partner"
# ]).agg({
#     "share_in_group_volume": "sum",
#     "share_in_group_value": "sum"
# }).reset_index()
