from __future__ import division
from __future__ import print_function

import numpy as np

from sklearn import datasets
from sklearn.externals import joblib
from sklearn.neighbors import KNeighborsClassifier


def predict(inputFeatures):
    global knn

    try:
        knn = load_model()
        print('Model loaded succesfully.')
    except:
        iris = datasets.load_iris()
        knn = KNeighborsClassifier()

        knn.fit(iris.data, iris.target_names[iris.target])
        print('New model trained.')

    predictString = knn.predict(inputFeatures.reshape(1, len(inputFeatures)))

    return predictString


def save_model():
    joblib.dump(knn, 'iris_knn.pkl')
    print('model saved.')


def load_model():
    return joblib.load('iris_knn.pkl')
