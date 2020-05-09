# -*- coding: utf-8 -*-
"""DIscoverWine.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13T8JHu4ivgL4n2CQgi2drEpTveR-y4mh

# Discover Data
Now we try to study the Wine dataset from Professor Sartori.
Firstly try the classification mode with:
1.   Decisione Tree
2.   Support Vector
3.   Linear Perceptron
4.   Gaussian Naive Bayes

After that part, try the clustering mode with:
1.   KMeans
2.   DBSCAN

Start!
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples, accuracy_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import ParameterGrid
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.svm import SVC

# %matplotlib inline

rnd_state = 42 # This variable will be used in all the procedure calls allowing a random_state parameter
               # in this way the running can be perfectly reproduced
               # just change this value for a different experiment

# the .py files with the functions provided must be in the same directory of the .ipynb file
from plot_clusters import plot_clusters      # python script provided separately
from plot_silhouette import plot_silhouette  # python script provided separately

"""# Starting 
* load the csv and create the DataFrame
* show head
* show shape
"""

#txt = np.loadtxt('winequality-red.csv', delimiter=';')
#df = pd.DataFrame(txt)

df = pd.read_csv('winequality-red.csv', sep=';')

dataset = datasets.load_wine()
X = dataset.data
Y = dataset.target

df.head()

"""# Prepare data
* Divide the feature we want to predict with algorithm to create a variable X and Y
* Create the train and test datasets.
"""

#X = df.drop(['quality'],axis=1)
#X.head()

xtrain, xtest, ytrain, ytest = train_test_split(X, Y, test_size=0.3, random_state=42)

"""# Learning Classification
Start instantiate the classifier and fit to the data
"""

class1 = DecisionTreeClassifier(criterion='entropy')
class1.fit(xtrain, ytrain)
predt1 = class1.predict(xtrain)
print(" The accuracy score for Decision Tree over train dataset is " + str(accuracy_score(ytrain, predt1)*100) + "%")
predte1 = class1.predict(xtest)
print(" The accuracy score for Decision Tree over test dataset is " + str(accuracy_score(ytest, predte1)*100) + "%")

class2 = GaussianNB()
class2.fit(xtrain, ytrain)
predt2 = class2.predict(xtrain)
print(" The accuracy score for Gaussian Naive Bayes over train dataset is " + str(accuracy_score(ytrain, predt2)*100) + "%")
predte2 = class2.predict(xtest)
print(" The accuracy score for Gaussian Naive Bayes over test dataset is " + str(accuracy_score(ytest, predte2)*100) + "%")

class2 = Perceptron()
class2.fit(xtrain, ytrain)
predt2 = class2.predict(xtrain)
print(" The accuracy score for Linear Perceptron over train dataset is " + str(accuracy_score(ytrain, predt2)*100) + "%")
predte2 = class2.predict(xtest)
print(" The accuracy score for Linear Perceptron over test dataset is " + str(accuracy_score(ytest, predte2)*100) + "%")

class2 = SVC()
class2.fit(xtrain, ytrain)
predt2 = class2.predict(xtrain)
print(" The accuracy score for Support Vector over train dataset is " + str(accuracy_score(ytrain, predt2)*100) + "%")
predte2 = class2.predict(xtest)
print(" The accuracy score for Support Vector over test dataset is " + str(accuracy_score(ytest, predte2)*100) + "%")

"""# Clusterization Mode
* Study the data
* Find best feature
* Execute KMeans and DBSCAN algorithm.
"""

sns.pairplot(pd.DataFrame(X))

focus = [11,5]
plt.scatter(X[:,focus[0]], X[:,focus[1]]
            , c='white'          # color filling the data markers
            , edgecolors='black' # edge color for data markers
            , marker='o'         # data marker shape, e.g. triangles (v<>^), square (s), star (*), ...
            , s=50)              # data marker size
plt.grid()  # plots a grid on the data
plt.show()

nclus = 2
kms = KMeans(n_clusters=nclus)
y_km = kms.fit_predict(X)
plot_clusters(X,y_km,dim=(focus[0],focus[1]), points = kms.cluster_centers_)

db = DBSCAN(eps=0.15, min_samples=9)
y_db = db.fit_predict(X)
cluster_labels_all = np.unique(y_db)
cluster_labels = cluster_labels_all[cluster_labels_all != -1]
n_clusters = len(cluster_labels)
cluster_centers = np.empty((n_clusters,X.shape[1])) 
for i in cluster_labels:
    cluster_centers[i,:] = np.mean(X[y_db==i,:], axis = 0)
plot_clusters(X,y_db,dim=(focus[0],focus[1]), points = cluster_centers)