import seaborn as sns
data = sns.load_dataset("penguins")
print(data[:5])
print(data.shape)
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"D:\Data set\read.csv")
print(data)
data.plot()
plt.show()

