import pandas as pd
from a_Data_Path.a_data_path import data_path
from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# Identify the data file names
data_clean = "data_clean.csv"
df = pd.read_csv(f"{data_path}/{data_clean}", parse_dates=["date"])
