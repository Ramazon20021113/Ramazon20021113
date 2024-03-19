# -*- coding: utf-8 -*-
"""Random Forest Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nkD0Iz-PfkyjUOin-KJzZTec-pnBGn3u
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import warnings

from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score

warnings.filterwarnings('ignore')

df= pd.read_csv('Position_Salaries.csv')
print(df)

df.info()

# Df sizning DataFrame deb faraz qiling
X = df.iloc[:,1:2].values #Xususiyatlari
y = df.iloc[:,2].values #Maqsadli o'zgaruvchi

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

#Kategorik o'zgaruvchilarni tekshiring va boshqaring
label_encoder = LabelEncoder()
x_categorical = df.select_dtypes(include=['object']).apply(label_encoder.fit_transform)
x_numerical = df.select_dtypes(exclude=['object']).values
x = pd.concat([pd.DataFrame(x_numerical), x_categorical], axis=1).values

# Tasodifiy o'rmon regressiyasini ma'lumotlar to'plamiga moslashtirish
regressor = RandomForestRegressor(n_estimators=10, random_state=0, oob_score=True)

# Regressorni x va y ma'lumotlari bilan moslang
regressor.fit(x, y)

# Modelni baholash
from sklearn.metrics import mean_squared_error, r2_score

# OOB reytingiga kirish
oob_score = regressor.oob_score_
print(f'Out-of-Bag Score: {oob_score}')

# Xuddi shu ma'lumotlar yoki yangi ma'lumotlar bo'yicha bashorat qilish
predictions = regressor.predict(x)

# Modelni baholash
mse = mean_squared_error(y, predictions)
print(f'Mean Squared Error: {mse}')

r2 = r2_score(y, predictions)
print(f'R-squared: {r2}')

import numpy as np

# X_grid faqat bitta xususiyat bilan yaratilgan deb hisoblasak, uni uchta xususiyatga ega qilib sozlangX_grid = np.arange(min(X), max(X), 0.01)[:, np.newaxis]
X_grid = np.arange(min(X), max(X), 0.01)[:, np.newaxis]
# Yana ikkita xususiyat qo‘shing (masalan, kvadrat va kubik funksiyalar)
X_grid = np.concatenate((X_grid, X_grid**2, X_grid**3), axis=1)

#Regressor yordamida bashorat qiling
y_pred = regressor.predict(X_grid)

# Syujet tuzish
plt.scatter(X, y, color='blue', label='Real points')
plt.plot(X_grid[:,0], y_pred, color='green', label='Predicted points')

plt.title("Random Forest Regression Results")
plt.xlabel('Position level')
plt.ylabel('Position_Salary')
plt.legend()
plt.show()

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Regressor sizning o'qitilgan Tasodifiy o'rmon modelingiz deb faraz qiling
# O'rmondan bitta daraxtni tanlang, masalan, birinchi daraxt (indeks 0)
tree_to_plot = regressor.estimators_[0]

# Qaror daraxtini chizing
plt.figure(figsize=(20, 10))
plot_tree(tree_to_plot, feature_names=df.columns.tolist(), filled=True, rounded=True, fontsize=10)
plt.title("Decision Tree from Random Forest")
plt.show()