from pathlib import Path
import pandas as pd

MAC_PATH = Path("./data/mac.csv")
TURKEY_PATH = Path("./data/turkey.csv")


menu_items = [pd.read_csv(f) for f in [MAC_PATH, TURKEY_PATH]]

all_ingredients = pd.concat(menu_items)
master_list = all_ingredients.groupby("ingredient").agg({"quantity":"sum", "unit":"first"})
print(master_list)
