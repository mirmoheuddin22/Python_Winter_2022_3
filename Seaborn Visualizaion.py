import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = sns.load_dataset("penguins")
print(data[:5])
print(data.shape)
sns.set_theme()
# For the image quality of the graphic.
sns.set(rc={"figure.dpi":300})
# For the size of the graphics
sns.set(rc = {"figure.figsize":(6,3)})
sns.scatterplot( x = "bill_length_mm", y = "bill_depth_mm", data = data, hue = "species")
plt.show()
sns.histplot(x = "flipper_length_mm", data = data)
sns.histplot(data=data, y="flipper_length_mm")
#controlling the width of the rectangles in the histogram:
sns.histplot(data=data, x="flipper_length_mm", binwidth=3)
KDE represents the probability distribution curve to the histogram plot.
sns.histplot(data=data, x="flipper_length_mm", kde=True)
#Using hue parameter to see the histograms of categories.
sns.histplot(data=data, x="flipper_length_mm", hue="species")
sns.barplot(x = "species", y = "flipper_length_mm", data = data)
sns.barplot(x = “species”, y = “flipper_length_mm”, data = data, hue = “sex”)
sns.boxplot(x = "species", y = "flipper_length_mm", data = data)
sns.boxplot(x = "species", y = "flipper_length_mm", data = data, hue = "sex")
sns.violinplot(x = 'species', y = 'flipper_length_mm', data = data)
sns.violinplot(x = "species", y = "flipper_length_mm", data = data, hue = "sex")
# Using facet grid to see a grid graph of the different subsets in your dataset:
sns.FacetGrid(data, col="island", row="sex")
sns.FacetGrid(data, col="island", row="sex").map(sns.histplot, "flipper_length_mm")
sns.FacetGrid(data, col="island", row="sex").map(sns.distplot, "flipper_length_mm")
#Seeing the pair relationship between the variables in the dataset:
sns.pairplot(data, hue="species", height=3)
sns.pairplot(data, hue="species", diag_kind="hist")
#Looking for correlations between numerical variables:
sns.heatmap(data.corr())
sns.heatmap(data.corr(), annot=True)
plt.show()