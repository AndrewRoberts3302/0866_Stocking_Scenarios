from b_read_in_the_data import df

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

print("\nThe head of df is:\n", df.head(2), "\n")

