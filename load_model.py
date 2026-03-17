import pickle
import numpy as np
import sklearn
from sklearn.datasets import load_iris
with open('model_iris.pkl_v1', 'rb') as f:
    model = pickle.load(f)
test=np.array([[5.1, 3.5, 1.4, 0.2]])
wynik_testu= model.predict(test)
nazwy = ['setosa', 'versicolor', 'virginica']
nazwa_pred = nazwy[wynik_testu[0]]
print(f"dla kwiata o parametrach {test} model wskazał {nazwa_pred}")
