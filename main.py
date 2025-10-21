import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Titanic.csv')
print(df.head())

# 2. Basic info
print(df.info())
print(df.describe())

# 3. Handle missing values
df = df.dropna()

# 4. Visualize distributions
sns.histplot(df['column_name'])
plt.show()

# 5. Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
