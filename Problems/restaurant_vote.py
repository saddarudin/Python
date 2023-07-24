import pandas as pd
import numpy as np

df = pd.read_csv("Restaurant.csv", names=["name", "income"], skiprows=[0])
print(df)
print(df.describe())
