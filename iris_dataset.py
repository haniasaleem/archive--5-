import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

"""**READ** **DATASET**"""

iris = pd.read_csv("Iris.csv")

iris = iris.drop('Id',axis=1)

iris.info()

iris.describe()

"""**Display Entries**"""

# original dataframe
iris

"""**Create a new attribute (Flower) and update proper names**"""

def assign_flower(species):
    if species == 'Iris-setosa':
        return 'Setosa'
    elif species == 'Iris-versicolor':
        return 'Versicolor'
    elif species == 'Iris-virginica':
        return 'Virginica'
    else:
        return None

iris['Flower'] = iris['Species'].apply(assign_flower)

# updated dataframe
iris

"""**frequency (count) of each flower**"""

print(iris['Species'].value_counts())

"""**SCATTER PLOT**"""

g = sns.scatterplot(y='PetalWidthCm', x='PetalLengthCm', data=iris)
plt.title('Scatter Plot - PetalCm')

"""**HISTOGRAM USING MATPLOTLIB**"""

plt.figure(figsize=(8,6))
plt.hist(iris.PetalLengthCm)
plt.xlabel('PetalLengthCm')
plt.ylabel('Count')
plt.title('Histogram of PetalLenghtCm')

# Display the histogram
plt.show()

"""**HISTOGRAM USING SEABORN**"""

plt.figure(figsize=(12, 4))
sns.histplot(data=iris, x=iris.PetalWidthCm, kde=True)
plt.xlabel('PetalWidthCm')
plt.ylabel('Count')
plt.title(f'Histogram of PetalWidth')
plt.show()

"""BOXPLOT"""

plt.figure(figsize=(12, 8))  # Adjust the figure size as needed

plt.subplot(2,2,1)
sns.boxplot(data=iris, y=iris.SepalLengthCm)
plt.xlabel('SepalLengthCm')
plt.ylabel('Value')
plt.title(f'Boxplot of SepalLengthCm')

plt.subplot(2,2,2)
sns.boxplot(data=iris, y=iris.SepalWidthCm)
plt.xlabel('SepalWidthCm')
plt.ylabel('Value')
plt.title(f'Boxplot of SepalWidthCm')

plt.subplot(2,2,3)
sns.boxplot(data=iris, y=iris.PetalLengthCm)
plt.xlabel('PetalLengthCm')
plt.ylabel('Value')
plt.title(f'Boxplot of PetalLengthCm')

plt.subplot(2,2,4)
sns.boxplot(data=iris, y=iris.PetalWidthCm)
plt.xlabel('PetalWidththCm')
plt.ylabel('Value')
plt.title(f'Boxplot of PetalWidththCm')

plt.tight_layout()
plt.show()

"""**CORRELATION MATRIX**"""

attributes =[iris.SepalLengthCm,
              iris.SepalWidthCm,
              iris.PetalLengthCm,
              iris.PetalWidthCm]
df = pd.DataFrame(attributes)

# Calculate the correlation matrix
corr_matrix = df.corr()

# plt.figure(figsize=(8, 6))
# plt.show()
fig, ax = plt.subplots()

"""**Heatmap for the correlation**"""

features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
plt.figure(figsize=(8, 6))  # Adjust the figure size as needed

sns.heatmap(iris.corr(), annot=True, cmap='coolwarm', fmt=".3f", linewidths=0.5)
plt.xlabel('')
plt.ylabel('')
plt.title('Correlation Matrix')

plt.show()

"""**simple Linear
Regression Model**
"""

from sklearn.linear_model import LinearRegression

X = iris[['PetalLengthCm']]  # Independent variable (Petal Length)
y = iris['PetalWidthCm']     # Dependent variable (Petal Width)

# Create a linear regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.xlabel('PetalLengthCm')
plt.ylabel('PetalWidthCm')
plt.title('Linear Regression Model')
plt.legend()
plt.show()


# try for bell curve but not shows proper result.

mu = np.mean(y_pred)  # Mean
sigma = np.std(y_pred)  # Standard deviation
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 150)  # Values along the x-axis
y = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))  # Probability density function

plt.plot(X, y, color='red')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Probability Density')
plt.title('Bell Curve (Normal Distribution)')
plt.show()

from sklearn.model_selection import train_test_split
input_cols = ['PetalLengthCm']
output_variable = ['PetalWidthCm']
X = input_cols
y = output_variable

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=12)

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

"""**Pickle file**"""

# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))

 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)