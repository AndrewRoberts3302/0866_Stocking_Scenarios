import pandas as pd

from f_update_custom_quality import df
from b_read_in_the_data_EDIT import cmbc_cuk_products, mcbc_products, craft_update
##############################################################################################

# ale_mapping = {
#     "Cask Ale": "Ale",
#     "Craft Ale": "Ale",
#     "Premium Ale": "Ale",
#     "Standard Ale": "Ale",
#     "AFB Ale/Stout": "Ale"
# }
#
# # Replace the values in the product_class column using the mapping
# df["product_class"] = df["product_class"].replace(ale_mapping)
#
#
# craft_mapping = {
#     "Craft Lager": "Craft",
#     "Craft Ale": "Craft",
#     "AFB Craft": "Craft",
#     "Craft Stout": "Craft"
# }
#
# # Replace the values in the product_class column using the mapping
# df["product_group"] = df["product_group"].replace(craft_mapping)
#
#
# ignore_mapping1 = {
# "Standard Lager": "ignore1",
# "Craft Lager": "ignore1",
# "Unknown": "ignore1",
# "Traditional": "ignore1",
# "AFB Craft": "ignore1",
# "Modern": "ignore1",
# "Speciality Beer": "ignore1",
# "AFB Lager": "ignore1",
# "Mainstream Standard": "ignore1",
# "Craft Stout": "ignore1",
# "High Strength": "ignore1",
# "Premium Lager": "ignore1",
#
# }
#
# # Replace the values in the product_class column using the mapping
# df["product_class"] = df["product_class"].replace(ignore_mapping1)
#
#
#
# ignore_mapping2 = {
# "Cask Ale": "ignore2",
# "Premium Ale": "ignore2",
# "Standard Ale": "ignore2",
# "AFB Ale/Stout": "ignore2",
# "Stout": "ignore2",
# "Standard Lager": "ignore2",
# "Unknown": "ignore2",
# "Traditional": "ignore2",
# "Modern": "ignore2",
# "Speciality Beer": "ignore2",
# "AFB Lager": "ignore2",
# "Mainstream Standard": "ignore2",
# "World Lager": "ignore2",
# "High Strength": "ignore2",
# "Premium Lager": "ignore2",
#
# }
#
# # Replace the values in the product_class column using the mapping
# df["product_group"] = df["product_group"].replace(ignore_mapping2)




#######################################################################################
# Check the data
# print("\nThe head of df before merging in MCBC product data is:\n", df.head(2), "\n")
# print("\nThe head of mcbc_products is:\n", mcbc_products.head(2), "\n")
# #
# print("\nThe shape of df before merging in MCBC product data is:\n", df.shape, "\n")
# print("\nThe shape of mcbc_products is:\n", mcbc_products.shape, "\n")
# #
# # Drop the product class column
# df = df.drop(["product_class"], axis=1)
# #
# # Drop the custom product columns that aren't required.
# mcbc_products = mcbc_products.drop(["product_id"], axis=1)
# #
# print("\nThe shape of mcbc_products is:\n", mcbc_products.shape, "\n")
# # Rename the custom dataframe for merging.
# mcbc_products =mcbc_products.rename(
#     columns={
#         "product_description": "product",
#         "product_ladder": "product_class"
#     }
# )
#
# print(mcbc_products.head(2))
# print(df.head(5))
#
# # Merge the data.
# df = pd.merge(
#     df, mcbc_products,
#     left_on=["product"], right_on=["product"],
#     how="inner"
# )
#
# print(df.head(5))
#
# df["product"] = df["product_class"]
# #
# # # QC the merge.
# # print("\nThe head of df after merging in the custom product data is:\n", df.head(2), "\n")
#
# print(df.head(5))


# ##############################################################################################
# Check the data
# print("\nThe head of df before merging in CMBC CUK product data is:\n", df.head(2), "\n")
# print("\nThe head of cmbc_cuk_products is:\n", cmbc_cuk_products.head(2), "\n")
#
# # Drop the product class column
# df = df.drop(["product_class"], axis=1)
#
# # Drop the custom product columns that aren't required.
# cmbc_cuk_products = cmbc_cuk_products.drop(["ProductId", "PT_Segment"], axis=1)
#
# # Rename the custom dataframe for merging.
# cmbc_cuk_products =cmbc_cuk_products.rename(
#     columns={
#         "ProductDescription": "product",
#         "PT_SubSegment": "product_class"
#     }
# )
#
# # Merge the data.
# df = pd.merge(
#     df, cmbc_cuk_products,
#     left_on=["product"], right_on=["product"],
#     how="inner"
# )
#
# # QC the merge.
# print("\nThe head of df after merging in the custom product data is:\n", df.head(2), "\n")

###################################################################################################
# Cider only

