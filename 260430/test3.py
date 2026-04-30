import requests
import pandas as pd

url="https://dsec.apigateway.data.gov.mo/public/KeyIndicator/VisitorArrivals"

response=requests.post(
    url=url,
    headers={"Authorization":"APPCODE 09d43a591fba407fb862412970667de4"},
)

print(response)
res_dict=response.json()

# print(res_dict)
val_list=res_dict["value"]["values"]

df=pd.DataFrame(val_list)

df["year"]=df["periodString"].str.split("年").str[0]
df["month"]=df["periodString"].str.split("年").str[1].str[0:-1]


df.groupby("year")



df.to_excel('data.xlsx', index=False)
