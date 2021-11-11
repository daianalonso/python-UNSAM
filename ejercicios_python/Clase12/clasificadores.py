from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np

iris_dataset = load_iris()
#%%Ejercicio 12.12
clf_scores = np.zeros(100)
knn_scores = np.zeros(100)
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'])
    knn = KNeighborsClassifier(n_neighbors = 1)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    knn_scores[i] = knn.score(X_test, y_test)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    pred = clf.predict(X_test)
    clf_scores[i] = clf.score(X_test, y_test)

clf_mean = clf_scores.mean()
knn_mean = knn_scores.mean()
print("Promedio de evaluación de scores:")
print("Arboles de decisión: {:.4f},".format(clf_mean), "Vecinos más cercanos: {:.4f}".format(knn_mean))
