import pandas as pd
data = {
    "Name":["anju", "marie", "john"],
    "age":[25, 30, 28],
    "city": ["paris", "lyon", "paris"]

}
df = pd.DataFrame(data)
df.to_csv("people.csv", index=False)
df.to_excel("people.xlsx", index=False)
print(df)
df = pd.DataFrame(data)
print(df["Name"])
print(df["age"])
print(df["city"])
print(df[["Name", "age"]])
print(df.iloc[2])
print(df.iloc[0:2])
print(df[df["city"] == "paris"])