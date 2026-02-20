import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("data.csv")
df.dropna(inplace=True)
df['Sales']=pd.to_numeric(df['Sales'],errors='coerce')
#df['Profit']=pd.to_numeric(df['Profit'],errors='coerce')

#df['Profit']=pd.to_numeric(df['Profit'],errors='coerce')
pivot_data=df.pivot_table(index="Region",columns="Category",values="Sales",aggfunc="sum")
sns.set(style="whitegrid",font_scale=1.1)
plt.figure(figsize=(10,6))
sns.heatmap(pivot_data,annot=True,fmt=".1f",cmap="YlGnBu",linewidths=0.5)
plt.title("Total  Sales by Region and Category",fontsize=14)
plt.xlabel("Product Category")
plt.ylabel("Region")
plt.tight_layout()
plt.show()