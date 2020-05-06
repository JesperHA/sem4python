import numpy as np
import pandas as pd


data = np.array([['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]])
print(type(data))
df = pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:])

# print(df)

# print(df['Col2'])

third_coloumn = df.iloc[:, 2]

# print(third_coloumn)

third_row = df.iloc[2, 1]

# print(third_row)
