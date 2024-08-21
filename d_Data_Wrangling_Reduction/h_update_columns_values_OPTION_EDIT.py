import pandas as pd

from g_update_products_with_cmbc_cuk_or_mcbc_segments_OPTION_EDIT import df, craft_update
# from g1_spec_beer_update_OPTION import df
from b_read_in_the_data_EDIT import mcbc_products
from b_read_in_the_data_EDIT import heineken_csdi
############################################################################
# df.loc[df['product_class'] == "Craft Beer", 'product'] = "Craft Beer"
#
# print(df.head(20))

# Check the data
# print("\nThe head of df before merging in Craft update is:\n", df.head(2), "\n")
# print("\nThe head of craft update is:\n", craft_update.head(2), "\n")

# Drop the product class column
# df = df.drop(["product_class"], axis=1)
#
# u = craft_update['product_class'].unique()
# print('The unique values in craft_update product are: \n', u, '\n')

# Rename the custom dataframe for merging.
# craft_update =craft_update.rename(
#     columns={
#         "PM_ProductItemId": "product_id"
#     }
# )

# Drop the custom product columns that aren't required.
# craft_update = craft_update.drop(["product_id"], axis=1)

# Merge the data.
# df = pd.merge(
#     df, craft_update,
#     left_on=["product"], right_on=["product"],
#     how="inner"
# )
#
# df["product"] = df["product_class"]
#
# # QC the merge.
# print("\nThe head of df after merging in the custom product data is:\n", df.head(2), "\n")
#
#
#
# u = df['product'].unique()
# print('The unique values in df product are: \n', u, '\n')

