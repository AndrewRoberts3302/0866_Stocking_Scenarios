import pandas as pd

import numpy as np

from n_identify_non_stockists import df

# Identify the unique date counts in df.

print("The columns available in df before assigning scenarios are:\n")
print(df.columns)

# Definitions of the columns used to create the scenarios.

print("\nThere uses are:\n")

print("is_continuous_control states whether the outlet continuously stocks the control product.")
print("is_continuous_activation states whether the outlet continuously stocks the activation product.")
print("product_comp_stocks_activation_product states whether the outlet continuously stocks the activation product in the comparison period.")
print("product_act_stocks_activation_product states whether the outlet continuously stocks the activation product in the activation period.")
print("product_comp_stocks_control_product states whether the outlet continuously stocks the control product in the comparison period.")
print("product_act_stocks_control_product states whether the outlet continuously stocks the control product in the activation period.")
print("date_count_of_activation_product_stocks states how many dates the outlet has stocked the activation product for in the data.")
print("date_count_of_control_product_stocks states how many dates the outlet has stocked the control product for in the data.")

print("\nThe unique values in each of these columns are:\n")
print('The unique values in is_continuous_control are: \n', df['is_continuous_control'].unique(), '\n')
print('The unique values in is_continuous_activation are: \n', df['is_continuous_activation'].unique(), '\n')
print('The unique values in product_comp_stocks_activation_product are: \n', df['product_comp_stocks_activation_product'].unique(), '\n')
print('The unique values in product_act_stocks_activation_product are: \n', df['product_act_stocks_activation_product'].unique(), '\n')
print('The unique values in product_comp_stocks_control_product are: \n', df['product_comp_stocks_control_product'].unique(), '\n')
print('The unique values in product_act_stocks_control_product are: \n', df['product_act_stocks_control_product'].unique(), '\n')
u = df['date_count_of_activation_product_stocks'].unique()
print('The unique values in date_count_of_activation_product_stocks are: \n', sorted(u), '\n')
u = df['date_count_of_control_product_stocks'].unique()
print('The unique values in date_count_of_control_product_stocks are: \n', sorted(u), '\n')

dc = len(pd.unique(df["date"]))

# Add in the scenarios

# Add in columns with positive results for all.

# Original Order:
# df["sc_01"] = "01_continuous_dual_product_stockist"
# df["sc_02"] = "02_removed_activation_product"
# df["sc_03"] = "03_added_activation_product"
# df["sc_04"] = "04_continuous_control_product_solo_stockist"
# df["sc_05"] = "05_control_product_replaced_with_activation_product"
# df["sc_06"] = "06_activation_product_replaced_with_control_product"
# df["sc_07"] = "07_continuous_activation_product_solo_stockist"
# df["sc_08"] = "08_removed_activation_product_regardless"
# df["sc_09"] = "09_added_activation_product_regardless"
# df["sc_10"] = "10_continuous_non_stockist_of_activation_product"
# df["sc_11"] = "11_continuous_non_stockist_of_control_product"
# df["sc_12"] = "12_continuous_dual_product_stockist_01_with_relaxed_middle_period"
# df["sc_13"] = "13_continuous_control_product_solo_stockist_04_with_relaxed_middle_period"
# df["sc_14"] = "14_continuous_activation_product_solo_stockist_07_with_relaxed_middle_period"
# df["sc_15"] = "15_removed_control_product"
# df["sc_16"] = "16_added_control_product"
# df["sc_17"] = "17_activation_product_solo_stocking_last_qtr"
# df["sc_18"] = "18_control_product_solo_stocking_last_qtr"
# df["sc_19"] = "19_dual_stockist_last_qtr"
# df["sc_20"] = "20_activation_product_stockist_last_qtr_regardless"
# df["sc_21"] = "21_control_product_stockist_last_qtr_regardless"
# df["sc_22"] = "22_removed_control_product_regardless"
# df["sc_23"] = "23_added_control_product_regardless"

