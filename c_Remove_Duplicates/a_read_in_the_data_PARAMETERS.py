import pandas as pd
from a_Data_Path.a_data_path import data_path


# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)


# df = pd.read_csv("../b_SQL_DataPulls/data_strongbow.csv", parse_dates=["date"]) # NOT USED

# Identify the data names.
data_cs = "data_cs.csv"
data_di = "data_di.csv"
# EPOS_data = "EPOS_data.csv"

#From SQL Source
# data_cs = "total_wet_CS.csv"
# data_di = "total_wet_DI.csv"



# data_cs = "data_cs_0461_brands.csv"
# data_di = "data_di_0461_brands.csv"

##############################################################################
#cider only
h_cs= "heineken_products_cs.csv"
h_di ="heineken_products_di.csv"

# Read in the data.
cs = pd.read_csv(f"{data_path}/{data_cs}", parse_dates=["date"])
di = pd.read_csv(f"{data_path}/{data_di}", parse_dates=["date"])
# EPOS = pd.read_csv(f"{data_path}/{EPOS_Data_731}", parse_dates=["date"])
h_cs=pd.read_csv(f"{data_path}/{h_cs}",)
h_di=pd.read_csv(f"{data_path}/{h_di}",)



