import pandas as pd
df = pd.read_csv("penguin_species_dataset.csv")
print(df["Species"].value_counts())
