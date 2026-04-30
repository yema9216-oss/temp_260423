import re
import pandas as pd

df = pd.read_csv(
    'data1.csv',
    
)
df.to_excel('data_org.xlsx', index=False)

df["team_name"]=df["team_name"].str.title().str.lstrip()
df["school"]=df["school"].str.title()
df["area"]=df["area"].fillna("UNKNOW").str.title().str.replace("Macao","Macau")
df["contact"]=df["contact"].fillna("UNKNOW")
df.insert(5,"problem_type",df["problem"])
df["problem_type"]=df["problem_type"].map(lambda s:s[0])

def temp_func(s:str):
    s=re.sub(r"(\d+)/100",r"\1",s)
    m=re.search(r"\d+",s)
    if m is None: return "Null"
    return m.group()

df["score_text"]=df["score_text"].str.title().str.replace("Missing","Null").map(temp_func)

del temp_func

df.to_excel('data.xlsx', index=False)