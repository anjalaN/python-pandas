import pandas as pd

data = {
    "name": ["anju", "sara", "john"],
    "age": [25, 30, 28]
}

df = pd.DataFrame(data)
df["age"].mean()
df["age"].median()

print(df)
print(df["age"].mean())
print(df["age"].median())