# ############################################################################################
# product_mapping1 = {
#
# "Addlestones Premium Cloudy Cider": "Non Flavoured Cider",
# "Adnams Wild Wave 0.5": "Non Flavoured Cider",
# "Adnams Wild Wave English Cider": "Non Flavoured Cider",
# "Alex James Britpop Cider": "Non Flavoured Cider",
# "Ampleforth Medium Cider": "Non Flavoured Cider",
# "Angioletti Mela Rossa": "Non Flavoured Cider",
#         "Angioletti Rose Cider": "Non Flavoured Cider",
#         "Angioletti Secco": "Non Flavoured Cider",
#         "Angry Orchard Crisp Apple": "Non Flavoured Cider",
#         "Anthem Cider": "Non Flavoured Cider",
#         "Any Other Draught Cider": "Non Flavoured Cider",
#         "Any Other Packaged Cider": "Non Flavoured Cider",
#         "Appleshed Cider": "Non Flavoured Cider",
#         "Ashover Kingston Jack": "Non Flavoured Cider",
#         "Ashridge Devon Blush": "Non Flavoured Cider",
#         "Ashridge Devon Gold": "Non Flavoured Cider",
#         "Ashridge Organic Cider": "Non Flavoured Cider",
#         "Aston Manor Friel Cider": "Non Flavoured Cider",
#         "Aston Manor Friels Vintage": "Non Flavoured Cider",
#         "Aston Manor Knights Malvern Myst": "Non Flavoured Cider",
#         "Babycham Extra Dry": "Non Flavoured Cider",
#         "Bath Ciders Bounders": "Non Flavoured Cider",
#         "Bensons Eccentric English Apple Cider": "Non Flavoured Cider",
#         "Biddenden Bushels Cider": "Non Flavoured Cider",
#         "Biddenden Dry": "Non Flavoured Cider",
#         "Biddenden Red Love": "Non Flavoured Cider",
#         "Biddenden Vintage Cider": "Non Flavoured Cider",
#         "Black Dragon Welsh Cider": "Non Flavoured Cider",
#         "Blackthorn": "Non Flavoured Cider",
#         "Blackthorn Gold": "Non Flavoured Cider",
#         "Bolee D'Armorique Cidre Breton": "Non Flavoured Cider",
#         "Bottle Kicking Scrambler": "Non Flavoured Cider",
#         "Braxzz Oaked": "Non Flavoured Cider",
#         "Bristol Beer Factory North Street Cider": "Non Flavoured Cider",
#         "Bristol Steam Cloudy Cider": "Non Flavoured Cider",
#         "Broadoak Bristol Port Cider": "Non Flavoured Cider",
#         "Broadoak Cider": "Non Flavoured Cider",
#         "Broadoak Moonshine": "Non Flavoured Cider",
#         "Broadoak Pheasant Plucker": "Non Flavoured Cider",
#         "Broadoak Vintage Cider": "Non Flavoured Cider",
#         "Butcombe Ashton Press": "Non Flavoured Cider",
#         "Cairn O Mohr Vintage Cider": "Non Flavoured Cider",
#         "Caledonian North Shore Wild Scottish Cider": "Non Flavoured Cider",
#         "Carling British Cider": "Non Flavoured Cider",
#         "Castlings Heath Apple Pie": "Non Flavoured Cider",
#         "Chapel Down Curious Apple": "Non Flavoured Cider",
#         "Cidre Breton": "Non Flavoured Cider",
#         "Colcombe House New Catch": "Non Flavoured Cider",
#         "Cornish Orchards Cornish Gold Cider": "Non Flavoured Cider",
#         "Cornish Orchards Dry Cider": "Non Flavoured Cider",
#         "Cornish Orchards Farmhouse Cider": "Non Flavoured Cider",
#         "Cornish Orchards Heritage Cider": "Non Flavoured Cider",
#         "Cornish Orchards Keepers Meadow": "Non Flavoured Cider",
#         "Cornish Orchards Vintage Cider": "Non Flavoured Cider",
#         "Cotswold Cider Company BlowHorn": "Non Flavoured Cider",
#         "Cotswold Cider Company No Brainer": "Non Flavoured Cider",
#         "Cotswold Cider Company She Devil": "Non Flavoured Cider",
#         "Crate Cider": "Non Flavoured Cider",
#         "Crumptons Oak Cider": "Non Flavoured Cider",
#         "Devon Red Cider": "Non Flavoured Cider",
#         "Diamond White": "Non Flavoured Cider",
#         "Dorset Nectar Dabinett Organic": "Non Flavoured Cider",
#         "Dry Blackthorn": "Non Flavoured Cider",
#         "Eliots Spicy Cider": "Non Flavoured Cider",
#         "Farmer Jims Farmyard Perry": "Non Flavoured Cider",
#         "Farmhouse Cider": "Non Flavoured Cider",
#         "Garden Cider Company Original": "Non Flavoured Cider",
#         "Guest Cider": "Non Flavoured Cider",
#         "Gwynt y Ddraig Ancient Warrior": "Non Flavoured Cider",
#         "Gwynt Y Ddraig Black Dragon": "Non Flavoured Cider",
#         "Gwynt Y Ddraig Celtic Warrior": "Non Flavoured Cider",
#         "Gwynt Y Ddraig Dog Dancer (Cask)": "Non Flavoured Cider",
#         "Gwynt Y Ddraig Farmhouse Pyder": "Non Flavoured Cider",
#         "Gwynt y Ddraig Farmhouse Scrumpy (Cask)": "Non Flavoured Cider",
#         "Gwynt Y Ddraig Farmhouse Vintage Scrumpy": "Non Flavoured Cider",
#         "Gwynt Y Ddraig Haymaker": "Non Flavoured Cider",
# "Gwynt Y Ddraig Old Crow": "Non Flavoured Cider",
# "Gwynt Y Ddraig Orchard Gold": "Non Flavoured Cider",
#     "Gwynt y Ddraig Welsh Warrior": "Non Flavoured Cider",
#     "Hallets Blindfold Cider": "Non Flavoured Cider",
#     "Harefields Sliding Bevel": "Non Flavoured Cider",
#     "Harrow Wood Dickies Dribble": "Non Flavoured Cider",
#     "Harrow Wood Farm Cider": "Non Flavoured Cider",
#     "Hawkes Soul Trader": "Non Flavoured Cider",
#     "Healeys Cornish Gold": "Non Flavoured Cider",
#     "Healeys Cornish Rattler 4%": "Non Flavoured Cider",
#     "Healeys Cornish Rattler Original": "Non Flavoured Cider",
#     "Healeys Cornish Rattler Zero": "Non Flavoured Cider",
#     "Hecks Portwine Of Glastonbury (Cask)": "Non Flavoured Cider",
#     "Henry Westons Family Reserve Cask Conditioned BIB (Cask)": "Non Flavoured Cider",
#     "Henry Westons Family Vintage": "Non Flavoured Cider",
#     "Henry Westons Medium Dry": "Non Flavoured Cider",
#     "Henry Westons Medium Sweet": "Non Flavoured Cider",
#     "Henry Westons Mulled Cider": "Non Flavoured Cider",
#     "Henry Westons Organic Medium Dry": "Non Flavoured Cider",
#     "Henry Westons Single Orchard Still Cider": "Non Flavoured Cider",
#     "Henry Westons Vintage": "Non Flavoured Cider",
#     "Henry Westons Vintage Reserve": "Non Flavoured Cider",
#     "Henry Westons Vintage Rose": "Non Flavoured Cider",
#     "Hobo East Coast Cyder": "Non Flavoured Cider",
#     "Hogans": "Non Flavoured Cider",
#     "Hogans Dry Cider": "Non Flavoured Cider",
#     "Hogans High Sobriety": "Non Flavoured Cider",
#     "Hogans Medium Cider": "Non Flavoured Cider",
#     "Hogans Pukhraj Cider": "Non Flavoured Cider",
#     "Hogs Back Hazy Hog": "Non Flavoured Cider",
#     "Holdens Marcher Lords": "Non Flavoured Cider",
#     "Honeys Unfiltered Cider": "Non Flavoured Cider",
#     "Hoxton Harry Masters Jersey": "Non Flavoured Cider",
#     "Hunts Andsome Bay Cider": "Non Flavoured Cider",
#     "Hunts Barn Screecher": "Non Flavoured Cider",
#     "Hunts Bull Walloper": "Non Flavoured Cider",
#     "Hunts Clinker": "Non Flavoured Cider",
#     "Hunts Misty Maid": "Non Flavoured Cider",
#     "Inchs": "Non Flavoured Cider",
#     "Jakes Kentish Cider": "Non Flavoured Cider",
#     "Kingstone Press": "Non Flavoured Cider",
#     "Lancaster Blush Cider": "Non Flavoured Cider",
#     "Maeloc Dry Cider": "Non Flavoured Cider",
#     "Magners Non Alcoholic": "Non Flavoured Cider",
#     "Magners Original": "Non Flavoured Cider",
#     "Mallets Original Cider": "Non Flavoured Cider",
#     "Marco Pierre White The Governor Cider": "Non Flavoured Cider",
#     "Marstons English Cider": "Non Flavoured Cider",
#     "Mayador M": "Non Flavoured Cider",
#     "Mela Rossa Craft Italian Cider": "Non Flavoured Cider",
#     "Moles Black Rat Cider": "Non Flavoured Cider",
#     "Moles Black Rat Scrumpy": "Non Flavoured Cider",
#     "Moles West Country Gold Cider": "Non Flavoured Cider",
#     "Mr Whiteheads Devils Device": "Non Flavoured Cider",
#     "Natch": "Non Flavoured Cider",
#     "Natch Cider": "Non Flavoured Cider",
#     "Newton Court Organic Farmhouse Scrumpy": "Non Flavoured Cider",
#     "Newton Court Redstreak": "Non Flavoured Cider",
#     "Nightingale Cider Company Discovery Cider": "Non Flavoured Cider",
#     "No Logo Cider": "Non Flavoured Cider",
#     "Norcotts Elderflower Cider": "Non Flavoured Cider",
#     "Norcotts Original Cider": "Non Flavoured Cider",
#     "Olde English": "Non Flavoured Cider",
#     "Olde English Dry Cider": "Non Flavoured Cider",
#     "Oldfields Draught Orchard Cider": "Non Flavoured Cider",
#     "Oldfields Orchard Medium Dry": "Non Flavoured Cider",
#     "Olivers Yarlington Mill Medium Fine Cider": "Non Flavoured Cider",
#     "Orchard Gold Cider": "Non Flavoured Cider",
#     "Orchard Pig": "Non Flavoured Cider",
#     "Orchard Pig Charmer": "Non Flavoured Cider",
#     "Orchard Pig Dark Cider The Moon": "Non Flavoured Cider",
#     "Orchard Pig Reveller": "Non Flavoured Cider",
#     "Orchard Pig Truffler": "Non Flavoured Cider",
#     "Orchard Thieves Apple Cider": "Non Flavoured Cider",
#     "Orpens Apple Cider": "Non Flavoured Cider",
#     "Otter Wildsider": "Non Flavoured Cider",
#     "Pavement Press English Cider": "Non Flavoured Cider",
#     "Polgoon Bills Cider": "Non Flavoured Cider",
#     "Polgoon Cornish Pink": "Non Flavoured Cider",
#     "Polgoon Original Cider": "Non Flavoured Cider",
#     "Poundhouse Cider": "Non Flavoured Cider",
#     "Pulp Apple Craft Cider": "Non Flavoured Cider",
#     "Pure North Deanhouse Cider (Cask)": "Non Flavoured Cider",
#     "Real Al Company Crafty Apple": "Non Flavoured Cider",
#     "Rekorderlig Apple Cider": "Non Flavoured Cider",
#     "Rekorderlig Dry Apple Cider": "Non Flavoured Cider",
#     "Rekorderlig Winter": "Non Flavoured Cider",
#     "Robinsons Cider": "Non Flavoured Cider",
#     "Rockfish Sea Cider": "Non Flavoured Cider",
#     "Ross on Wye Oak Cask Blend": "Non Flavoured Cider",
#     "Sam Smiths Cider Reserve": "Non Flavoured Cider",
#     "Sam Smiths Organic Cider": "Non Flavoured Cider",
#     "Sams Autumn Scrumpy": "Non Flavoured Cider",
#     "Sams Eden Cider": "Non Flavoured Cider",
#     "Sandford Orchard Devon Mist": "Non Flavoured Cider",
#     "Sandford Orchard Devon Red": "Non Flavoured Cider",
#     "Sandford Orchard Devon Scrumpy": "Non Flavoured Cider",
#     "Sandford Orchard Fannys Bramble": "Non Flavoured Cider",
#     "Sandford Orchard The General": "Non Flavoured Cider",
#     "Sandford Orchards Devon Dry": "Non Flavoured Cider",
#     "Sandford Orchards Devon Red": "Non Flavoured Cider",
#     "Sandford Orchards Devon Scrumpy": "Non Flavoured Cider",
#     "Sandford Orchards Vintage Cider": "Non Flavoured Cider",
#     "Sandford Rib Tickler": "Non Flavoured Cider",
#     "Sassy Apple Cider": "Non Flavoured Cider",
#     "Savannah": "Non Flavoured Cider",
#     "Scruffy Dog Original Cider": "Non Flavoured Cider",
#     "Scrumpy Jack": "Non Flavoured Cider",
#     "SeaCider Hardcore": "Non Flavoured Cider",
#     "SeaCider Original Medium": "Non Flavoured Cider",
#     "SeaCider Sticky Toffee Pudding": "Non Flavoured Cider",
#     "Sharps Cold River Cider": "Non Flavoured Cider",
#     "Sharps Orchard Cornish Cider": "Non Flavoured Cider",
#     "Shepherd Neame Orchard View": "Non Flavoured Cider",
#     "Sheppys 200 Special Edition": "Non Flavoured Cider",
#     "Sheppys Cider with Honey": "Non Flavoured Cider",
#     "Sheppys Classic Draught Cider": "Non Flavoured Cider",
#     "Sheppys Kingston Black": "Non Flavoured Cider",
#     "Sheppys Low Alcohol Cider": "Non Flavoured Cider",
#     "Sheppys Oak Matured Vintage Cider": "Non Flavoured Cider",
#     "Sheppys Original Cloudy Cider": "Non Flavoured Cider",
#     "Sheppys South West Orchards": "Non Flavoured Cider",
#     "Sheppys South West Orchards Cider": "Non Flavoured Cider",
#     "Shepton Mallet Cider Mill Somerset Snuffler": "Non Flavoured Cider",
#     "Sidra Avalon": "Non Flavoured Cider",
#     "Skreach Cider": "Non Flavoured Cider",
#     "Snails Bank Appley Dapply": "Non Flavoured Cider",
#     "Snails Bank Mulled Cider": "Non Flavoured Cider",
#     "Snails Bank Pig Squeal": "Non Flavoured Cider",
#     "Somersby Cider": "Non Flavoured Cider",
#     "South West Orchards Low Alcohol": "Non Flavoured Cider",
#     "Stella Cidre": "Non Flavoured Cider",
#     "Stowford Press": "Non Flavoured Cider",
#     "Stowford Press Cloudy": "Non Flavoured Cider",
#     "Stowford Press Low Alcohol Cider": "Non Flavoured Cider",
#     "Strongbow": "Non Flavoured Cider",
#     "Strongbow 5%": "Non Flavoured Cider",
#     "Strongbow Cloudy Apple": "Non Flavoured Cider",
#     "Sxollie Golden Delicious Cider": "Non Flavoured Cider",
#     "Sxollie Granny Smith Cider": "Non Flavoured Cider",
#     "Taffy Apple": "Non Flavoured Cider",
#     "Taunton Natural Dry": "Non Flavoured Cider",
#     "Taunton Original Medium": "Non Flavoured Cider",
#     "Taunton Tradition": "Non Flavoured Cider",
#     "Trenchmore Farm Silly Moo Unfiltered Cider": "Non Flavoured Cider",
#     "Trumans Cote Breton Brut Cidre": "Non Flavoured Cider",
#     "Tutts Clump Cider": "Non Flavoured Cider",
#     "Tutts Clump Oldbury": "Non Flavoured Cider",
#     "United Breweries Peacock Apple Cider": "Non Flavoured Cider",
#     "Weald Valley Cider": "Non Flavoured Cider",
#     "Westons Caple Rd No 3": "Non Flavoured Cider",
#     "Westons Caple Rd No 5": "Non Flavoured Cider",
#     "Westons London Cider W9": "Non Flavoured Cider",
#     "Westons Mortimers Orchard Cider": "Non Flavoured Cider",
#     "Westons Mortimers Orchard English Berry Cider": "Flavoured Cider",
#     "Westons Old Rosie Cloudy Cider": "Non Flavoured Cider",
#     "Westons Old Rosie with Rhubarb (Cask)": "Non Flavoured Cider",
#     "Westons Rosies Pig Cloudy Cider": "Non Flavoured Cider",
#     "Westons Rosies Pig Flat Tyre": "Non Flavoured Cider",
#     "Westons Stowford LA": "Non Flavoured Cider",
#     "Westons Wyld Wood Organic Cider": "Non Flavoured Cider",
#     "Wignac Cidre Naturel": "Non Flavoured Cider",
#     "Wilces Dry Cider": "Non Flavoured Cider",
#     "Winkleigh Sams Poundhouse Crisp": "Non Flavoured Cider",
#     "Woodpecker": "Non Flavoured Cider",
#     "Woodpecker Red": "Non Flavoured Cider",
#
# "Angry Orchard Crisp Apple": "Non Flavoured Cider",
# "Abrahalls Cuckoo Penny": "Non Flavoured Cider",
# "Aspall Blush Cyder": "Flavoured Cider",
# "Blackthorn": "Non Flavoured Cider",
# "Any Other Draught Cider": "Non Flavoured Cider",
# "Abrahalls Slack Alice": "Non Flavoured Cider",
# "Broadoak Moonshine": "Non Flavoured Cider",
# "Orchard Thieves Apple Cider": "Non Flavoured Cider",
# "Aspall Cyder": "Non Flavoured Cider",
# "Addlestones Premium Cloudy Cider": "Non Flavoured Cider",
# "Aspall Harry Sparrow Cyder": "Non Flavoured Cider",
# "Cornish Orchards Cornish Gold Cider": "Non Flavoured Cider",
# "Aspall Mulled Cider": "Non Flavoured Cider",
# "Aspall Suffolk Vichy": "Non Flavoured Cider",
# "Carling British Cider": "Non Flavoured Cider",
# "Thatchers Stans Cheddar Valley": "Non Flavoured Cider",
# "Aspall Premier Cru": "Non Flavoured Cider",
# "Aspall Suffolk Cyder": "Non Flavoured Cider",
# "Blackthorn Gold": "Non Flavoured Cider",
# "Cornish Orchards Heritage Cider": "Non Flavoured Cider",
# "Cornish Orchards Hedgerow Cider": "Non Flavoured Cider",
# "Bulmers Orchard Pioneers Green Apple Cider": "Non Flavoured Cider",
# "Dry Blackthorn": "Non Flavoured Cider",
# "Thatchers Stans Trad": "Non Flavoured Cider",
# "Broadoak Pheasant Plucker": "Non Flavoured Cider",
# "Black Dragon Welsh Cider": "Non Flavoured Cider",
# "Cornish Orchards Hedgerow": "Non Flavoured Cider",
# "Hogans Lonely Partridge": "Non Flavoured Cider",
# "Cornish Orchards Vintage Cider": "Non Flavoured Cider",
# "Cornish Orchards Dry Cider": "Non Flavoured Cider",
# "Guest Cider": "Non Flavoured Cider",
# "Inchs": "Non Flavoured Cider",
# "Bulmers Orchard Pioneers Red Apple Cider": "Non Flavoured Cider",
# "Bottle Kicking Rambler": "Non Flavoured Cider",
# "Kentish Pip Craftsman Cider": "Non Flavoured Cider",
# "Magners Original": "Non Flavoured Cider",
# "Cornish Orchards Wassail Mulled Cider": "Non Flavoured Cider",
# "Cornish Orchards Farmhouse Cider": "Non Flavoured Cider",
# "Harrys Haymaker Dry Cider": "Non Flavoured Cider",
# "Orchard Pig Explorer": "Non Flavoured Cider",
# "Bulmers Original": "Non Flavoured Cider",
# "Bottle Kicking Scrambler": "Non Flavoured Cider",
# "Lilleys Merry Monkey Scrumpy": "Non Flavoured Cider",
# "Stowford Press": "Non Flavoured Cider",
# "Harrys Corker": "Non Flavoured Cider",
# "Hawkes Urban Orchard": "Non Flavoured Cider",
# "Harrys Scrummage": "Non Flavoured Cider",
# "Stowford Press Low Alcohol Cider": "Non Flavoured Cider",
# "Healeys Cornish Gold": "Non Flavoured Cider",
# "Harrys Pink Rhubarb Still Cider": "Non Flavoured Cider",
# "Magners Non Alcoholic": "Non Flavoured Cider",
# "Woodpecker Dry": "Non Flavoured Cider",
# "Hogs Back Hazy Hog": "Non Flavoured Cider",
# "Healeys Cornish Rattler Original": "Non Flavoured Cider",
# "Healeys Cornish Rattler 4%": "Non Flavoured Cider",
# "Henry Westons Organic Medium Dry": "Non Flavoured Cider",
# "Lilleys Fire Dancer": "Non Flavoured Cider",
# "Henry Westons Vintage Reserve": "Non Flavoured Cider",
# "Natch": "Non Flavoured Cider",
# "Henry Westons Vintage Rose": "Non Flavoured Cider",
# "Orchard Pig Pink Cider": "Non Flavoured Cider",
# "Lilleys Sunset Cider": "Non Flavoured Cider",
# "Henry Westons Family Reserve Cask Conditioned BIB (Cask)": "Non Flavoured Cider",
# "Kingstone Press": "Non Flavoured Cider",
# "Strongbow Cloudy Apple": "Non Flavoured Cider",
# "Malvern Gold Medium": "Non Flavoured Cider",
# "Orchard Pig Truffler": "Non Flavoured Cider",
# "Kopparberg Naked Apple": "Non Flavoured Cider",
# "Orchard Pig Reveller": "Non Flavoured Cider",
# "Natch Cider": "Non Flavoured Cider",
# "Kopparberg Rose Cider": "Non Flavoured Cider",
# "Orchard Gold Cider": "Non Flavoured Cider",
# "Thatchers Katy Rose": "Non Flavoured Cider",
# "Scrumpy Jack": "Non Flavoured Cider",
# "Sheppys 200 Special Edition": "Non Flavoured Cider",
# "Rekorderlig Apple Cider": "Non Flavoured Cider",
# "Snails Bank Orchard Dry": "Non Flavoured Cider",
# "SeaCider Bakewell Tart": "Non Flavoured Cider",
# "Stella Cidre": "Non Flavoured Cider",
# "Taunton Natural Dry": "Non Flavoured Cider",
# "Thatchers Oak Aged Green Goblin": "Non Flavoured Cider",
# "Shepherd Neame Orchard View": "Non Flavoured Cider",
# "Somersby Cider": "Non Flavoured Cider",
# "Thatchers Rose": "Non Flavoured Cider",
# "Thatchers Dry": "Non Flavoured Cider",
# "Thatchers Katy": "Non Flavoured Cider",
# "Thatchers Gold": "Non Flavoured Cider",
# "Thistly Cross Traditional Cider (Cask)": "Non Flavoured Cider",
# "Thatchers Old Rascal": "Non Flavoured Cider",
# "Thistly Cross Cider": "Non Flavoured Cider",
# "Strongbow": "Non Flavoured Cider",
# "Turners Apple Pie Cider": "Non Flavoured Cider",
# "Thatchers Somerset Rose": "Non Flavoured Cider",
# "Thistly Cross Traditional Cider": "Non Flavoured Cider",
# "Thatchers Stans Big Apple": "Non Flavoured Cider",
# "Westons Twist Mulled Cider": "Non Flavoured Cider",
# "Thatchers Stans Big Apple (Cask)": "Non Flavoured Cider",
# "Westons Mortimers Orchard Cider": "Non Flavoured Cider",
# "Symonds Founders Reserve": "Non Flavoured Cider",
# "Westons Wyld Wood Organic Cider": "Non Flavoured Cider",
# "Thistly Cross Whisky Cask": "Non Flavoured Cider",
# "Westons Stowford LA": "Non Flavoured Cider",
# "Thatchers Apple & Blackcurrant": "Non Flavoured Cider",
# "Woodpecker": "Non Flavoured Cider",
# "Thatchers Haze": "Non Flavoured Cider",
# "Westons Old Rosie Cloudy Cider (Cask)": "Non Flavoured Cider",
# "Cornish Pear Rattler": "Non Flavoured Cider",
# "Cornish Orchards Pear": "Non Flavoured Cider",
# "Bulmers Pear Cider": "Non Flavoured Cider",
# "Lilleys Bee Sting Pear Cider": "Non Flavoured Cider",
# "Sting Odd Pear": "Non Flavoured Cider",
# "Cornish Orchards Pear Cider": "Non Flavoured Cider",
# "Magners Pear": "Non Flavoured Cider",
# "Kopparberg Pear": "Non Flavoured Cider",
# "Rekorderlig Pear": "Non Flavoured Cider",
# "Malvern Hills Black Pear (Cask)": "Non Flavoured Cider",
# "Brothers Strawberry And Lime": "Non Flavoured Cider",
#
#
#
# "Abrahalls AD Dry Still Cider (Cask)": "Non Flavoured Cider",
# "Abrahalls Celtic Tiger": "Non Flavoured Cider",
# "Abrahalls Cloudy Apple Cider": "Non Flavoured Cider",
# "Abrahalls Lily The Pink": "Non Flavoured Cider",
# "Abrahalls Ruby Tuesday": "Flavoured Cider",
# "Abrahalls Thundering Molly": "Non Flavoured Cider",
# "Aspall Cyderkyn": "Non Flavoured Cider",
# "Aspall Organic Suffolk Cyder": "Non Flavoured Cider",
# "Aspall Waddlegoose Lane Deben Draught": "Non Flavoured Cider",
# "Aston Manor Friels Apple And Spiced Plum": "Non Flavoured Cider",
# "Bad Apple": "Non Flavoured Cider",
# "Cotswold Cider Company Freak Show": "Non Flavoured Cider",
# "Cotswold Cider Company Sideburn": "Non Flavoured Cider",
# "Drynks Smashed Apple Cider": "Non Flavoured Cider",
# "Dunkertons Organic Cider": "Non Flavoured Cider",
# "Galipette Cidre Brut": "Non Flavoured Cider",
# "Garden Cider Company Elderflower": "Non Flavoured Cider",
# "Gaymers Cider": "Non Flavoured Cider",
# "Gwynt Y Ddraig Fiery Fox": "Non Flavoured Cider",
# "Gwynt Y Ddraig Happy Daze": "Non Flavoured Cider",
# "Healeys Cornish Rattler 4.8% Cyder": "Non Flavoured Cider",
# "Healeys Cornish Rattler Mango": "Non Flavoured Cider",
# "Healeys Cornish Rattler Mulled": "Non Flavoured Cider",
# "Healeys Cornish Rattler Peach": "Non Flavoured Cider",
# "Herrljunga Swedish Apple Cider": "Non Flavoured Cider",
# "Hoxton Cidersmiths Sixpointsix": "Non Flavoured Cider",
# "Lilleys Captain Rum Cider": "Non Flavoured Cider",
# "Lilleys Cheeky Pig": "Non Flavoured Cider",
# "Lilleys Dark Sider": "Non Flavoured Cider",
# "Lilleys Gladiator (Cask)": "Non Flavoured Cider",
# "Lilleys Red Rabbit (Cask)": "Non Flavoured Cider",
# "Lilleys Rum Cider": "Non Flavoured Cider",
# "Lilleys Somerset Dry": "Non Flavoured Cider",
# "Lilleys Wild Dog": "Non Flavoured Cider",
# "Lost Orchards Cider Pure Apple": "Non Flavoured Cider",
# "Luscombe Organic Devon cider": "Non Flavoured Cider",
# "Orchard Pig Navelgazer": "Non Flavoured Cider",
# "Orchard Pig The Hogfather (Cask)": "Non Flavoured Cider",
# "Sandford Orchard Cider Ginger": "Non Flavoured Cider",
# "Sassy Cidre Brut": "Non Flavoured Cider",
# "Sassy Organic Cider": "Non Flavoured Cider",
# "Sassy Rose Cider": "Non Flavoured Cider",
# "Saxbys Original Cider": "Non Flavoured Cider",
# "Sheppys Special Edition Cider": "Non Flavoured Cider",
# "Snails Bank Tumbledown": "Non Flavoured Cider",
# "South Hams Fortnum & Mason Mulled Devon Cider": "Non Flavoured Cider",
# "Strongbow Sirrus": "Non Flavoured Cider",
# "Thatchers Dry Cider (Cask)": "Non Flavoured Cider",
# "Thatchers Vintage": "Non Flavoured Cider",
# "Thatchers Zero": "Non Flavoured Cider",
# "Thistly Cross Ginger": "Non Flavoured Cider",
# "Thistly Cross Jaggy Thistle Medium Dry (Cask)": "Non Flavoured Cider",
# "Thistly Cross Original Cider": "Non Flavoured Cider",
# "Thistly Cross Original Cider (Still)": "Non Flavoured Cider",
# "Thistly Cross Original Sparkling Cider": "Non Flavoured Cider",
# "Thistly Cross Strawberry Red (Cask)": "Flavoured Cider",
# "Westons Old Rosie Cloudy Cider Cask Conditioned BIB (Cask)": "Non Flavoured Cider",
# "Westons Rosies Pig Engine Warmer": "Non Flavoured Cider",
#





