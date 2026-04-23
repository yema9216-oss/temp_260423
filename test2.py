import pandas as pd

df = pd.read_csv(
    'data1.csv',

)

df["area"]=df["area"].fillna("UNKNOW")
area_col=df["area"]

# for i in range(len(area_col)):
#     area_col[i].upper()

df["area"]=df["area"].str.upper()
df["area"]=df["area"].str.replace("MACAO","MACAU")
print(df["area"])

# print(df)
df.to_excel('data.xlsx', index=False)