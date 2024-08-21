import pandas as pd
from a_Data_Path.a_data_path import data_path

# Set the console to display full contents of a DataFrame
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.width', None)

# Read in the supplied data from the project files.
huk_segment = pd.read_csv("../a_Supplied_Files/SSRS_OutletIndex.csv",)

# Read in the data.
# data = "data.csv"  # This is the usual file to use.

###############################################################################
# Read in other project specific data sources instead.
###############################################################################
#0658 - Madri vs Birra Moretti
data = "data_0658.csv"  # CSDI source


###############################################################################
# 0610 - CMBC Poretti Sales Stories
# data = "data_0610.csv"  # CSDI source
# data = "EPOS_Data_731.csv"  # EPOS source
###############################################################################

###############################################################################
# 0517 Edrington UK - Famous Grouse vs Blendeds
# data = "data_0517_spirits.csv"
###############################################################################

###############################################################################
# 0516 Pernod Ricard UK
# data = "data_0516_spirits_london_rest_of_gb.csv"
###############################################################################

###############################################################################
# 0508 Asahi UK - Draught Beer Scenarios - 0492 Follow Up
# data = "data_0508_total_draught_beer_london_rest_of_gb.csv"
###############################################################################

###############################################################################
# 0507 Asahi UK - Draught Beer Scenarios - 0492 Follow Up
# data = "data_0507_total_draught_and_packaged_beer.csv"
###############################################################################

###############################################################################
# 0500 Asahi UK - Draught Beer Scenarios - 0492 Follow Up
# data = "data_0492_total_draught_beer.csv"
# data = "data_0492_total_draught_beer_other_premiums_1.csv"
# data = "data_0492_total_draught_beer_other_premiums_2.csv"
###############################################################################

###############################################################################
# 0492  Asahi UK - Draught Beer Scenarios
# data = "data_0492_total_draught_beer.csv"
# data = "data_0492_total_draught_beer_other_premiums_1.csv"
# data = "data_0492_total_draught_beer_other_premiums_2.csv"
###############################################################################

###############################################################################
# 0461 Heineken UK - Old Mout Scenarios
# data = "data_0461.csv"
###############################################################################

###############################################################################
# 0448 Edrington SKU Sales Stories - 0432 Follow Ups
###############################################################################

# data = "data_0448_01_famous_grouse_blended_whisky.csv"
# data = "data_0448_02_couvoisier_other_cognac.csv"
# data = "data_0448_03_jim_beam_other_american_whiskey.csv"
# data = "data_0448_07_premium_blended_whisky_standard_blended_whisky.csv"
# data = "data_0448_08_vsop_cognac_vs_cognac.csv"
# data = "data_0448_09_premium_american_whiskey_standard_american_whiskey.csv"
# data = "data_0448_13_peated_malt_whisky_vs_unpeated_malt_whisky.csv"

###############################################################################
# 0432 Identify the data file names
# data = "data_0432_brandy.csv"
# data = "data_0432_gl2_in_spirits.csv"
# data = "data_0432_whiskey.csv"


# 0398 Identify the data file names
# data = "data_0398.csv"
# data = "data_0398_gin.csv"
# data = "data_0398_whiskey.csv"
# data = "data_0398_rum.csv"
# data = "data_0398_american_whiskey.csv"
# data = "data_0398_vodka.csv"
# data = "data_0398_brandy.csv"

###############################################################################
# These are required in all projects
###############################################################################

# These are used as options.
craft_update_data = "craft_update_data.csv"
mcbc_product_data = "mcbc_product_data.csv"
cmbc_cuk_product_data = "cmbc_cuk_product_data.csv"
mcbc_outlet_data = "mcbc_outlet_data.csv"
flavoured_cider_data = "cider_flavour_data.csv"
Spec_beer_products = "Spec_beer_products.csv"
heineken_csdi = "heineken_csdi.csv"



# Read in the data from the data folder location.
df = pd.read_csv(f"{data_path}/{data}", parse_dates=["date"])
mcbc_products = pd.read_csv(f"{data_path}/{mcbc_product_data}")
cmbc_cuk_products = pd.read_csv(f"{data_path}/{cmbc_cuk_product_data}")
mcbc_outlets = pd.read_csv(f"{data_path}/{mcbc_outlet_data}")
craft_update = pd.read_csv(f"{data_path}/{craft_update_data}")
flavoured_cider = pd.read_csv(f"{data_path}/{flavoured_cider_data}")
Spec_beer_products = pd.read_csv(f"{data_path}/{Spec_beer_products}")
heineken_csdi = pd.read_csv(f"{data_path}/{heineken_csdi}")

print("\nThe shape of mcbc_products is:\n", mcbc_products.shape, "\n")
mcbc_products = mcbc_products.drop_duplicates()
print("\nThe shape of mcbc_products is:\n", mcbc_products.shape, "\n")
u = craft_update['product_class'].unique()
print('The unique values in craft_update product are: \n', u, '\n')
print('The head of heineken_csdi is: \n', u, '\n')
print(heineken_csdi.head(10))
print(df.head(100))
###############################################################################