#     "Appleshed Dark Fruits Cider": "Flavoured Cider",
#     "Ascension Shimmy": "Flavoured Cider",
#     "Ascension Wrath": "Flavoured Cider",
#     "Aspall Pip & Wild Blackberry And Nettle": "Flavoured Cider",
#     "Aspall Waddlegoose Lane Three Berry": "Flavoured Cider",
#     "Barbourne Cherry Bakewell": "Flavoured Cider",
#     "Bensons Raspberry and Lime Cider": "Flavoured Cider",
#     "Blind Pig Bourbon and Blueberry": "Flavoured Cider",
#     "Blind Pig Whiskey Honey and Apple": "Flavoured Cider",
#     "Bottle Kicking Apple And Mango": "Flavoured Cider",
#     "Broadoak Mango Cider": "Flavoured Cider",
#     "Broadoak Mulled Cider": "Flavoured Cider",
#     "Broadoak Pear and Chilli": "Flavoured Cider",
#     "Broadoak Twisted Lime": "Flavoured Cider",
#     "Brothers Cherry Bakewell": "Flavoured Cider",
#     "Brothers Cloudy Lemon": "Flavoured Cider",
#     "Brothers Marshmallow": "Flavoured Cider",
#     "Brothers Parma Violet Cider": "Flavoured Cider",
#     "Brothers Pink Grapefruit Cider": "Flavoured Cider",
#     "Brothers Rhubarb and Custard": "Flavoured Cider",
#     "Brothers Strawberries And Cream": "Flavoured Cider",
#     "Brothers Strawberry & Kiwi": "Flavoured Cider",
#     "Brothers Strawberry And Lime": "Flavoured Cider",
#     "Brothers Strawberry Pear Cider": "Flavoured Cider",
#     "Brothers Tutti Frutti Cider": "Flavoured Cider",
#     "Brothers Wild Fruit Cider": "Flavoured Cider",
#     "Bulmers Crushed Red Berries & Lime": "Flavoured Cider",
#     "Carling Black Fruit Cider": "Flavoured Cider",
#     "Cock Eyed Hedge Rose": "Flavoured Cider",
#     "Cornish Berry Rattler": "Flavoured Cider",
#     "Cornish Orchards Blush Cider": "Flavoured Cider",
#     "Cornish Orchards Cherry and Blackberry": "Flavoured Cider",
#     "Cornish Orchards Hedgerow": "Flavoured Cider",
#     "Cornish Orchards Hedgerow Cider": "Flavoured Cider",
#     "Cornish Orchards Raspberry and Elderflower": "Flavoured Cider",
#     "Cotswold Cider Company Muscle Mary": "Flavoured Cider",
#     "Dorset Orchards Apple Bee": "Flavoured Cider",
#     "Duddas Tun Cherry Cider": "Flavoured Cider",
#     "Duddas Tun Salted Caramel": "Flavoured Cider",
#     "Garden Cider Company Blueberry": "Flavoured Cider",
#     "Garden Cider Company Plum And Ginger": "Flavoured Cider",
#     "Garden Cider Company Raspberry And Rhubarb": "Flavoured Cider",
#     "Garden Cider Company Wild Strawberry": "Flavoured Cider",
#     "Ham Hill Bop Drop": "Flavoured Cider",
#     "Harrys Dirty Harrys Raspberry And Blackcurrant Cider": "Flavoured Cider",
#     "Harrys Sutton Comfort Cider": "Flavoured Cider",
#     "Hawkes Dead And Berried": "Flavoured Cider",
#     "Hawkes Pineapple Punch": "Flavoured Cider",
#     "Hawkes Urban Orchard Mixed Berry": "Flavoured Cider",
#     "Healeys Cornish Rattler Pineapple": "Flavoured Cider",
#     "Healeys Cornish Rattler Strawberry And Lime": "Flavoured Cider",
#     "Herrljunga Blackcurrant & Lime": "Flavoured Cider",
#     "Herrljunga Strawberry & Vanilla": "Flavoured Cider",
#     "Hogans Wild Elder": "Flavoured Cider",
#     "Hunts Hazy Dazy": "Flavoured Cider",
#     "Hunts Raspberry Devon Cider": "Flavoured Cider",
#     "Iford Wild Juice": "Flavoured Cider",
#     "Kingstone Press Wild Berry": "Flavoured Cider",
#     "Kopparberg Black": "Flavoured Cider",
#     "Kopparberg Blackberry and Lime": "Flavoured Cider",
#     "Kopparberg Blueberry & Lime": "Flavoured Cider",
#     "Kopparberg Cherry": "Flavoured Cider",
#     "Kopparberg Elderflower & Lime": "Flavoured Cider",
#     "Kopparberg Light Passionfruit": "Flavoured Cider",
#     "Kopparberg Mixed Fruit Tropical": "Flavoured Cider",
#     "Kopparberg Mixed Fruits": "Flavoured Cider",
#     "Kopparberg Mixed Fruits Non-Alcoholic": "Flavoured Cider",
#     "Kopparberg Passionfruit": "Flavoured Cider",
#     "Kopparberg Passionfruit And Orange": "Flavoured Cider",
#     "Kopparberg Raspberry": "Flavoured Cider",
#     "Kopparberg Rhubarb": "Flavoured Cider",
#     "Kopparberg Spiced Blackberry": "Flavoured Cider",
#     "Kopparberg Strawberry And Lime": "Flavoured Cider",
#     "Kopparberg Strawberry And Lime Non-Alcoholic": "Flavoured Cider",
#     "Kopparberg Summer Punch": "Flavoured Cider",
#     "Kopparberg Wild Berries": "Flavoured Cider",
#     "Kopparberg X Strong Raspberry": "Flavoured Cider",
#     "Lilley Winter Fruits": "Flavoured Cider",
#     "Lilleys Apple and Blackberry": "Flavoured Cider",
#     "Lilleys Apples and Pears": "Flavoured Cider",
#     "Lilleys Cherries And Berries": "Flavoured Cider",
#     "Lilleys Colider": "Flavoured Cider",
#     "Lilleys Crazy Goat": "Flavoured Cider",
#     "Lilleys Elderflower": "Flavoured Cider",
#     "Lilleys Gingerbread Cider": "Flavoured Cider",
#     "Lilleys Lemon and Lime": "Flavoured Cider",
#     "Lilleys Mango": "Flavoured Cider",
#     "Lilleys Mango Cider": "Flavoured Cider",
#     "Lilleys Mango Cider (Cask)": "Flavoured Cider",
# "Lilleys Mulled Cider": "Flavoured Cider",
# "Lilleys Passion Fruit Martini": "Flavoured Cider",
# "Lilleys Peach": "Flavoured Cider",
# "Lilleys Pear And Raspberry (Cask)": "Flavoured Cider",
# "Lilleys Pina Colada Cider": "Flavoured Cider",
# "Lilleys Pineapple Cider": "Flavoured Cider",
# "Lilleys Raspberry Mojito Cider": "Flavoured Cider",
# "Lilleys Rhubarb": "Flavoured Cider",
# "Lilleys Strawberry Cider": "Flavoured Cider",
# "Lilleys Tropical Cider": "Flavoured Cider",
# "Lilleys Whisky Cider": "Flavoured Cider",
# "Lilleys Woo Woo Cider": "Flavoured Cider",
# "Lost Orchards Cider Dark Berries": "Flavoured Cider",
# "Lost Orchards Cider Scottish Red Berries & Lime": "Flavoured Cider",
# "Lyme Bay Annings Crushed Mixed Berries": "Flavoured Cider",
# "Lyme Bay Annings Elderflower And Cucumber": "Flavoured Cider",
# "Lyme Bay Annings Pear and Peach": "Flavoured Cider",
# "Lyme Bay Annings Pink Grapefruit and Pineapple": "Flavoured Cider",
# "Lyme Bay Annings Strawberry and Lyme": "Flavoured Cider",
# "Maeloc Pineapple And Pear": "Flavoured Cider",
# "Magners Dark Fruit": "Flavoured Cider",
# "Magners Orchard Berries": "Flavoured Cider",
# "Millwhites Apples and Pears": "Flavoured Cider",
# "Norcotts Rhubarb Cider": "Flavoured Cider",
# "Old Mout Cider Berries & Cherries": "Flavoured Cider",
# "Old Mout Cider Berries & Cherries Alcohol Free": "Flavoured Cider",
# "Old Mout Cider Kiwi & Lime": "Flavoured Cider",
# "Old Mout Cider Passionfruit & Apple": "Flavoured Cider",
# "Old Mout Cider Pineapple & Raspberry": "Flavoured Cider",
# "Old Mout Cider Pomegranate & Strawberry": "Flavoured Cider",
# "Old Mout Cider Watermelon and Lime": "Flavoured Cider",
# "Old Mout Pineapple & Raspberry Alcohol Free": "Flavoured Cider",
# "Old Mout Strawberry & Apple": "Flavoured Cider",
# "Oldfields Orchard Berry Cider": "Flavoured Cider",
# "Peacock Mango & Lime Cider": "Flavoured Cider",
# "Pearsons Medium Dry Cider": "Flavoured Cider",
# "Pimms Cider Cup Strawberry & Cucumber": "Flavoured Cider",
# "Pulp Mango And Lime": "Flavoured Cider",
# "Pulp Rhubarb Craft Cider": "Flavoured Cider",
# "Purbeck No 10": "Flavoured Cider",
# "Rattler Strawberry And Lime": "Flavoured Cider",
# "Rekorderlig Blood Orange": "Flavoured Cider",
# "Rekorderlig Botanicals Blackberry Violet Juniper": "Flavoured Cider",
# "Rekorderlig Botanicals Grapefruit & Rosemary": "Flavoured Cider",
# "Rekorderlig Botanicals Peach & Basil": "Flavoured Cider",
# "Rekorderlig Botanicals Rhubarb Lemon & Mint": "Flavoured Cider",
# "Rekorderlig Mango and Raspberry": "Flavoured Cider",
# "Rekorderlig Passion Fruit": "Flavoured Cider",
# "Rekorderlig Peach & Apricot": "Flavoured Cider",
# "Rekorderlig Pink Lemon Cider": "Flavoured Cider",
# "Rekorderlig Spiced Plum": "Flavoured Cider",
# "Rekorderlig Strawberry & Lime": "Flavoured Cider",
# "Rekorderlig Strawberry & Lime Low Alcohol": "Flavoured Cider",
# "Rekorderlig Watermelon": "Flavoured Cider",
# "Rekorderlig Wild Berries": "Flavoured Cider",
# "Sams Cider Fruity Blackcurrant": "Flavoured Cider",
# "Sams Fruity Raspberry": "Flavoured Cider",
# "Sandford Orchard Berry Lane": "Flavoured Cider",
# "Sandford Orchard Fannys Bramble": "Flavoured Cider",
# "Sandford Orchard Old Blossom": "Flavoured Cider",
# "Sandford Orchard Strawberry Lane": "Flavoured Cider",
# "Sandford Orchards St Louis Hopped": "Flavoured Cider",
# "Saxbys Blackcurrant Cider": "Flavoured Cider",
# "Saxbys Blackcurrant Cider Sparkling": "Flavoured Cider",
# "Saxbys Plum Cider": "Flavoured Cider",
# "Saxbys Rhubarb Cider": "Flavoured Cider",
# "Saxbys Strawberry Cider": "Flavoured Cider",
# "Saxbys Strawberry Cider (Cask)": "Flavoured Cider",
# "SeaCider Black Cherry": "Flavoured Cider",
# "Seacider Blood Orange": "Flavoured Cider",
# "SeaCider Honeycomb Infused": "Flavoured Cider",
# "SeaCider Lemon Meringue Pie": "Flavoured Cider",
# "SeaCider Mandarin": "Flavoured Cider",
# "Seacider Mango": "Flavoured Cider",
# "SeaCider Marmalade": "Flavoured Cider",
# "SeaCider Passion Fruit": "Flavoured Cider",
# "SeaCider Raspberry Ripple": "Flavoured Cider",
# "SeaCider Rhubarb": "Flavoured Cider",
# "SeaCider Strawberry": "Flavoured Cider",
# "SeaCider White Peach": "Flavoured Cider",
# "Sheppys Cider with Elderflower": "Flavoured Cider",
# "Sheppys Raspberry Cider": "Flavoured Cider",
# "Skal Forrest Berries Cider": "Flavoured Cider",
# "Skal Rhubarb And Pink Grapefruit": "Flavoured Cider",
# "Skal Strawberry And Lime Cider": "Flavoured Cider",
# "Skuna Fruition": "Flavoured Cider",
# "Slightly Foxed Mango Cider": "Flavoured Cider",
# "Smirnoff Cider Mandarin And Pink Grapefruit": "Flavoured Cider",
# "Smirnoff Cider Passion Fruit And Lime": "Flavoured Cider",
# "Smirnoff Cider Raspberry And Pomegranate": "Flavoured Cider",
# "Snails Bank Fruit Bat": "Flavoured Cider",
# "Snails Bank Mango Cider": "Flavoured Cider",
# "Snails Bank Pineapple and Pink Grapefruit": "Flavoured Cider",
# "Snails Bank Rhubarb": "Flavoured Cider",
# "Snails Bank Strawberry and Lime": "Flavoured Cider",
# "Snails Bank Strawberry and Lime": "Flavoured Cider",
# "Somersby Blackberry Cider": "Flavoured Cider",
# "Somersby Strawberry and Rhubarb Cider": "Flavoured Cider",
# "South West Orchards Raspberry Cider": "Flavoured Cider",
# "Stella Cidre Raspberry": "Flavoured Cider",
# "Stowford Press Dark Berry": "Flavoured Cider",
# "Strongbow Dark Fruit": "Flavoured Cider",
# "Strongbow Rose": "Flavoured Cider",
# "Strongbow Ultra Dark Fruit": "Flavoured Cider",
# "Thatchers Blood Orange": "Flavoured Cider",
# "Thatchers Cloudy Lemon": "Flavoured Cider",
# "Thatchers Dark Berry": "Flavoured Cider",
# "Thistly Cross Elderflower": "Flavoured Cider",
# "Thistly Cross Strawberry": "Flavoured Cider",
# "Tomos Watkin Very Berry": "Flavoured Cider",
# "Trenchmore Farm Silly Moo Cowfold Cider": "Flavoured Cider",
# "Turners Elderflower": "Flavoured Cider",
# "Westons Old Rosies Pig Old Banger (Cask)": "Flavoured Cider",
# "Westons Raspberry Roller": "Flavoured Cider",
# "Westons Rosies Pig Flat Tyre (Cask)": "Flavoured Cider",
# "Westons Rosies Pig Mulled Cider": "Flavoured Cider",
# "Westons Rosies Pig Raspberry Cloudy Cider": "Flavoured Cider",
# "Westons Rosies Pig Rhubarb": "Flavoured Cider",
# "Westons Rosies Pig Rusted Wheel": "Flavoured Cider",
# "Westons Rosies Pig Strawberry and Elderflower": "Flavoured Cider",
# "Westons Rosies Pig Tropical": "Flavoured Cider",
# "Westons Twist Raspberry": "Flavoured Cider",
# "Wignac Cidre Alcohol Free": "Flavoured Cider",
# "Wignac Cidre Rose": "Flavoured Cider",
# "Babycham Original": "Flavoured Cider",
# "Belnor Sparkling Perry": "Flavoured Cider",
# "Broadoak Premium Perry (Cask)": "Flavoured Cider",
# "Brothers Festival Strength Pear Cider": "Flavoured Cider",
# "Bulmers Pear Cider": "Flavoured Cider",
# "Burrow Hill Perry": "Flavoured Cider",
# "Charmaine Poire Mousseux Superieur Demi Sec": "Flavoured Cider",
# "Cornish Orchards Pear": "Flavoured Cider",
# "Cornish Orchards Pear Cider": "Flavoured Cider",
# "Cornish Pear Rattler": "Flavoured Cider",
# "Cornish Rattler Pear": "Flavoured Cider",
# "Gwatkin Farmhouse Perry": "Flavoured Cider",
# "Gwynt Y Ddraig Perry Vale": "Flavoured Cider",
# "Gwynt Y Ddraig Two Trees Perry": "Flavoured Cider",
# "Hallets Real Perry": "Flavoured Cider",
# "Henneys Dry Cider": "Flavoured Cider",
# "Henry Westons Country Perry Cask Conditioned Bag In Box": "Flavoured Cider",
# "Herrljunga Swedish Pear Cider": "Flavoured Cider",
# "Hogans Vintage Perry": "Flavoured Cider",
# "Kopparberg Pear": "Flavoured Cider",
# "Kopparberg Pear Non-Alcoholic": "Flavoured Cider",
# "Lilleys Bee Sting Pear Cider": "Flavoured Cider",
# "Lilleys Pickled Parrot Perry": "Flavoured Cider",
# "Lyme Bay Annings Pear And Mint": "Flavoured Cider",
# "Magners Pear": "Flavoured Cider",
# "Mr Whiteheads Midnight Special": "Flavoured Cider",
# "Mr Whiteheads Novo Pyrus Perry": "Flavoured Cider",
# "Newton Court Panting Partridge (Cask)": "Flavoured Cider",
# "Newton Court Winnals Longdon Perry (Cask)": "Flavoured Cider",
# "Norcotts Pear Cider": "Flavoured Cider",
# "Old Mout Cider Pineapple & Raspberry": "Flavoured Cider",
# "Olivers Lemonade Perry": "Flavoured Cider",
# "Perrys Grey Heron": "Flavoured Cider",
# "Rekorderlig Pear": "Flavoured Cider",
# "Ross On Wye Flakey Bark Perry": "Flavoured Cider",
# "Sam Smiths Organic Perry": "Flavoured Cider",
# "Sassy Pear Cider": "Flavoured Cider",
# "Snails Bank Very Perry": "Flavoured Cider",
# "Sting Odd Pear": "Flavoured Cider",
# "Sxollie Packham Pear Perry": "Flavoured Cider",
# "Westons Perry": "Flavoured Cider",
# "Westons Wyld Wood Organic Pear Cider": "Flavoured Cider",
#
# "Brothers Wild Fruit Cider": "Flavoured Cider",
# "Brothers Marshmallow": "Flavoured Cider",
# "Brothers Rhubarb and Custard": "Flavoured Cider",
# "Brothers Parma Violet Cider": "Flavoured Cider",
# "Kopparberg Raspberry": "Flavoured Cider",
# "Carling Black Fruit Cider": "Flavoured Cider",
# "Aspall Isabels Berry": "Flavoured Cider",
# "Brothers Tutti Frutti Cider": "Flavoured Cider",
# "Cornish Orchards Cherry and Blackberry": "Flavoured Cider",
# "Brothers Strawberries And Cream": "Flavoured Cider",
# "Healeys Cornish Rattler Strawberry And Lime": "Flavoured Cider",
# "Brothers Toffee Apple Cider": "Flavoured Cider",
# "Lilleys Cherries And Berries": "Flavoured Cider",
# "Harrys Flash Harrys Mango & Lime Cider": "Flavoured Cider",
# "Bulmers Crushed Red Berries & Lime": "Flavoured Cider",
# "Henry Westons Vintage": "Flavoured Cider",
# "Kingstone Press Wild Berry": "Flavoured Cider",
# "Cornish Orchards Raspberry and Elderflower": "Flavoured Cider",
# "Kopparberg Blueberry & Lime": "Flavoured Cider",
# "Harrys Dirty Harrys Raspberry And Blackcurrant Cider": "Flavoured Cider",
# "Lilleys Mango": "Flavoured Cider",
# "Harrys Sutton Comfort Cider": "Flavoured Cider",
# "Cornish Orchards Blush Cider": "Flavoured Cider",
# "Kentish Pip Craftsman Cider": "Flavoured Cider",
# "Kopparberg Elderflower & Lime": "Flavoured Cider",
# "Lilleys Mulled Cider": "Flavoured Cider",
# "Kopparberg Mixed Fruit Tropical": "Flavoured Cider",
# "Kopparberg Mixed Fruits": "Flavoured Cider",
# "Magners Dark Fruit": "Flavoured Cider",
# "Kopparberg Spiced Blackberry": "Flavoured Cider",
# "Kopparberg Mixed Fruits Non-Alcoholic": "Flavoured Cider",
# "Kopparberg Passionfruit": "Flavoured Cider",
# "Kopparberg Passionfruit And Orange": "Flavoured Cider",
# "Lilleys Strawberry Cider": "Flavoured Cider",
# "Kopparberg Rhubarb": "Flavoured Cider",
# "Kopparberg Strawberry And Lime Non-Alcoholic": "Flavoured Cider",
# "Rekorderlig Botanicals Peach & Basil": "Flavoured Cider",
# "Lilleys Apples and Pears": "Flavoured Cider",
# "Lilleys Passion Fruit Martini": "Flavoured Cider",
# "Kopparberg X Strong Raspberry": "Flavoured Cider",
# "Old Mout Cider Kiwi & Lime": "Flavoured Cider",
# "Magners Rose Cider": "Flavoured Cider",
# "Kopparberg Strawberry And Lime": "Flavoured Cider",
# "Old Mout Cider Berries & Cherries": "Flavoured Cider",
# "Skal Forrest Berries Cider": "Flavoured Cider",
# "Magners Orchard Berries": "Flavoured Cider",
# "Lilleys Pineapple Cider": "Flavoured Cider",
# "Old Mout Cider Pineapple & Raspberry": "Flavoured Cider",
# "Pulp Rhubarb Craft Cider": "Flavoured Cider",
# "Old Mout Cider Passionfruit & Apple": "Flavoured Cider",
# "Kopparberg Summer Punch": "Flavoured Cider",
# "Old Mout Cider Pomegranate & Strawberry": "Flavoured Cider",
# "Snails Bank Sloe Gin": "Flavoured Cider",
# "Rekorderlig Passion Fruit": "Flavoured Cider",
# "Lilleys Rhubarb": "Flavoured Cider",
# "Rekorderlig Mango and Raspberry": "Flavoured Cider",
# "Rekorderlig Botanicals Rhubarb Lemon & Mint": "Flavoured Cider",
# "Rekorderlig Strawberry & Lime": "Flavoured Cider",
# "Lilleys Raspberry Mojito Cider": "Flavoured Cider",
# "Rekorderlig Watermelon": "Flavoured Cider",
# "Thatchers Blood Orange": "Flavoured Cider",
# "Rekorderlig Pink Lemon Cider": "Flavoured Cider",
# "Lilleys Tropical Cider": "Flavoured Cider",
# "Rekorderlig Spiced Plum": "Flavoured Cider",
# "SeaCider Raspberry Ripple": "Flavoured Cider",
# "Westons Raspberry Roller": "Flavoured Cider",
# "Rekorderlig Botanicals Blackberry Violet Juniper": "Flavoured Cider",
# "Saxbys Sour Cherry Cider": "Flavoured Cider",
# "Stowford Press Dark Berry": "Flavoured Cider",
# "Rekorderlig Strawberry & Lime Low Alcohol": "Flavoured Cider",
# "Old Mout Cider Berries & Cherries Alcohol Free": "Flavoured Cider",
# "Skal Strawberry And Lime Cider": "Flavoured Cider",
# "Somersby Blackberry Cider": "Flavoured Cider",
# "Westons Rosies Pig Mulled Cider": "Flavoured Cider",
# "Old Mout Cider Watermelon and Lime": "Flavoured Cider",
# "Strongbow Rose": "Flavoured Cider",
# "Strongbow Ultra Dark Fruit": "Flavoured Cider",
# "Rekorderlig Wild Berries": "Flavoured Cider",
# "Rekorderlig Botanicals Grapefruit & Rosemary": "Flavoured Cider",
# "Thatchers Dark Berry": "Flavoured Cider",
# "Westons Rosies Pig Cloudy Cider": "Flavoured Cider",
# "Westons Rosies Pig Rhubarb": "Flavoured Cider",
# "Saxbys Plum Cider": "Flavoured Cider",
# "Saxbys Rhubarb Cider": "Flavoured Cider",
# "Westons Rosies Pig Strawberry and Elderflower": "Flavoured Cider",
# "Sheppys Raspberry Cider": "Flavoured Cider",
# "Saxbys Strawberry Cider": "Flavoured Cider",
# "Snails Bank Fruit Bat": "Flavoured Cider",
# "Westons Rosies Pig Tropical": "Flavoured Cider",
# "Snails Bank Strawberry and Lime": "Flavoured Cider",
# "Skal Rhubarb And Pink Grapefruit": "Flavoured Cider",
# "Stowford Press Mixed Berries": "Flavoured Cider",
# "Strongbow Dark Fruit": "Flavoured Cider",
# "Thatchers Cloudy Lemon": "Flavoured Cider",
# "Westons Mortimers Orchard English Berry Cider": "Flavoured Cider",
# "Westons Old Rosie with Rhubarb (Cask)": "Flavoured Cider",
# "Westons Old Rosies Pig Old Banger (Cask)": "Flavoured Cider",
# "Westons Rosies Pig Flat Tyre (Cask)": "Flavoured Cider",
#
# "Abrahalls Loubi Lou": "Flavoured Cider",
# "Abrahalls Tutti Frutti": "Flavoured Cider",
# "Aspall Pip & Wild Strawberry And Rose Cider": "Flavoured Cider",
# "Brothers Raspberry Ripple": "Flavoured Cider",
# "Cock Eyed Monkey Mango": "Flavoured Cider",
# "Cockeyed Pear Mania": "Flavoured Cider",
# "Hunts Pixie Juice": "Flavoured Cider",
# "Hunts Red Head Strawberry": "Flavoured Cider",
# "Lilleys Lemon And Ginger": "Flavoured Cider",
# "Lost Orchards Cider Pure Apple": "Flavoured Cider",
# "Maeloc Strawberry Cider": "Flavoured Cider",
# "Mallets Dark Fruit Cider": "Flavoured Cider",
# "Norcotts Pink Grapefruit": "Flavoured Cider",
# "Norcotts Raspberry and Orange Cider": "Flavoured Cider",
# "Norcotts Strawberry And Lime": "Flavoured Cider",
# "Orchard Pig Maverick Chilli and Ginger Cider": "Flavoured Cider",
# "Purbeck Katy And Perry": "Flavoured Cider",
# "SeaCider Blueberry": "Flavoured Cider",
# "SeaCider Bourbon Barrell": "Flavoured Cider",
# "SeaCider Gingerbread": "Flavoured Cider",
# "Snails Bank Raspberry": "Flavoured Cider",
# "Snails Bank Sloe Gin": "Flavoured Cider",
# "Taunton English Berry Cider": "Flavoured Cider",
# "Abrahalls Cracklin Rosie Perry": "Flavoured Cider",
# "Chardolini Perry": "Flavoured Cider"
#
#
#
#
# }
#
#
# # Replace the product names using the mapping dictionary
# df['product'] = df['product'].replace(product_mapping1)
#
# #
# #
# product_mapping2 = {
# "Total Beer": "Total LAD",
# "Total Cider": "Total LAD",
# "Total RTD": "Total LAD",
# }
# df['product_group'] = df['product_group'].replace(product_mapping2)
#
# product_mapping3 = {
# "Beer": "Beer and Cider",
# "Cider": "Beer and Cider",
# }
# df['product_class'] = df['product_class'].replace(product_mapping3)

