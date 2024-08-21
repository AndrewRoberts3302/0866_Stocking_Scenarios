# from pathlib import Path
from a_Data_Path.a_data_path import data_path
from r_remove_the_inbetween_periods_OPTION_EDIT import df

# cwd = Path(__file__).parent

df.to_csv(data_path / "data_clean.csv", index=False)
