# WRITE THE CSDI DATA TO CSV (file)

# Write the CSDI data to csv.

# from pathlib import Path

from a_Data_Path.a_data_path import data_path
# from e_remove_duplicates_from_heineken_data_OPTION import heineken_csdi
# from f_combine_products_OPTION import csdi
# from e_add_value_column import csdi
from f_combine_products_OPTION import csdi
# cwd = Path(__file__).parent
csdi.to_csv(data_path / "data_0658.csv", index=False)
# heineken_csdi.to_csv(data_path / "heineken_csdi.csv", index=False)

# EPOS.to_csv(data_path / "data_0658.csv", index=False)

print(csdi.head(20))