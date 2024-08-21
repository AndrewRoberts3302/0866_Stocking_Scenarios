import pandas as pd

from f_update_custom_quality import df
from b_read_in_the_data_EDIT import Spec_beer_products

print(df.head(5))


print("\nThe head of df before merging in Spec Beer product data is:\n", df.head(2), "\n")
print("\nThe head of Spec_beer_products is:\n", Spec_beer_products.head(2), "\n")
#
# Drop the product class column
# df = df.drop(["product_class"], axis=1)
# #
# # # Rename the custom dataframe for merging.
# Spec_beer_products =Spec_beer_products.rename(
#     columns={
#         "PT_ProductDescription": "product",
#         "PT_ClassificationLevel2Description": "product_class"
#     }
# )
# #
# # Merge the data.
# df = pd.merge(
#     df, Spec_beer_products,
#     left_on=["product"], right_on=["product"],
#     how="inner"
# )
#
# df.loc[df['product'] == 'Erdinger Heffe Weissbier', 'product_class'] = 'Speciality Beer'
# df['product_class'] = df['product_class'].replace(['Standard Speciality Lager', 'Premium Speciality Lager'], 'Speciality Beer')



# QC the merge.
# print("\nThe head of df after merging in the custom product data is:\n", df.head(2), "\n")

# if 'product_class' in df.columns:
#     df['product_class'] = df['product_class'].replace(
#         {'Standard Speciality Lager': 'Speciality Beer',
#          'Premium Speciality Lager': 'Speciality Beer',
#          'Keg Premium Bitter': 'Speciality Beer'}
#     )


# condition = (df['product_class'] == 'Keg Premium Bitter')
# df = df[~condition]

# df = df.drop(["product_class", "product", "product_group", ], axis=1)

# df =df.rename(
#     columns={
#         "PT_Segment": "product",
#         "ClassificationLevel4Description": "product_class",
#         "ClassificationLevel5Description": "product_group"
#     }
# )


# speciality_beer_products = [
#     'Kwak', 'Sam Smiths Double Four', 'St Austell Dawn', 'Duvel Dark Maredsous 8',
#     'Duvel Maredsous Triple 10', 'Erdinger Urweisse', 'Flensburger Lager', 'Liefmans Fruit Beer',
#     'Liefmans Fruitesse On The Rocks', 'Oakham Citra (Cask)', 'Benediktiner Weissbier', 'Chimay Gold',
#     'Erdinger Dunkel', 'Franziskaner Hefe', 'Konig Ludwig', 'Leffe Blonde', 'Affligem Blond',
#     'Cantillon Ros De Gam', 'Erdinger Oktoberfest', 'Grimbergen Blond', 'House Of Apres Duette',
#     'Sambrooks Junction Ale (Cask)', 'Spaten Munchner Hell', 'St Austell Arnie', 'Trappistes Rochefort 10',
#     'Trappistes Rochefort 6', 'Bacchus Framboise', 'Chimay Blue', 'Chimay Red', 'Chimay White', 'Duvel',
#     'Fruli', 'Maisels Weisse', 'Westmalle Dubbel', 'Wold Top Anglers Reward (Cask)', 'La Trappe Dubbel',
#     'Redemption Trinity (Cask)', 'Sambrooks Powerhouse Porter (Cask)', 'Trappistes Orval',
#     'Trappistes Rochefort 8', 'Westmalle Triple', 'Augustiner Weissbier', 'Erdinger Heffe Weissbier',
#     'Hoegaarden', 'Kasteel Rouge', 'Khukuri Lager', 'La Chouffe', 'La Trappe Blonde', 'Leffe Brune',
#     'Bacchus Kriek', 'Bellerose Biere Blonde Extra', 'De Koninck', 'Franziskaner Weissbier', 'Kasteel Tripel',
#     'La Trappe Quadrupel', 'La Trappe Triple', 'Liefmans Kriek', 'Westmalle Trappist Dubbel'
# ]
#
# df.loc[df['product'].isin(speciality_beer_products), 'product_class'] = 'Speciality Beer'





print(df.head(20))
