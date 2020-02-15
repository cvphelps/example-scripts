from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wandb
wandb.init(project="vega-sklearn")

# Load data
wine_quality = pd.read_csv("wine.csv")
y = wine_quality["quality"]
X = wine_quality.drop(["quality"], axis = 1)
feature_names=wine_quality.columns
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
labels = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# Train model, get predictions
model = RandomForestClassifier()
model.fit(X, y)
y_pred = model.predict(X_test)
y_probas = model.predict_proba(X_test)
importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

# Visualize model performance
wandb.sklearn.plot_classifier(model, X_train, X_test, y_train, y_test, y_pred, y_probas, labels, False, 'RandomForest', feature_names)
# wandb.sklearn.plot_learning_curve(rf, X_test, y_test)
# wandb.sklearn.plot_class_balance(y_train, y_test)
# wandb.sklearn.plot_calibration_curve(RandomForestClassifier(), X, y, "Random Forest")
# wandb.sklearn.plot_feature_importances(rf)
# wandb.sklearn.plot_summary_metrics(rf, X, y, X_test, y_test)