###################################################################################
# Cider only
# List of allowed ciders



#############################################################################################

# product_mapping = {
# "Peroni Nastro Azzurro": "Super Premium Category",
# "Asahi Super Dry": "Super Premium Category",
# "Camden Hells Lager": "Super Premium Category",
# "Birra Moretti": "Non Premium Category",
# "Estrella Damm": "Non Premium Category",
# "Madri Excepcional": "Non Premium Category",
# "San Miguel": "Non Premium Category",
#     # Add more mappings as needed
#
# }
#
# # Replace the product names using the mapping dictionary
# df['product'] = df['product'].replace(product_mapping)



##############################################################################
# product_mapping = {
# "AFB Craft": "Craft",
# "Craft Stout": "Craft",
# "Entry Craft Ale": "Craft",
# "Entry Craft Lager": "Craft",
# "Premium Craft Ale": "Craft",
# "Premium Craft Lager": "Craft",
#
#
#     # Add more mappings as needed
#
# }
#
# # Replace the product names using the mapping dictionary
# df['product_class'] = df['product_class'].replace(product_mapping)


##############################################################################
# product_mapping = {
# "Carlsberg Danish Pilsner": "Pilsner",
# "Drygate Kelvin Pilsner": "Pilsner",
# "Pratts Brook Pilsner": "Pilsner",
# "Brewpoint Midpoint Pilsner": "Pilsner",
# "Grolsch Premium Pilsner": "Pilsner",
# "Sharps Offshore Pilsner": "Pilsner",
# "Pilsner Urquell": "Pilsner",
# "Veltins Pilsner": "Pilsner",
# "Bedlam Pilsner": "Pilsner",
# "Curious Kentish Pilsner": "Pilsner",
# "Wolfpack Lager Pilsner": "Pilsner",
# "Brooklyn Pilsner": "Pilsner",
# "Efes Pilsner": "Pilsner",
# "Drygate Pilsner": "Pilsner",
# "Shindigger Pilsner": "Pilsner",
# "Portobello London Pilsner": "Pilsner",
# "Salcombe Pilsner": "Pilsner",
# "Cornish Crown Pilsner": "Pilsner",
# "St Ives Porth Pilsner": "Pilsner",
# "ABK Pilsner": "Pilsner",
# "Robinsons Pilsner Unfiltered (Cask)": "Pilsner",
# "Berliner Pilsner": "Pilsner",
# "Seven Bro7hers Pilsner": "Pilsner",
# "Fridays American Pilsner": "Pilsner",
# "Tooth And Claw Wolf Pilsner": "Pilsner",
#     # Add more mappings as needed
#
# }
#
# # Replace the product names using the mapping dictionary
# df['product'] = df['product'].replace(product_mapping)





