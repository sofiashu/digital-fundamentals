import pandas as pd

df = pd.read_csv("wild_boars.csv")

with open("median_values.txt", "w", encoding="utf-8") as med:
    for col in df.columns[2:]:
        cont = df[col].median()
        med.write(f"{col}: {cont:.2f}\n")