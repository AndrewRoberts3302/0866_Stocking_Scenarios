# from pathlib import Path
from a_Data_Path.a_data_path import data_path

from j_aggregate_the_dataframe_OPTION_EDIT import df

# cwd = Path(__file__).parent

df.to_csv(data_path / "data_reduced.csv", index=False)

print(df.head(100))



