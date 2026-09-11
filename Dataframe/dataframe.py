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
