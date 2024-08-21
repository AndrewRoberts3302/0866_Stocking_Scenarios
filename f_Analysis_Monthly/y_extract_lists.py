from x_merge_results import results

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

list_dates = results[["date"]]
list_dates = list_dates.drop_duplicates()
list_dates = list_dates.sort_values(by=["date"])

list_market = results[["market"]]
list_market = list_market.drop_duplicates()
list_market = list_market.sort_values(by=["market"])

list_scenario = results[["scenario"]]
list_scenario = list_scenario.drop_duplicates()
list_scenario = list_scenario.sort_values(by=["scenario"])

list_product = results[["product"]]
list_product = list_product.drop_duplicates()
list_product = list_product.sort_values(by=["product"])
########################################################
#EPOS only
# results["ros_volume"] = results["ros_volume"] / 100000