################################################################################







# AR0658_Madri_vs_Moretti_Stocking_Scenarios, scenario 1
# df.loc[df["product"] == "Madrí Excepcional", "product"] = "Madri and Moretti"
# df.loc[df["product"] == "Peroni Nastro Azzurro", "product"] = "Peroni, Kronenbourg, Asahi"
# df.loc[df["product"] == "Kronenbourg 1664", "product"] = "Peroni, Kronenbourg, Asahi"
#
# # Update all other products
# df.loc[
#     (
#         (df["product"] != "Peroni, Kronenbourg, Asahi")
#     ), "product"] = "Exc Peroni, Kronenbourg and Asahi"


################################################################################


# AR0641 CMBC Super Premium Sales Stories, Scenario 4, Kronenbourg
# df.loc[df["product"] == "Kronenbourg 1664", "product"] = "Kronenbourg 1664" #Activation product stays the same
# df.loc[df["product"] == "Peroni Nastro Azzurro", "product"] = "Asahi, Peroni" #Control product grouped together
# df.loc[df["product"] == "Asahi Super Dry", "product"] = "Asahi, Peroni" #Control product grouped together




# AR0641 CMBC Super Premium Sales Stories, Scenario 3, Asahi
# df.loc[df["product"] == "Asahi Super Dry", "product"] = "Asahi Super Dry" #Activation product stays the same
# df.loc[df["product"] == "Peroni Nastro Azzurro", "product"] = "Kronenbourg, Peroni" #Control product grouped together
# df.loc[df["product"] == "Kronenbourg 1664", "product"] = "Kronenbourg, Peroni" #Control product grouped together




