import pandas as pd
 
data = {
    'X1':[2.9, 2.4, 2, 2.3, 3.2],
    'X2':[9.2, 8.7, 7.2, 8.5, 9.6],
    'X3':[13.2, 11.5, 10.8, 12.3, 12.6],
    'X4':[2, 3, 4, 3, 2]
}
 
df = pd.DataFrame(data)

df.loc[len(df)] = [10, 20, 30, 40]
df['total'] = df.X1 +  df.X2 + df.X3 + df.X4
print(df)