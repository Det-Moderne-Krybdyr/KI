# Decision Tree Classification

# Importing the libraries
import numpy as np
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
#import os  
#path = os.getcwd() 
#os.chdir(path)
 

# Importing the dataset 
dataset = pd.read_csv('./adult_income.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#encode categorial data for y
le = LabelEncoder()
y = le.fit_transform(y)

#encode categorial data for x
categorial_columns = [2,4,5,6,7,11]

ct = ColumnTransformer(
    transformers=[
        ('onehot',OneHotEncoder(),categorial_columns)
    ],
    remainder='passthrough'
)

x_trans = ct.fit_transform(X)

# TODO: Visualize each feature and observe the plots to better understand 
# Write code scripts to plot the figures
#df = pd.DataFrame(dataset)
#sns.pairplot(df,hue="Purchased")
#plt.show()

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(x_trans, y, test_size = 0.20, random_state = 0) # 80% train, 20% test
 

# Training the Decision Tree Classification model on the Training set
classifier = DecisionTreeClassifier(criterion = 'entropy',max_depth=3,min_samples_leaf=5, random_state = 0) # Use 'gini' for Gini impurity
classifier.fit(X_train, y_train)


# Predicting the Test set results
y_pred = classifier.predict(X_test)


#  Evaluate the model by making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred) 
print(f"Confusion Matrix: \n {cm}")
 
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
 

# Visualize the decision tree  
plt.figure(figsize=(25,20))
tree.plot_tree(classifier, class_names=['no', 'yes'],  filled=True, rounded=True)
plt.show()


# Predicting a new result
#new_data=[[30,87000]]
#prediction = classifier.predict(new_data)
#print(f"Prediction for new data: {prediction}")
 
# TODO: Observe the plotted tree to see if it is too complex or not
# write a code check whether or not there is an overfitting
# if the model is overfitting, fix the overfitting and show the plot results for before and after
# overfitting can be fixed be adding params max_depth=3,min_samples_leaf=5 to DecisionTreeClassifier which makes test accuracy closer to training accuracy
# changed from Training Accuracy: 0.996875 and Test Accuracy: 0.9 to Training Accuracy: 0.909375 and Test Accuracy: 0.95 for the data set
train_pred = classifier.predict(X_train)
train_acc = accuracy_score(y_train, train_pred)
test_acc = accuracy_score(y_test, y_pred)

print(f"Training Accuracy: {train_acc}")
print(f"Test Accuracy: {test_acc}")