# AR0641 CMBC Super Premium Sales Stories, Scenario 2, Peroni
# df.loc[df["product"] == "Peroni Nastro Azzurro", "product"] = "Peroni Nastro Azzurro" #Activation product stays the same
# df.loc[df["product"] == "Asahi Super Dry", "product"] = "Kronenbourg, Asahi" #Control product grouped together
# df.loc[df["product"] == "Kronenbourg 1664", "product"] = "Kronenbourg, Asahi" #Control product grouped together


# AR0641 CMBC Super Premium Sales Stories, Scenario 1,

# Update Peroni, Kronenbourg and Asahi to Super Premium Lager
# This needs to be present during the entire process
# df.loc[df["product"] == "Asahi Super Dry", "product"] = "Peroni, Kronenbourg, Asahi"
# df.loc[df["product"] == "Peroni Nastro Azzurro", "product"] = "Peroni, Kronenbourg, Asahi"
# df.loc[df["product"] == "Kronenbourg 1664", "product"] = "Peroni, Kronenbourg, Asahi"
#
# # Update all other products
# df.loc[
#     (
#         (df["product"] != "Peroni, Kronenbourg, Asahi")
#     ), "product"] = "Exc Peroni, Kronenbourg and Asahi"


################################################################################


################################################################################

# # SB153 MCBC Premium Lager Analysis # Part one: Update the product class data with MCBCs product class.
# print("\nThe head of mcbc_products is:\n", mcbc_products.head(2), "\n")
# print("\nThe head of df is:\n", df.head(2), "\n")
# mcbc_products = mcbc_products[["product_description", "product_ladder"]].drop_duplicates()
# mcbc_products = mcbc_products.rename(columns={
#     "product_description": "product",
#     "product_ladder": "product_class"
# })
# df = df.drop(["product_class"], axis=1)
# df = pd.merge(
#     df, mcbc_products,
#     left_on=["product"], right_on=["product"], how="inner"
# )
# print("\nThe head of df after merging in mcbc_products is:\n", df.head(2), "\n")
#
# # Update the product columns with what is in the product class column.
# df["product"] = df["product_class"] + " - Products" # The suffix is required to stop the results doubling.

