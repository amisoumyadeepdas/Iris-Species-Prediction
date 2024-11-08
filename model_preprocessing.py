'''
Let's train a simple model related to Iris dataset using sklearn
'''

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

#load dataset

data = load_iris()
X,y=data.data,data.target

#train the model

model = RandomForestClassifier()
model.fit(X,y)
joblib.dump(model,'irisTest.joblib')

