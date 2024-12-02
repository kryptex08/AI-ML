from sklearn.cluster import KMeans
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt

#load
wine=load_wine()
x=wine.data
y=wine.target

#kmeans
kmeans=KMeans(n_clusters=2,random_state=42)
kmeans.fit(x)

#centroids and lables and score
centroids=kmeans.cluster_centers_
labels=kmeans.labels_

#plot the graph
plt.scatter(x[:,0],x[:,1],c=labels,cmap='viridis',marker='o')
plt.scatter(centroids[:,0],centroids[:,1],c='red',marker='x',label='centroids')
plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()

predictions=labels

cluster_0=np.sum((predictions==0)&(y==1))
cluster_1=np.sum((predictions==1)&(y==0))

if cluster_0>cluster_1:
    predictions=np.where(predictions==0,1,0)

ac=accuracy_score(y,predictions)
print(f"Accuracy:{ac:.2f}")
