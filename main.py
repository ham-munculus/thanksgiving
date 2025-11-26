from pathlib import Path
import pandas as pd

MAC_PATH = Path("./data/mac.csv")
TURKEY_PATH = Path("./data/turkey.csv")
CROISSANTS_PATH = Path("./data/croissants.csv")
CRANBERRY_JAM_PATH = Path("./data/cranberry_jam.csv")
POTATO_SOUP_PATH = Path("./data/potato_soup.csv")
MAYO_PATH = Path("./data/mayo.csv")

menu = [MAC_PATH, TURKEY_PATH, CROISSANTS_PATH, CRANBERRY_JAM_PATH, POTATO_SOUP_PATH, MAYO_PATH]

menu_items = [pd.read_csv(f) for f in menu]

all_ingredients = pd.concat(menu_items)
master_list = all_ingredients.groupby("ingredient").agg({"quantity":"sum", "unit":"first"})
print(master_list)
master_list.to_csv("./data/master_list.csv", header=True)
