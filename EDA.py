### CONDUCTING DATA CLEANING AND INTIAL EDA OF GOODREADS DATA
#%%
import pandas as pd
# %%
df = pd.read_csv("goodreads_data.csv")
# %%
print(df.describe)
# %%
