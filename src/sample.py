# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
df = pd.read_excel('../data/ST60B_2024.xlsx')
df = df.iloc[4:]
print(df.head())

# %%
engine = create_engine("sqlite:///../db/oiltest.db")
df.to_sql('st60b_2024', engine, if_exists='replace', index=False)
engine.close()
# %%

