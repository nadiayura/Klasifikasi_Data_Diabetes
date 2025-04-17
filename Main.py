# Import necessary libraries 
import numpy as np  
import pandas as pd 
from sklearn.model_selection import train_test_split  
from sklearn.tree import DecisionTreeClassifier 
from sklearn.metrics import accuracy_score, confusion_matrix  
from sklearn import tree 
import matplotlib.pyplot as plt 
 
# Load the dataset from a CSV file 
# Ganti 'path_to_your_file.csv' dengan path file CSV Anda 
df = pd.read_csv('C:/Users/Nadia Ayu R/Downloads/lat/.vscode/data_diabetes.csv', delimiter=';') # 
# Menggunakan delimiter ';' 
 
# Display the first few rows of the dataset 
print(df.head()) 
 
# Memastikan kolom target 
# Anda perlu menyesuaikan nama kolom ini berdasarkan struktur CSV Anda 
X = df.drop(columns='Outcome') # Fitur (semua kolom kecuali target) 
y = df['Outcome'] # Target (kolom target) 
# Split the data into training and testing sets (80% train, 20% test) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
 
# Initialize the Decision Tree Classifier 
classifier = DecisionTreeClassifier(max_depth=3) 
 
# Train the classifier using the training data 
classifier.fit(X_train, y_train) 
 
# Predict the target values for the test set 
y_pred = classifier.predict(X_test) 
 
# Calculate accuracy 
accuracy = accuracy_score(y_test, y_pred) 
print(f"Accuracy: {accuracy * 100:.2f}%") 
 
# Confusion Matrix 
conf_matrix = confusion_matrix(y_test, y_pred) 
print("Confusion Matrix:") 
print(conf_matrix) 
 
# Visualize the Decision Tree 
plt.figure(figsize=(12, 8)) 
tree.plot_tree(classifier, filled=True, feature_names=X.columns, 
class_names=np.unique(y.astype(str))) 
plt.title('Decision Tree Visualization') 
plt.show()