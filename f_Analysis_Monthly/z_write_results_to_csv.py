# from pathlib import Path
from a_Data_Path.a_data_path import data_path

from y_extract_lists import list_scenario, list_market, list_product, list_dates, results

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

# cwd = Path(__file__).parent

results.to_csv(data_path / "results_monthly.csv", index=False)

list_scenario.to_csv(data_path / "list_scenario.csv", index=False)
list_market.to_csv(data_path / "list_market.csv", index=False)
list_product.to_csv(data_path / "list_product.csv", index=False)
list_dates.to_csv(data_path / "list_dates.csv", index=False)