################################################################################

# # Update the product class
# # SB142 EBS Highland Park Sales Stories - Follow Up
# # This is the true product that doesn't actually need updating
# df.loc[df["product"] == "Highland Park 12 Year Old", "product"] = "Highland Park"
# # These are the "Top Malt Products"
# df.loc[df["product"] == "Glenfiddich 12 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Glenmorangie 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Laphroaig 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Jura 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Talisker 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Balvenie Doublewood 12 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Cragganmore 12 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Glenlivet Founders Reserve", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Oban 14", "product"] = "Top Malt Product"
# # These are the "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park 18 Year Old", "product"] = "Highland Park"
# df.loc[df["product"] == "Highland Park 21 Year Old", "product"] = "Highland Park"
# df.loc[df["product"] == "Highland Park 25 Year Old", "product"] = "Highland Park"
# df.loc[df["product"] == "Highland Park 30 Year Old", "product"] = "Highland Park"
# df.loc[df["product"] == "Highland Park Dark Origins", "product"] = "Highland Park"
# df.loc[df["product"] == "Highland Park Fire", "product"] = "Highland Park"  # Aren't seeing this in the data
# df.loc[df["product"] == "Highland Park Freya", "product"] = "Highland Park"
# df.loc[df["product"] == "Highland Park Valkyrie", "product"] = "Highland Park"  # Aren't seeing this in the data

