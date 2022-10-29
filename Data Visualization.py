import pandas as pd
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
cols = ["A", "B", "C"]
df = pd.DataFrame([list(s1), list(s2)], columns = cols) # df = DataFrame
print(df)
new_row = [7,8,9]
df.loc[-1] = new_row
print(df)
df.reset_index(drop = True)
print(df.reset_index(drop = True))
new_row = [7, 8, 9]
new_df = pd.DataFrame([new_row], columns = cols)
print(new_df)
df = pd.concat([new_df, df], ignore_index = True)
print(df)
import numpy as np
df = pd.DataFrame(np.insert(df.values, 1, new_row, axis = 0),columns =cols)
print(df)