# allowed_ciders = [
#     "Addlestones Premium Cloudy Cider",
#     "Adnams Wild Wave 0.5",
#     "Adnams Wild Wave English Cider",
#     "Alex James Britpop Cider",
#     "Ampleforth Medium Cider",
#     "Angioletti Mela Rossa",
#     "Angioletti Rose Cider",
#     "Angioletti Secco",
#     "Angry Orchard Crisp Apple",
#     "Anthem Cider",
#     "Any Other Draught Cider",
#     "Any Other Packaged Cider",
#     "Appleshed Cider",
#     "Ashover Kingston Jack",
#     "Ashridge Devon Blush",
#     "Ashridge Devon Gold",
#     "Ashridge Organic Cider",
#     "Aston Manor Friel Cider",
#     "Aston Manor Friels Vintage",
#     "Aston Manor Knights Malvern Myst",
#     "Babycham Extra Dry",
#     "Bath Ciders Bounders",
#     "Bensons Eccentric English Apple Cider",
#     "Biddenden Bushels Cider",
#     "Biddenden Dry",
#     "Biddenden Red Love",
#     "Biddenden Vintage Cider",
#     "Black Dragon Welsh Cider",
#     "Blackthorn",
#     "Blackthorn Gold",
#     "Bolee D'Armorique Cidre Breton",
#     "Bottle Kicking Scrambler",
#     "Braxzz Oaked",
#     "Bristol Beer Factory North Street Cider",
#     "Bristol Steam Cloudy Cider",
#     "Broadoak Bristol Port Cider",
#     "Broadoak Cider",
#     "Broadoak Moonshine",
#     "Broadoak Pheasant Plucker",
#     "Broadoak Vintage Cider",
#     "Butcombe Ashton Press",
#     "Cairn O Mohr Vintage Cider",
#     "Caledonian North Shore Wild Scottish Cider",
#     "Carling British Cider",
#     "Castlings Heath Apple Pie",
#     "Chapel Down Curious Apple",
#     "Cidre Breton",
#     "Colcombe House New Catch",
#     "Cornish Orchards Cornish Gold Cider",
#     "Cornish Orchards Dry Cider",
#     "Cornish Orchards Farmhouse Cider",
#     "Cornish Orchards Heritage Cider",
#     "Cornish Orchards Keepers Meadow",
#     "Cornish Orchards Vintage Cider",
#     "Cotswold Cider Company BlowHorn",
#     "Cotswold Cider Company No Brainer",
#     "Cotswold Cider Company She Devil",
#     "Crate Cider",
#     "Crumptons Oak Cider",
#     "Devon Red Cider",
#     "Diamond White",
#     "Dorset Nectar Dabinett Organic",
#     "Dry Blackthorn",
#     "Eliots Spicy Cider",
#     "Farmer Jims Farmyard Perry",
#     "Farmhouse Cider",
#     "Garden Cider Company Original",
#     "Guest Cider",
#     "Gwynt y Ddraig Ancient Warrior",
#     "Gwynt Y Ddraig Black Dragon",
#     "Gwynt Y Ddraig Celtic Warrior",
#     "Gwynt Y Ddraig Dog Dancer (Cask)",
#     "Gwynt Y Ddraig Farmhouse Pyder",
#     "Gwynt y Ddraig Farmhouse Scrumpy (Cask)",
#     "Gwynt Y Ddraig Farmhouse Vintage Scrumpy",
#     "Gwynt Y Ddraig Haymaker",
#     "Gwynt Y Ddraig Old Crow",
#     "Gwynt Y Ddraig Orchard Gold",
#     "Gwynt y Ddraig Welsh Warrior",
#     "Hallets Blindfold Cider",
#     "Harefields Sliding Bevel",
#     "Harrow Wood Dickies Dribble",
#     "Harrow Wood Farm Cider",
#     "Hawkes Soul Trader",
#     "Healeys Cornish Gold",
#     "Healeys Cornish Rattler 4%",
#     "Healeys Cornish Rattler Original",
#     "Healeys Cornish Rattler Zero",
#     "Hecks Portwine Of Glastonbury (Cask)",
#     "Henry Westons Family Reserve Cask Conditioned BIB (Cask)",
#     "Henry Westons Family Vintage",
#     "Henry Westons Medium Dry",
#     "Henry Westons Medium Sweet",
#     "Henry Westons Mulled Cider",
#     "Henry Westons Organic Medium Dry",
#     "Henry Westons Single Orchard Still Cider",
#     "Henry Westons Vintage",
#     "Henry Westons Vintage Reserve",
#     "Henry Westons Vintage Rose",
#     "Hobo East Coast Cyder",
#     "Hogans",
#     "Hogans Dry Cider",
#     "Hogans High Sobriety",
#     "Hogans Medium Cider",
#     "Hogans Pukhraj Cider",
#     "Hogs Back Hazy Hog",
#     "Holdens Marcher Lords",
#     "Honeys Unfiltered Cider",
#     "Hoxton Harry Masters Jersey",
#     "Hunts Andsome Bay Cider",
#     "Hunts Barn Screecher",
#     "Hunts Bull Walloper",
#     "Hunts Clinker",
#     "Hunts Misty Maid",
#     "Inchs",
#     "Jakes Kentish Cider",
#     "Kingstone Press",
#     "Lancaster Blush Cider",
#     "Maeloc Dry Cider",
#     "Magners Non Alcoholic",
#     "Magners Original",
#     "Mallets Original Cider",
#     "Marco Pierre White The Governor Cider",
#     "Marstons English Cider",
#     "Mayador M",
#     "Mela Rossa Craft Italian Cider",
#     "Moles Black Rat Cider",
#     "Moles Black Rat Scrumpy",
#     "Moles West Country Gold Cider",
#     "Mr Whiteheads Devils Device",
#     "Natch",
#     "Natch Cider",
#     "Newton Court Organic Farmhouse Scrumpy",
#     "Newton Court Redstreak",
#     "Nightingale Cider Company Discovery Cider",
#     "No Logo Cider",
#     "Norcotts Elderflower Cider",
#     "Norcotts Original Cider",
#     "Olde English",
#     "Olde English Dry Cider",
#     "Oldfields Draught Orchard Cider",
#     "Oldfields Orchard Medium Dry",
#     "Olivers Yarlington Mill Medium Fine Cider",
#     "Orchard Gold Cider",
#     "Orchard Pig",
#     "Orchard Pig Charmer",
#     "Orchard Pig Dark Cider The Moon",
#     "Orchard Pig Reveller",
#     "Orchard Pig Truffler",
#     "Orchard Thieves Apple Cider",
#     "Orpens Apple Cider",
#     "Otter Wildsider",
#     "Pavement Press English Cider",
#     "Polgoon Bills Cider",
#     "Polgoon Cornish Pink",
#     "Polgoon Original Cider",
#     "Poundhouse Cider",
#     "Pulp Apple Craft Cider",
#     "Pure North Deanhouse Cider (Cask)",
#     "Real Al Company Crafty Apple",
#     "Rekorderlig Apple Cider",
#     "Rekorderlig Dry Apple Cider",
#     "Rekorderlig Winter",
#     "Robinsons Cider",
#     "Rockfish Sea Cider",
#     "Ross on Wye Oak Cask Blend",
#     "Sam Smiths Cider Reserve",
#     "Sam Smiths Organic Cider",
#     "Sams Autumn Scrumpy",
#     "Sams Eden Cider",
#     "Sandford Orchard Devon Mist",
#     "Sandford Orchard Devon Red",
#     "Sandford Orchard Devon Scrumpy",
#     "Sandford Orchard Fannys Bramble",
#     "Sandford Orchard The General",
#     "Sandford Orchards Devon Dry",
#     "Sandford Orchards Devon Red",
#     "Sandford Orchards Devon Scrumpy",
#     "Sandford Orchards Vintage Cider",
#     "Sandford Rib Tickler",
#     "Sassy Apple Cider",
#     "Savannah",
#     "Scruffy Dog Original Cider",
#     "Scrumpy Jack",
#     "SeaCider Hardcore",
#     "SeaCider Original Medium",
#     "SeaCider Sticky Toffee Pudding",
#     "Sharps Cold River Cider",
#     "Sharps Orchard Cornish Cider",
#     "Shepherd Neame Orchard View",
#     "Sheppys 200 Special Edition",
#     "Sheppys Cider with Honey",
#     "Sheppys Classic Draught Cider",
#     "Sheppys Kingston Black",
#     "Sheppys Low Alcohol Cider",
#     "Sheppys Oak Matured Vintage Cider",
#     "Sheppys Original Cloudy Cider",
#     "Sheppys South West Orchards",
#     "Sheppys South West Orchards Cider",
#     "Shepton Mallet Cider Mill Somerset Snuffler",
#     "Sidra Avalon",
#     "Skreach Cider",
#     "Snails Bank Appley Dapply",
#     "Snails Bank Mulled Cider",
#     "Snails Bank Pig Squeal",
#     "Somersby Cider",
#     "South West Orchards Low Alcohol",
#     "Stella Cidre",
#     "Stowford Press",
#     "Stowford Press Cloudy",
#     "Stowford Press Low Alcohol Cider",
#     "Strongbow",
#     "Strongbow 5%",
#     "Strongbow Cloudy Apple",
# "Sxollie Golden Delicious Cider",
# "Sxollie Granny Smith Cider",
# "Taffy Apple",
# "Taunton Natural Dry",
# "Taunton Original Medium",
# "Taunton Tradition",
# "Trenchmore Farm Silly Moo Unfiltered Cider",
# "Trumans Cote Breton Brut Cidre",
# "Tutts Clump Cider",
# "Tutts Clump Oldbury",
# "United Breweries Peacock Apple Cider",
# "Weald Valley Cider",
# "Westons Caple Rd No 3",
# "Westons Caple Rd No 5",
# "Westons London Cider W9",
# "Westons Mortimers Orchard Cider",
# "Westons Mortimers Orchard English Berry Cider",
# "Westons Old Rosie Cloudy Cider",
# "Westons Old Rosie with Rhubarb (Cask)",
# "Westons Rosies Pig Cloudy Cider",
# "Westons Rosies Pig Flat Tyre",
# "Westons Stowford LA",
# "Westons Wyld Wood Organic Cider",
# "Wignac Cidre Naturel",
# "Wilces Dry Cider",
# "Winkleigh Sams Poundhouse Crisp",
# "Woodpecker",
# "Woodpecker Red",
# "Angry Orchard Crisp Apple",
# "Abrahalls Cuckoo Penny",
# "Aspall Blush Cyder",
# "Blackthorn",
# "Any Other Draught Cider",
# "Abrahalls Slack Alice",
# "Broadoak Moonshine",
# "Orchard Thieves Apple Cider",
# "Aspall Cyder",
# "Addlestones Premium Cloudy Cider",
# "Aspall Harry Sparrow Cyder",
# "Cornish Orchards Cornish Gold Cider",
# "Aspall Mulled Cider",
# "Aspall Suffolk Vichy",
# "Carling British Cider",
# "Thatchers Stans Cheddar Valley",
# "Aspall Premier Cru",
# "Aspall Suffolk Cyder",
# "Blackthorn Gold",
# "Cornish Orchards Heritage Cider",
# "Cornish Orchards Hedgerow Cider",
# "Bulmers Orchard Pioneers Green Apple Cider",
# "Dry Blackthorn",
# "Thatchers Stans Trad",
# "Broadoak Pheasant Plucker",
# "Black Dragon Welsh Cider",
# "Cornish Orchards Hedgerow",
# "Hogans Lonely Partridge",
# "Cornish Orchards Vintage Cider",
# "Cornish Orchards Dry Cider",
# "Guest Cider",
# "Inchs",
# "Bulmers Orchard Pioneers Red Apple Cider",
# "Bottle Kicking Rambler",
# "Kentish Pip Craftsman Cider",
# "Magners Original",
# "Cornish Orchards Wassail Mulled Cider",
# "Cornish Orchards Farmhouse Cider",
# "Harrys Haymaker Dry Cider",
# "Orchard Pig Explorer",
# "Bulmers Original",
# "Bottle Kicking Scrambler",
# "Lilleys Merry Monkey Scrumpy",
# "Stowford Press",
# "Harrys Corker",
# "Hawkes Urban Orchard",
# "Harrys Scrummage",
# "Stowford Press Low Alcohol Cider",
# "Healeys Cornish Gold",
# "Harrys Pink Rhubarb Still Cider",
# "Magners Non Alcoholic",
# "Woodpecker Dry",
# "Hogs Back Hazy Hog",
# "Healeys Cornish Rattler Original",
# "Healeys Cornish Rattler 4%",
# "Henry Westons Organic Medium Dry",
# "Lilleys Fire Dancer",
# "Henry Westons Vintage Reserve",
# "Natch",
# "Henry Westons Vintage Rose",
# "Orchard Pig Pink Cider",
# "Lilleys Sunset Cider",
# "Henry Westons Family Reserve Cask Conditioned BIB (Cask)",
# "Kingstone Press",
# "Strongbow Cloudy Apple",
# "Malvern Gold Medium",
# "Orchard Pig Truffler",
# "Kopparberg Naked Apple",
# "Orchard Pig Reveller",
# "Natch Cider",
# "Kopparberg Rose Cider",
# "Orchard Gold Cider",
# "Thatchers Katy Rose",
# "Scrumpy Jack",
# "Sheppys 200 Special Edition",
# "Rekorderlig Apple Cider",
# "Snails Bank Orchard Dry",
# "SeaCider Bakewell Tart",
# "Stella Cidre",
# "Taunton Natural Dry",
# "Thatchers Oak Aged Green Goblin",
# "Shepherd Neame Orchard View",
# "Somersby Cider",
# "Thatchers Rose",
# "Thatchers Dry",
# "Thatchers Katy",
# "Thatchers Gold",
# "Thistly Cross Traditional Cider (Cask)",
# "Thatchers Old Rascal",
# "Thistly Cross Cider",
# "Strongbow",
# "Turners Apple Pie Cider",
# "Thatchers Somerset Rose",
# "Thistly Cross Traditional Cider",
# "Thatchers Stans Big Apple",
# "Westons Twist Mulled Cider",
# "Thatchers Stans Big Apple (Cask)",
# "Westons Mortimers Orchard Cider",
# "Symonds Founders Reserve",
# "Westons Wyld Wood Organic Cider",
# "Thistly Cross Whisky Cask",
# "Westons Stowford LA",
# "Thatchers Apple & Blackcurrant",
# "Woodpecker",
# "Thatchers Haze",
# "Westons Old Rosie Cloudy Cider (Cask)",
# "Cornish Pear Rattler",
# "Cornish Orchards Pear",
# "Bulmers Pear Cider",
# "Lilleys Bee Sting Pear Cider",
# "Sting Odd Pear",
# "Cornish Orchards Pear Cider",
# "Magners Pear",
# "Kopparberg Pear",
# "Rekorderlig Pear",
# "Malvern Hills Black Pear (Cask)",
# "Brothers Strawberry And Lime",
# "Appleshed Dark Fruits Cider",
# "Ascension Shimmy",
# "Ascension Wrath",
# "Aspall Pip & Wild Blackberry And Nettle",
# "Aspall Waddlegoose Lane Three Berry",
# "Barbourne Cherry Bakewell",
# "Bensons Raspberry and Lime Cider",
# "Blind Pig Bourbon and Blueberry",
# "Blind Pig Whiskey Honey and Apple",
# "Bottle Kicking Apple And Mango",
# "Broadoak Mango Cider",
# "Broadoak Mulled Cider",
# "Broadoak Pear and Chilli",
# "Broadoak Twisted Lime",
# "Brothers Cherry Bakewell",
# "Brothers Cloudy Lemon",
# "Brothers Marshmallow",
# "Brothers Parma Violet Cider",
# "Brothers Pink Grapefruit Cider",
# "Brothers Rhubarb and Custard",
# "Brothers Strawberries And Cream",
# "Brothers Strawberry & Kiwi",
# "Brothers Strawberry And Lime",
# "Brothers Strawberry Pear Cider",
# "Brothers Tutti Frutti Cider",
# "Brothers Wild Fruit Cider",
# "Bulmers Crushed Red Berries & Lime",
# "Carling Black Fruit Cider",
# "Cock Eyed Hedge Rose",
# "Cornish Berry Rattler",
# "Cornish Orchards Blush Cider",
# "Cornish Orchards Cherry and Blackberry",
# "Cornish Orchards Hedgerow",
# "Cornish Orchards Hedgerow Cider",
# "Cornish Orchards Raspberry and Elderflower",
# "Cotswold Cider Company Muscle Mary",
# "Dorset Orchards Apple Bee",
# "Duddas Tun Cherry Cider",
# "Duddas Tun Salted Caramel",
# "Garden Cider Company Blueberry",
# "Garden Cider Company Plum And Ginger",
# "Garden Cider Company Raspberry And Rhubarb",
# "Garden Cider Company Wild Strawberry",
# "Ham Hill Bop Drop",
# "Harrys Dirty Harrys Raspberry And Blackcurrant Cider",
# "Harrys Sutton Comfort Cider",
# "Hawkes Dead And Berried",
# "Hawkes Pineapple Punch",
# "Hawkes Urban Orchard Mixed Berry",
# "Healeys Cornish Rattler Pineapple",
# "Healeys Cornish Rattler Strawberry And Lime",
# "Herrljunga Blackcurrant & Lime",
# "Herrljunga Strawberry & Vanilla",
# "Hogans Wild Elder",
# "Hunts Hazy Dazy",
# "Hunts Raspberry Devon Cider",
# "Iford Wild Juice",
# "Kingstone Press Wild Berry",
# "Kopparberg Black",
# "Kopparberg Blackberry and Lime",
# "Kopparberg Blueberry & Lime",
# "Kopparberg Cherry",
# "Kopparberg Elderflower & Lime",
# "Kopparberg Light Passionfruit",
# "Kopparberg Mixed Fruit Tropical",
# "Kopparberg Mixed Fruits",
# "Kopparberg Mixed Fruits Non-Alcoholic",
# "Kopparberg Passionfruit",
# "Kopparberg Passionfruit And Orange",
# "Kopparberg Raspberry",
# "Kopparberg Rhubarb",
# "Kopparberg Spiced Blackberry",
# "Kopparberg Strawberry And Lime",
# "Kopparberg Strawberry And Lime Non-Alcoholic",
# "Kopparberg Summer Punch",
# "Kopparberg Wild Berries",
# "Kopparberg X Strong Raspberry",
# "Lilley Winter Fruits",
# "Lilleys Apple and Blackberry",
# "Lilleys Apples and Pears",
# "Lilleys Cherries And Berries",
# "Lilleys Colider",
# "Lilleys Crazy Goat",
# "Lilleys Elderflower",
# "Lilleys Gingerbread Cider",
# "Lilleys Lemon and Lime",
# "Lilleys Mango",
# "Lilleys Mango Cider",
# "Lilleys Mango Cider (Cask)",
# "Lilleys Mulled Cider",
# "Lilleys Passion Fruit Martini",
# "Lilleys Peach",
# "Lilleys Pear And Raspberry (Cask)",
# "Lilleys Pina Colada Cider",
# "Lilleys Pineapple Cider",
# "Lilleys Raspberry Mojito Cider",
# "Lilleys Rhubarb",
# "Lilleys Strawberry Cider",
# "Lilleys Tropical Cider",
# "Lilleys Whisky Cider",
# "Lilleys Woo Woo Cider",
# "Lost Orchards Cider Dark Berries",
# "Lost Orchards Cider Scottish Red Berries & Lime",
# "Lyme Bay Annings Crushed Mixed Berries",
# "Lyme Bay Annings Elderflower And Cucumber",
# "Lyme Bay Annings Pear and Peach",
# "Lyme Bay Annings Pink Grapefruit and Pineapple",
# "Lyme Bay Annings Strawberry and Lyme",
# "Maeloc Pineapple And Pear",
# "Magners Dark Fruit",
# "Magners Orchard Berries",
# "Millwhites Apples and Pears",
# "Norcotts Rhubarb Cider",
# "Old Mout Cider Berries & Cherries",
# "Old Mout Cider Berries & Cherries Alcohol Free",
# "Old Mout Cider Kiwi & Lime",
# "Old Mout Cider Passionfruit & Apple",
# "Old Mout Cider Pineapple & Raspberry",
# "Old Mout Cider Pomegranate & Strawberry",
# "Old Mout Cider Watermelon and Lime",
# "Old Mout Pineapple & Raspberry Alcohol Free",
# "Old Mout Strawberry & Apple",
# "Oldfields Orchard Berry Cider",
# "Peacock Mango & Lime Cider",
# "Pearsons Medium Dry Cider",
# "Pimms Cider Cup Strawberry & Cucumber",
# "Pulp Mango And Lime",
# "Pulp Rhubarb Craft Cider",
# "Purbeck No 10",
# "Rattler Strawberry And Lime",
# "Rekorderlig Blood Orange",
# "Rekorderlig Botanicals Blackberry Violet Juniper",
# "Rekorderlig Botanicals Grapefruit & Rosemary",
# "Rekorderlig Botanicals Peach & Basil",
# "Rekorderlig Botanicals Rhubarb Lemon & Mint",
# "Rekorderlig Mango and Raspberry",
# "Rekorderlig Passion Fruit",
# "Rekorderlig Peach & Apricot",
# "Rekorderlig Pink Lemon Cider",
# "Rekorderlig Spiced Plum",
# "Rekorderlig Strawberry & Lime",
# "Rekorderlig Strawberry & Lime Low Alcohol",
# "Rekorderlig Watermelon",
# "Rekorderlig Wild Berries",
# "Sams Cider Fruity Blackcurrant",
# "Sams Fruity Raspberry",
# "Sandford Orchard Berry Lane",
# "Sandford Orchard Fannys Bramble",
# "Sandford Orchard Old Blossom",
# "Sandford Orchard Strawberry Lane",
# "Sandford Orchards St Louis Hopped",
# "Saxbys Blackcurrant Cider",
# "Saxbys Blackcurrant Cider Sparkling",
# "Saxbys Plum Cider",
# "Saxbys Rhubarb Cider",
# "Saxbys Strawberry Cider",
# "Saxbys Strawberry Cider (Cask)",
# "SeaCider Black Cherry",
# "Seacider Blood Orange",
# "SeaCider Honeycomb Infused",
# "SeaCider Lemon Meringue Pie",
# "SeaCider Mandarin",
# "Seacider Mango",
# "SeaCider Marmalade",
# "SeaCider Passion Fruit",
# "SeaCider Raspberry Ripple",
# "SeaCider Rhubarb",
# "SeaCider Strawberry",
# "SeaCider White Peach",
# "Sheppys Cider with Elderflower",
# "Sheppys Raspberry",
# "Sheppys Raspberry Cider",
# "Skal Forrest Berries Cider",
# "Skal Rhubarb And Pink Grapefruit",
# "Skal Strawberry And Lime Cider",
# "Skuna Fruition",
# "Slightly Foxed Mango Cider",
# "Smirnoff Cider Mandarin And Pink Grapefruit",
# "Smirnoff Cider Passion Fruit And Lime",
# "Smirnoff Cider Raspberry And Pomegranate",
# "Snails Bank Fruit Bat",
# "Snails Bank Mango Cider",
# "Snails Bank Pineapple and Pink Grapefruit",
# "Snails Bank Rhubarb",
# "Snails Bank Strawberry and Lime",
# "Somersby Blackberry Cider",
# "Somersby Strawberry and Rhubarb Cider",
# "South West Orchards Raspberry Cider",
# "Stella Cidre Raspberry",
# "Stowford Press Dark Berry",
# "Strongbow Dark Fruit",
# "Strongbow Rose",
# "Strongbow Ultra Dark Fruit",
# "Thatchers Blood Orange",
# "Thatchers Cloudy Lemon",
# "Thatchers Dark Berry",
# "Thistly Cross Elderflower",
# "Thistly Cross Strawberry",
# "Tomos Watkin Very Berry",
# "Trenchmore Farm Silly Moo Cowfold Cider",
# "Turners Elderflower",
# "Westons Old Rosies Pig Old Banger (Cask)",
# "Westons Raspberry Roller",
# "Westons Rosies Pig Flat Tyre (Cask)",
# "Westons Rosies Pig Mulled Cider",
# "Westons Rosies Pig Raspberry Cloudy Cider",
# "Westons Rosies Pig Rhubarb",
# "Westons Rosies Pig Rusted Wheel",
# "Westons Rosies Pig Strawberry and Elderflower",
# "Westons Rosies Pig Tropical",
# "Westons Twist Raspberry",
# "Wignac Cidre Alcohol Free",
# "Wignac Cidre Rose",
# "Babycham Original",
# "Belnor Sparkling Perry",
# "Broadoak Premium Perry (Cask)",
# "Brothers Festival Strength Pear Cider",
# "Bulmers Pear Cider",
# "Burrow Hill Perry",
# "Charmaine Poire Mousseux Superieur Demi Sec",
# "Cornish Orchards Pear",
# "Cornish Orchards Pear Cider",
# "Cornish Pear Rattler",
# "Cornish Rattler Pear",
# "Gwatkin Farmhouse Perry",
# "Gwynt Y Ddraig Perry Vale",
# "Gwynt Y Ddraig Two Trees Perry",
# "Hallets Real Perry",
# "Henneys Dry Cider",
# "Henry Westons Country Perry Cask Conditioned Bag In Box",
# "Herrljunga Swedish Pear Cider",
# "Hogans Vintage Perry",
# "Kopparberg Pear",
# "Kopparberg Pear Non-Alcoholic",
# "Lilleys Bee Sting Pear Cider",
# "Lilleys Pickled Parrot Perry",
# "Lyme Bay Annings Pear And Mint",
# "Magners Pear",
# "Mr Whiteheads Midnight Special",
# "Mr Whiteheads Novo Pyrus Perry",
# "Newton Court Panting Partridge (Cask)",
# "Newton Court Winnals Longdon Perry (Cask)",
# "Norcotts Pear Cider",
# "Old Mout Cider Pineapple & Raspberry",
# "Olivers Lemonade Perry",
# "Perrys Grey Heron",
# "Rekorderlig Pear",
# "Ross On Wye Flakey Bark Perry",
# "Sam Smiths Organic Perry",
# "Sassy Pear Cider",
# "Snails Bank Very Perry",
# "Sting Odd Pear",
# "Sxollie Packham Pear Perry",
# "Westons Perry",
# "Westons Wyld Wood Organic Pear Cider",
# "Brothers Wild Fruit Cider",
# "Brothers Marshmallow",
# "Brothers Rhubarb and Custard",
# "Brothers Parma Violet Cider",
# "Kopparberg Raspberry",
# "Carling Black Fruit Cider",
# "Aspall Isabels Berry",
# "Brothers Tutti Frutti Cider",
# "Cornish Orchards Cherry and Blackberry",
# "Brothers Strawberries And Cream",
# "Healeys Cornish Rattler Strawberry And Lime",
# "Brothers Toffee Apple Cider",
# "Lilleys Cherries And Berries",
# "Harrys Flash Harrys Mango & Lime Cider",
# "Bulmers Crushed Red Berries & Lime",
# "Henry Westons Vintage",
# "Kingstone Press Wild Berry",
# "Cornish Orchards Raspberry and Elderflower",
# "Kopparberg Blueberry & Lime",
# "Harrys Dirty Harrys Raspberry And Blackcurrant Cider",
# "Lilleys Mango",
# "Harrys Sutton Comfort Cider",
# "Cornish Orchards Blush Cider",
# "Kentish Pip Craftsman Cider",
# "Kopparberg Elderflower & Lime",
# "Lilleys Mulled Cider",
# "Kopparberg Mixed Fruit Tropical",
# "Kopparberg Mixed Fruits",
# "Magners Dark Fruit",
# "Kopparberg Spiced Blackberry",
# "Kopparberg Mixed Fruits Non-Alcoholic",
# "Kopparberg Passionfruit",
# "Kopparberg Passionfruit And Orange",
# "Lilleys Strawberry Cider",
# "Kopparberg Rhubarb",
# "Kopparberg Strawberry And Lime Non-Alcoholic",
# "Rekorderlig Botanicals Peach & Basil",
# "Lilleys Apples and Pears",
# "Lilleys Passion Fruit Martini",
# "Kopparberg X Strong Raspberry",
# "Old Mout Cider Kiwi & Lime",
# "Magners Rose Cider",
# "Kopparberg Strawberry And Lime",
# "Old Mout Cider Berries & Cherries",
# "Saxbys Sour Cherry Cider",
# "Stowford Press Dark Berry",
# "Rekorderlig Strawberry & Lime Low Alcohol",
# "Old Mout Cider Berries & Cherries Alcohol Free",
# "Skal Strawberry And Lime Cider",
# "Somersby Blackberry Cider",
# "Westons Rosies Pig Mulled Cider",
# "Old Mout Cider Watermelon and Lime",
# "Strongbow Rose",
# "Strongbow Ultra Dark Fruit",
# "Rekorderlig Wild Berries",
# "Rekorderlig Botanicals Grapefruit & Rosemary",
# "Thatchers Dark Berry",
# "Westons Rosies Pig Cloudy Cider",
# "Westons Rosies Pig Rhubarb",
# "Saxbys Plum Cider",
# "Saxbys Rhubarb Cider",
# "Westons Rosies Pig Strawberry and Elderflower",
# "Sheppys Raspberry Cider",
# "Saxbys Strawberry Cider",
# "Snails Bank Fruit Bat",
# "Westons Rosies Pig Tropical",
# "Snails Bank Strawberry and Lime",
# "Skal Rhubarb And Pink Grapefruit",
# "Stowford Press Mixed Berries",
# "Strongbow Dark Fruit",
# "Thatchers Cloudy Lemon",
# "Westons Mortimers Orchard English Berry Cider",
# "Westons Old Rosie with Rhubarb (Cask)",
# "Westons Old Rosies Pig Old Banger (Cask)",
# "Westons Rosies Pig Flat Tyre (Cask)",
#
# "SeaCider Gingerbread",
# "Abrahalls AD Dry Still Cider (Cask)",
# "Healeys Cornish Rattler Mulled",
# "Sassy Organic Cider",
# "Sassy Rose Cider",
# "Aspall Waddlegoose Lane Deben Draught",
# "Abrahalls Thundering Molly",
# "Norcotts Raspberry and Orange Cider",
# "Thistly Cross Jaggy Thistle Medium Dry (Cask)",
# "Aspall Organic Suffolk Cyder",
# "Aston Manor Friels Apple And Spiced Plum",
# "Hunts Pixie Juice",
# "Hoxton Cidersmiths Sixpointsix",
# "Abrahalls Ruby Tuesday",
# "Thistly Cross Original Cider (Still)",
# "Thistly Cross Ginger",
# "Taunton English Berry Cider",
# "Chant Badgers Spit Cider",
# "Healeys Cornish Rattler Peach",
# "Healeys Cornish Rattler 4.8% Cyder",
# "Purbeck Katy And Perry",
# "Richs Legbender Cider (Cask)",
# "Norcotts Strawberry And Lime",
# "Luscombe Organic Devon cider",
# "SeaCider Blueberry",
# "Lilleys Rum Cider",
# "Herrljunga Ginger & Lemon",
# "Kingstone Rosey",
# "Hunts Wobbler Cider",
# "Bulmers Wild Blueberry and Lime",
# "Dunkertons Perry",
# "Healeys Cornish Rattler Mango",
# "Orchard Pig The Hogfather (Cask)",
# "Gwatkin No Bull Cider",
# "Chaplin and Corks Somerset Reserve Cider",
# "Special VAT",
# "Hunts Thrasher Cider",
# "Cock Eyed Monkey Mango",
# "SeaCider Bourbon Barrell",
# "Norcotts Mango & Lime Cider",
# "Abrahalls Celtic Tiger",
# "South Hams Fortnum & Mason Mulled Devon Cider",
# "Abrahalls Loubi Lou",
# "Lilleys Cheeky Pig",
# "Drynks Smashed Apple Cider",
# "Garden Cider Company Elderflower",
# "Orchard Pig Navelgazer",
# "Thistly Cross Strawberry Red (Cask)",
# "Lilleys Gladiator (Cask)",
# "Lost Orchards Cider Pure Apple",
# "Lambrini Cherry",
# "Gwynt Y Ddraig Happy Daze",
# "Gwynt Y Ddraig Fiery Fox",
# "Sandford Orchard Cider Ginger",
# "Thatchers Vintage",
# "Strongbow Sirrus",
# "Bays Windfall Cider",
# "Lilleys Wild Dog",
# "Lilleys Dark Sider",
# "Thistly Cross Original Sparkling Cider",
# "Chardolini Perry",
# "Abrahalls Cracklin Rosie Perry",
# "Abrahalls Tutti Frutti",
# "Mallets Dark Fruit Cider",
# "Brothers Raspberry Ripple",
# "Sheppys Special Edition Cider",
# "Snails Bank Raspberry",
# "Lilleys Red Rabbit (Cask)",
# "Lilleys Captain Rum Cider",
# "Cockeyed Pear Mania",
# "Thatchers Dry Cider (Cask)",
# "Dunkertons Organic Cider",
# "Lilleys Lemon And Ginger",
# "Orchard Pig Maverick Chilli and Ginger Cider",
# "Snails Bank Tumbledown",
# "Gaymers Cider",
# "Lilleys Somerset Dry",
# "Aspall Pip & Wild Strawberry And Rose Cider",
# "Aspall Cyderkyn",
# "Snails Bank Tumbledown Dry",
# "Galipette Cidre Brut",
# "Herrljunga Swedish Apple Cider",
# "Abrahalls Cloudy Apple Cider",
#
# ]
#
# df = df[~((df['product_class'] == 'Cider') & (~df['product'].isin(allowed_ciders)))]