# New Order:
df["sc_20"] = "20_continuous_dual_product_stockist"
df["sc_14"] = "14_removed_activation_product_control_continuous"
df["sc_15"] = "15_added_activation_product_control_continuous"
df["sc_18"] = "18_continuous_control_product_solo_stockist"
df["sc_10"] = "10_control_product_replaced_with_activation_product"
df["sc_11"] = "11_activation_product_replaced_with_control_product"
df["sc_19"] = "19_continuous_activation_product_solo_stockist"
df["sc_04"] = "04_removed_activation_product_regardless"
df["sc_03"] = "03_added_activation_product_regardless"
df["sc_12"] = "12_continuous_non_stockist_of_activation_product"
df["sc_13"] = "13_continuous_non_stockist_of_control_product"
df["sc_21"] = "21_dual_product_stockist_regardless"
df["sc_22"] = "22_continuous_control_product_solo_stockist"
df["sc_23"] = "23_continuous_activation_product_solo_stockist"
df["sc_16"] = "16_removed_control_product_activation_continuous"
df["sc_17"] = "17_added_control_product_activation_continuous"
df["sc_07"] = "07_activation_product_solo_stocking_last_qtr"
df["sc_08"] = "08_control_product_solo_stocking_last_qtr"
df["sc_09"] = "09_dual_stockist_last_qtr"
df["sc_02"] = "02_activation_product_stockist_last_qtr_regardless"
df["sc_01"] = "01_control_product_stockist_last_qtr_regardless"
df["sc_06"] = "06_removed_control_product_regardless"
df["sc_05"] = "05_added_control_product_regardless"
df["sc_24"] = "24_added_activation_to_control_product"
df["sc_25"] = "25_activation_product_stockist_continuous_regardless"
df["sc_26"] = "26_control_product_stockist_continuous_regardless"
df["sc_27"] = "27_activation_product_added_never_control_product"

# Take slices of the dataframes that meet each scenario criteria

# 20_continuous_dual_product_stockist
sc_20 = df.loc[
    (df["date_count_of_activation_product_stocks"] == dc) &
    (df["is_continuous_control"] == 1)
]

# 14_removed_activation_product_control_continuous
sc_14 = df.loc[
    (df["product_comp_stocks_activation_product"] == "comp_cont") &
    (df["product_act_stocks_activation_product"] == "non_stockist") &
    (df["is_continuous_control"] == 1)
]

# 15_added_activation_product_control_continuous
sc_15 = df.loc[
    (df["product_comp_stocks_activation_product"] == "non_stockist") &
    (df["product_act_stocks_activation_product"] == "act_cont") &
    (df["is_continuous_control"] == 1)
]

# 18_continuous_control_product_solo_stockist
sc_18 = df.loc[
    (df["date_count_of_activation_product_stocks"] == 0) &
    (df["is_continuous_control"] == 1)
]

# 10_control_product_replaced_with_activation_product
sc_10 = df.loc[
    (df["product_comp_stocks_activation_product"] == "non_stockist") &
    (df["product_act_stocks_activation_product"] == "act_cont") &
    (df["product_comp_stocks_control_product"] == "comp_cont") &
    (df["product_act_stocks_control_product"] == "non_stockist")
]

# 11_activation_product_replaced_with_control_product
sc_11 = df.loc[
    (df["product_comp_stocks_activation_product"] == "comp_cont") &
    (df["product_act_stocks_activation_product"] == "non_stockist") &
    (df["product_comp_stocks_control_product"] == "non_stockist") &
    (df["product_act_stocks_control_product"] == "act_cont")
]

# 19_continuous_activation_product_solo_stockist
sc_19 = df.loc[
    (df["date_count_of_control_product_stocks"] == 0) &
    (df["is_continuous_activation"] == 1)
]

# 04_removed_activation_product_regardless
sc_04 = df.loc[
    (df["product_comp_stocks_activation_product"] == "comp_cont") &
    (df["product_act_stocks_activation_product"] == "non_stockist")
]

# 03_added_activation_product_regardless
sc_03 = df.loc[
    (df["product_comp_stocks_activation_product"] == "non_stockist") &
    (df["product_act_stocks_activation_product"] == "act_cont")
]

# 12_continuous_non_stockist_of_activation_product
sc_12 = df.loc[
    (df["date_count_of_activation_product_stocks"] == 0)
]

