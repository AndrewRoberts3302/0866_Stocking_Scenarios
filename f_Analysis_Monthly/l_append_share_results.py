import pandas as pd

from i_volume_shares_product_level import sh_1
from j_volume_shares_product_class_level import sh_2
from k_volume_shares_product_group_level import sh_3

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

sh = pd.concat([sh_1, sh_2, sh_3], axis=0)

print(sh.head(2))