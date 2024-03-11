import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler


# Loading data
data = pd.read_excel("data.xlsx")
df  = data.copy()
df = df.set_index('country')

# Descriptive statistics
df.describe()

# Correlation matrix
plt.figure(figsize=(30,10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", vmin = -1, vmax = 1)
plt.title('Korelacja między zmiennymi')

# Coefficient of Variation
def cv(x):
    return x.std()/x.mean() 

cv_coefficients = [cv(df['life_expectancy']), cv(df['gdp_per_capita']),cv(df['unemploymnet_rate']),cv(df['crime_index']),cv(df['air_quality_index']),cv(df['gini_index'])]
variables = ['life_expectancy', 'gdp_per_capita', 'unemploymnet_rate', 'crime_index', 'air_quality_index', 'gini_index']

plt.figure(figsize=(30,10))
plt.bar(variables, cv_coefficients)
plt.title('Coefficient of Variation')
plt.xlabel('Variables')
plt.ylabel('Coefficient Value')
for i, v in enumerate(cv_coefficients):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')
plt.show()

# Linear Ordering - Hellwig's Method
data_stym = data.copy()
data_stym['unemploymnet_rate'] = data_stym['unemploymnet_rate'] * -1 
data_stym['crime_index'] = data_stym['crime_index'] * -1 
data_stym['air_quality_index'] = data_stym['air_quality_index'] * -1 
data_stym['gini_index'] = data_stym['gini_index'] * -1 
data_stym.head()

stand_data = data_stym.copy()
columns_to_standardize = stand_data.columns[1:]  
scaler = StandardScaler()
stand_data[columns_to_standardize] = scaler.fit_transform(data_stym[columns_to_standardize])
stand_data.head()

def transform_column(data_frame, column_name):
    max_value = data_frame[column_name].max()
    transformed_column = (data_frame[column_name] - max_value)**2
    return transformed_column

template_data = stand_data.copy()
columns_to_transform = template_data.columns[1:]

for column in columns_to_transform:
    template_data[column] = transform_column(template_data, column)

template_data.head()

# Sum after variables
columns_to_summ= template_data.columns[1:]
summed_values = template_data[columns_to_summ].sum(axis=1)
di = summed_values**(1/2)
# Creating a dataframe with country names and di values
di_df = pd.DataFrame({'Country': template_data['country'], 'di': di})

print("Wynik dla każdego kraju:")
di_df.head()

d0 = di.mean() + 2 * di.std()
si = di.copy()
si = 1 - di/d0
si_df = pd.DataFrame({'Country': template_data['country'], 'si': si})
sorted_si = data.copy()
sorted_si['Hellwig'] = list(si_df['si'])
sorted_si = sorted_si.sort_values(by="Hellwig", ascending=False)
sorted_si= sorted_si.reset_index(drop=True, inplace=False)
sorted_si.index = sorted_si.index + 1
sorted_si

# Method of Standardized Sums
columns_to_summ_stand_data= stand_data.columns[1:]
stand_sum = stand_data[columns_to_summ_stand_data].sum(axis=1)
stand_sum_df = pd.DataFrame({'Summ_after_variables': stand_sum})
index = (stand_sum - stand_sum.min())/(stand_sum - stand_sum.min()).max()
index_df = data.copy()
index_df['MSS'] = index
index_df = index_df.sort_values(by="MSS", ascending=False)
index_df=  index_df.reset_index(drop=True, inplace=False)
index_df.index = index_df.index + 1
index_df

# Cluster Analysis - K-means method
group_1 = ['Nigeria', 'Brazil', 'Colombia', 'Argentina']
group_2 = ['India', 'Algeria', 'Russia', 'Egypt', 'Indonesia', 'China', 'Mexico', 'Poland']
group_3 = ['Spain', 'Saudi Arabia', 'France', 'Canada', 'Sweden', 'USA', 'Australia', 'New Zealand', 'Germany', 'Japan', 'UK']
df_group_1 = data[data['country'].isin(group_1)]
df_group_2 = data[data['country'].isin(group_2)]
df_group_3 = data[data['country'].isin(group_3)]

# Calculating descriptive statistics for the variable_of_interest for each group
stats_group_1 = pd.DataFrame(df_group_1.describe().reset_index())
stats_group_2 = pd.DataFrame(df_group_2.describe().reset_index())
stats_group_3 = pd.DataFrame(df_group_3.describe().reset_index())

# Statistics for group 1
stats_group_1

# Statistics for group 2
stats_group_2

# Statistics for group 3
stats_group_3

# Cluster Analysis - Hierarchical grouping

group_A = ('Sweden', 'USA', 'Germany', 'New Zealand', 'France', 'Australia', 'Canada', 'UK')
group_B = ('Russia', 'Saudi Arabia', 'Spain', 'Japan', 'Poland')
group_C = ('Nigeria', 'Brazil', 'Colombia', 'Algeria', 'Argentina')
group_D = ('Mexico', 'Egypt', 'Indonesia', 'China', 'India')

df_group_A = data[data['country'].isin(group_A)]
df_group_B = data[data['country'].isin(group_B)]
df_group_C = data[data['country'].isin(group_C)]
df_group_D = data[data['country'].isin(group_D)]

# Calculating descriptive statistics for the variable_of_interest for each group
stats_group_A = pd.DataFrame(df_group_A.describe().reset_index())
stats_group_B = pd.DataFrame(df_group_B.describe().reset_index())
stats_group_C = pd.DataFrame(df_group_C.describe().reset_index())
stats_group_D = pd.DataFrame(df_group_D.describe().reset_index())

# Statistics for group A
stats_group_A

# Statistics for group B
stats_group_B

# Statistics for group C
stats_group_C

# Statistics for group D
stats_group_D