# SB153 MCBC Premium Lager Analysis
# Update the product columns with what is in the product class column.
# df["product"] = df["product_class"]

# # SB142 EBS Highland Park Sales Stories
#
# # This is the true product that doesn't actually need updating
# df.loc[df["product"] == "Highland Park 12 Year Old", "product"] = "Highland Park 12 Year Old"
# # These are the "Top Malt Products"
# df.loc[df["product"] == "Glenfiddich 12 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Glenmorangie 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Laphroaig 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Jura 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Talisker 10 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Balvenie Doublewood 12 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Cragganmore 12 Year Old", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Glenlivet Founders Reserve", "product"] = "Top Malt Product"
# df.loc[df["product"] == "Oban 14", "product"] = "Top Malt Product"
# # These are the "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park 18 Year Old", "product"] = "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park 21 Year Old", "product"] = "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park 25 Year Old", "product"] = "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park 30 Year Old", "product"] = "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park Dark Origins", "product"] = "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park Fire", "product"] = "Other Highland Park Products" # Aren't seeing this in the data
# df.loc[df["product"] == "Highland Park Freya", "product"] = "Other Highland Park Products"
# df.loc[df["product"] == "Highland Park Valkyrie", "product"] = "Other Highland Park Products"# Aren't seeing this in the data

# SB141	Guinness Replacement Analysis - Update cask ale products as "Cask Ale"
# df.loc[df["product_class"] == "Total Ale (Cask)", "product"] = "Total Ale (Cask) - Products"
# Note that this needs to be different to the values in other columns, why it is not called "Total Ale (Cask)".

print(df.head(2))

#####################################################################################################################################

# df = df.drop(["product"], axis=1)
#
# # Drop the custom product columns that aren't required.
# h = heineken_csdi.drop(["outlet", "date"], axis=1)
#
# print("\nThe shape of heineken data is:\n", heineken_csdi.shape, "\n")
# print(heineken_csdi.head(5))
# # Rename the custom dataframe for merging.
# heineken_csdi =heineken_csdi.rename(
#     columns={
#         "product2": "product"
#     }
# )
#
# # Merge the data.
# df = pd.merge(
#     df, heineken_csdi,
#     left_on=["product_id"], right_on=["product_id"],
#     how="inner"
# )
#
# # QC the merge.
# print("\nThe head of df after merging in the custom product data is:\n", df.head(2), "\n")
#


# product_mapping1 = {
#
# "Apple": "Unflavoured",
# "Pear": "Unflavoured",
# }
# df['product'] = df['product'].replace(product_mapping1)



# df.loc[df['product_class'].isin(['Mainstream', 'Premium', 'Classic']), 'product_class'] = (
#     df['product_class'] + ' ' + df['product']
# )
#
#
#
# df['product_class'] = df['product_class'].replace({
#     'Mainstream Flavoured': 'Mainstream Cider',
#     'Mainstream Unflavoured': 'Mainstream Cider',
#     'Premium Flavoured': 'Premium Cider',
#     'Premium Unflavoured': 'Premium Cider'
# })



# df = df.drop(columns="cider_exclusive")

# df["product"] = df["product_class"]

print(df.head(20))