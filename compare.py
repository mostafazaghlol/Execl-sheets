import pandas as pd

# Load the first Excel sheet into a DataFrame
df1 = pd.read_excel('sheet1.xlsx')

# Load the second Excel sheet into a DataFrame
df2 = pd.read_excel('sheet2.xlsx')

# loop through each item in df2
for item in df2['username']:
    if item in df1['username'].values:
        df2 = df2[df2['username'] != item]

# reset the index after deleting the rows
df2 = df2.reset_index(drop=True)

print(df2)
