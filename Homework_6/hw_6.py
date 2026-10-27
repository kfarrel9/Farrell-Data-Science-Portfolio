import pandas as pd
from sklearn.datasets import fetch_california_housing

# Load the housing dataset
housing = fetch_california_housing()

# create dataframe
X = pd.DataFrame(housing.data, columns=housing.feature_names) 
y = pd.Series(housing.target, name='med_house_value')

# display first 5 rows
print(X.head())

# print features and check for missing values
print(X.columns)
print(X.isnull().sum())

# generate summary statistics
print(X.describe())