# from pathlib import Path
from a_Data_Path.a_data_path import data_path

from y_extract_lists import list_scenario, list_market, list_product, list_quarters, results

# cwd = Path(__file__).parent

results.to_csv(data_path / "results_quarters.csv", index=False)

# These are written within the monthly results.
# list_scenario.to_ csv(cwd / "list_scenario.csv", index=False)
# list_market.to_csv(cwd / "list_market.csv", index=False)
# list_product.to_csv(cwd / "list_product.csv", index=False)# list_quarters.to_csv(cwd / "list_quarters.csv", index=False)
