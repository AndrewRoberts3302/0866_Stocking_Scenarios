import pandas as pd
from a_Data_Path.a_data_path import data_path

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# Read in the supplied data from the project folders.
huk_segment = pd.read_csv("../a_Supplied_Files/SSRS_OutletIndex.csv",)

# Identify the data file names.
data_reduced = "data_reduced.csv"
df = pd.read_csv(f"{data_path}/{data_reduced}", parse_dates=["date"])

print(df.head(20))
