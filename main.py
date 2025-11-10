from utlis.utlis import get_cols_name, change_dtype
import camelot
import pandas as pd
import camelot

docs = camelot.read_pdf(filepath="docs/Dok.pdf", pages="1")
df = docs[0].df

cols = get_cols_name(col_name="utlis/cols.conf")
df.columns = cols

df= change_dtype(df=df, dtype=int)
print(df.info())
print(df)