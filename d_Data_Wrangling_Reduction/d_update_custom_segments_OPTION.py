import pandas as pd
import numpy as np

from c_identify_products_RUN_THIS_WHEN_IDENTIFYING_PRODUCTS import df, huk_segment, mcbc_outlets

# Check the unique segments.
u = df["segment"].unique()
print("\nThe unique segments in the data are:\n", sorted(u), "\n")

####################################################################
# df = df.drop(
#     [
#         "segment"
#         ], axis=1
# )
# mcbc_outlets = mcbc_outlets.rename(
#     columns={
#         "PT_Segment": "segment",
#         "CGAIdent": "outlet"
#     }
# )
#
# df = pd.merge(
#     df, mcbc_outlets,
#     left_on=["outlet"],
#     right_on=["outlet"],
#     how="inner"
# )
#
# ##############################################################################
# Update with a merge from the HUK dataframe.

# df = df.drop(
#     [
#         "segment"
#         ], axis=1
# )
#
# huk_segment = huk_segment.rename(
#     columns={
#         "HUKSegment": "segment",
#         "CGAIdent": "outlet"
#     }
# )
#
# df = pd.merge(
#     df, huk_segment,
#     left_on=["outlet"],
#     right_on=["outlet"],
#     how="inner"
# )
##############################################################################

##############################################################################
# Update with conditions and choices.
# SB153 MCBC Premium Lager project.

# Assign segments.
# conditions = [
#     (df["segment"] == "Bar"),
#     (df["segment"] == "Bar Restaurant"),
#     (df["segment"] == "Cafe/Delicatessen"),
#     (df["segment"] == "Casual Dining Restaurant"),
#     (df["segment"] == "Community Pub"),
#     (df["segment"] == "Food Pub"),
#     (df["segment"] == "Guest/Boarding House"),
#     (df["segment"] == "High Street Pub"),
#     (df["segment"] == "Holiday/Caravan Park"),
#     (df["segment"] == "Hotel"),
#     (df["segment"] == "Large Venue"),
#     (df["segment"] == "Nightclub"),
#     (df["segment"] == "Restaurant"),
#     (df["segment"] == "Sports/Social Club")
#     ]
# choices = [
#     "Wet",
#     "Mixed",
#     "Other",
#     "Dry",
#     "Wet",
#     "Mixed",
#     "Other",
#     "Wet",
#     "Other",
#     "Mixed",
#     "Mixed",
#     "Wet",
#     "Dry",
#     "Wet"
#     ]
# df["segment"] = np.select(conditions, choices)
##############################################################################

##############################################################################
# Check the updated segments.
u = df["segment"].unique()
print("\nThe unique segments in the data are now reassigned as:\n", sorted(u), "\n")

print(df.head(100))
