import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data_kepuasan_streaming.csv')
print(df.head())

df.info()
df.describe()
df.isnull().sum()

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Heatmap Korelasi Fitur")
plt.show()

sns.histplot(df["durasi_dengar"], kde=True)
plt.title("Distribusi Durasi Dengar")
plt.show()

sns.countplot(x="kepuasan", data=df)
plt.title("Distribusi Kepuasan Pelanggan")
plt.show()

sns.boxplot(x="kepuasan", y="durasi_dengar", data=df)
plt.title("Durasi Dengar vs Kepuasan")
plt.show()

sns.barplot(x="langganan_premium", y="kepuasan", data=df)
plt.title("Premium vs Kepuasan")
plt.show()
