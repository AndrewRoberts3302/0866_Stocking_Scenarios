import pandas as pd

from f_append_products_EDIT import df

from pathlib import Path

print("\n---------------------------------------------------------------------\n")
print("RUNNING FILE: ", Path(__file__).name)
print("\n---------------------------------------------------------------------\n")

group_columns = [
    "date", "market", "product", "product_class", "product_group", "scenario"
]

sh = df.loc[df["share_group"] == 1]

sh = sh.groupby(group_columns).agg({
        "volume": "sum",
        "value": "sum"
}).rename(
    columns={
        "volume": "product_volume",
        "value": "product_value"
})

for m in ['value', 'volume']:
    sh[f'{m}_share_of_group'] = sh[f'product_{m}'] / sh.groupby(
        [col for col in group_columns if col not in ['product', 'product_class']], observed=True
    )[f'product_{m}'].transform('sum')

    sh[f'{m}_share_of_class'] = sh[f'product_{m}'] / sh.groupby(
        [col for col in group_columns if col not in ['product']], observed=True
    )[f'product_{m}'].transform('sum')


--------------------------------------------------------------------------------------
import pandas as pd

results = pd.read_csv('')

metrics = ['value', 'volume']

results = results.groupby(
    [col for col in results.columns not in metrics + [f'share_in__class_{m}' for m in metrics]]
).agg({f'share_in_group_{m}': 'sum' for m in metrics}).reset_index()

results.to_csv('', index=False)