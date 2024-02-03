#!/usr/bin/env python
# coding: utf-8

# In[4]:
#Day30

# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Generate a fictional dataset
np.random.seed(42)
study_hours = np.random.uniform(1, 10, 100)
sleep_hours = np.random.uniform(4, 12, 100)
pass_fail = np.where((study_hours > 5) & (sleep_hours > 6), 1, 0)

# Create a feature matrix X and target variable y
X = np.column_stack((study_hours, sleep_hours))
y = pass_fail

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create KNN classifier with k=5
knn_classifier = KNeighborsClassifier(n_neighbors=5)

# Train the classifier
knn_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn_classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Display classification report
print("Classification Report:\n", classification_report(y_test, y_pred))


# In[ ]:




