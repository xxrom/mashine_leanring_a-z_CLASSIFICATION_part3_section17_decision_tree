# Decision Tree Classification
# алгоритм разделяем горизонтальными и вертикальными линиями всю область
# с точками, пытается захватить все возможные варианты, даже те, которые явно
# были получены случайно или был сбой или исключение и поэтому алгоритм
# на мой взгляд не так хорошо, он оверфиттинг (переобучен сильно)

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling # тут можно это убрать, но не особо понял почему
# 120 лекция самое начало, но мы оставляем для графика с шагом 0.01
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

# Fitting the classifire to the Training set
from sklearn.tree import DecisionTreeClassifier
# criterion -  критерий насклько хорошо разбита область?
classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test) # предсказываем данные из X_test

# Making the Confusion Matrix # узнаем насколько правильная модель
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred) # in console cm

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01)) # подготавливаем матрицу поля данных с шагом 0.01
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green'))) # раскрашиваем данные по полотну X1, X2
plt.xlim(X1.min(), X1.max()) # границы для областей указываем?
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)): # все точки рисуем на полотне
  plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
              c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Decision Tree (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend() # в правом верхнем углу рисует соотношение точек и из значений
plt.show()

# Visualising the Test set results (границы одинаковые test = train)
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01)) # подготавливаем матрицу поля данных с шагом 0.01
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green'))) # раскрашиваем данные по полотну X1, X2
plt.xlim(X1.min(), X1.max()) # границы для областей указываем?
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)): # все точки рисуем на полотне
  plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
              c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Decision Tree (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend() # в правом верхнем углу рисует соотношение точек и из значений
plt.show()