# 13_continuous_non_stockist_of_activation_product
sc_13 = df.loc[
    (df["date_count_of_control_product_stocks"] == 0)
]

# 21_continuous_dual_product_stockist
sc_21 = df.loc[
    (df["product_comp_stocks_activation_product"] == "comp_cont") &
    (df["product_act_stocks_activation_product"] == "act_cont") &
    (df["product_comp_stocks_control_product"] == "comp_cont") &
    (df["product_act_stocks_control_product"] == "act_cont")
]

# 22_continuous_control_product_solo_stockist
sc_22 = df.loc[
    (df["date_count_of_activation_product_stocks"] == 0) &
    (df["product_comp_stocks_control_product"] == "comp_cont") &
    (df["product_act_stocks_control_product"] == "act_cont")
]

# 23_continuous_activation_product_solo_stockist
sc_23 = df.loc[
    (df["date_count_of_control_product_stocks"] == 0) &
    (df["product_comp_stocks_activation_product"] == "comp_cont") &
    (df["product_act_stocks_activation_product"] == "act_cont")
]

# 16_removed_control_product_activation_continuous
sc_16 = df.loc[
    (df["product_comp_stocks_control_product"] == "comp_cont") &
    (df["product_act_stocks_control_product"] == "non_stockist") &
    (df["is_continuous_activation"] == 1)
]

# 17_added_control_product_activation_continuous
sc_17 = df.loc[
    (df["product_comp_stocks_control_product"] == "non_stockist") &
    (df["product_act_stocks_control_product"] == "act_cont") &
    (df["is_continuous_activation"] == 1)
]

# 07_activation_product_solo_stocking_last_qtr
sc_07 = df.loc[
    (df["product_act_stocks_activation_product"] == "act_cont") &
    (df["product_act_stocks_control_product"] == "non_stockist")
]

# 08_control_product_solo_stocking_last_qtr
sc_08 = df.loc[
    (df["product_act_stocks_control_product"] == "act_cont") &
    (df["product_act_stocks_activation_product"] == "non_stockist")
]

# 09_dual_stockist_last_qtr
sc_09 = df.loc[
    (df["product_act_stocks_control_product"] == "act_cont") &
    (df["product_act_stocks_activation_product"] == "act_cont")
]

# 02_activation_product_stockist_last_qtr_regardless
sc_02 = df.loc[
    (df["product_act_stocks_activation_product"] == "act_cont")
]

# 01_control_product_stockist_last_qtr_regardless
sc_01 = df.loc[
    (df["product_act_stocks_control_product"] == "act_cont")
]

# 06_removed_control_product_regardless
sc_06 = df.loc[
    (df["product_comp_stocks_control_product"] == "comp_cont") &
    (df["product_act_stocks_control_product"] == "non_stockist")
]

# 05_added_control_product_regardless
sc_05 = df.loc[
    (df["product_comp_stocks_control_product"] == "non_stockist") &
    (df["product_act_stocks_control_product"] == "act_cont")
]

# 24_added_activation_to_control_product
sc_24 = df.loc[
    (df["product_comp_stocks_activation_product"] == "non_stockist") &
    (df["product_act_stocks_activation_product"].isin(["act_non_cont", "act_cont"])) &
    (df["product_comp_stocks_control_product"].isin(["comp_non_cont", "comp_cont"])) &
    (df["product_act_stocks_control_product"].isin(["act_non_cont", "act_cont"]))
]

# 25_activation_product_stockist_continuous_regardless
sc_25 = df.loc[
    (df["product_act_stocks_activation_product"] == "act_cont") &
    (df["product_comp_stocks_activation_product"] == "comp_cont")
]

# 26_control_product_stockist_continuous_regardless
sc_26 = df.loc[
    (df["product_act_stocks_control_product"] == "act_cont") &
    (df["product_comp_stocks_control_product"] == "comp_cont")
]

# 27_activation_product_added_never_control_product
sc_27 = df.loc[
    (df["product_comp_stocks_activation_product"] == "non_stockist") &
    (df["product_act_stocks_activation_product"] == "act_cont") &
    (df["date_count_of_control_product_stocks"] == 0)
]