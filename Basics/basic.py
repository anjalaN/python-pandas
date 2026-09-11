import pandas as pd

data = {
    "name": ["anju", "sara", "john"],
    "age": [25, 30, 28]
}

df = pd.DataFrame(data)
df["age"].mean()
df["age"].median()
df["age"].std()

print(df)
print(df["age"].mean())
print(df["age"].median())
print(df["age"].std())
print(df["age"].var())
print(df["age"].sample())
print(df["age"].sample(2))
print(df["age"].nlargest(2))
print(df["age"].nsmallest(2))