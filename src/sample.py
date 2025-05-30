# %%
import pandas as pd
from sqlalchemy import create_engine

# %%
# Import takes a minute; run it its own cell
df_raw = pd.read_excel('../data/raw/ST60B_2024.xlsx', header=None)
df_raw = df_raw[4:]

# %%
df_raw.head(1)

# %%
new_header = df_raw.iloc[3]

# %%
new_header.head()
df_raw.columns = [str(col).strip().lower().replace(" ", "_") for col in new_header]
df = df_raw.iloc[4:].reset_index(drop=True)
# df_raw.columns = [str(col).strip().lower().replace(" ", "_") for col in new_header]
# df = df_raw.iloc[3:].reset_index(drop=True)


# %%
df.head()


# %%
# Need to clean the data here, then put it in a table in a database
# df.info()
# df.describe()
# df.dtypes()
# df.head()
df.isnull().sum()
df.head()
df.describe()

# %%
df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]
df.head()

# %%
# engine = create_engine("sqlite:///../db/oiltest.db")
# df.to_sql('st60b_2024', engine, if_exists='replace', index=False)
# engine.close()
