from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

#sample data[height(cm),weight(cm)]
X=np.vstack([
    np.random.normal(loc=[2, 2], scale=0.5, size=(100, 2)),
    np.random.normal(loc=[8, 8], scale=0.5, size=(100, 2)),
    np.random.normal(loc=[5, 2], scale=0.5, size=(100, 2))
])
kmeans=KMeans(n_clusters=3,random_state=42)
kmeans.fit(X)

centroids=kmeans.cluster_centers_
labels=kmeans.labels_

print("Cluster centroids:",centroids)
print("Label for each point:",labels)

plt.scatter(X[:,0],X[:,1],c=labels,cmap="viridis",marker='o',label='Data Points')
plt.scatter(centroids[:,0],centroids[:,1],c='red',marker='x',s=100,label='Centroids')
plt.xlabel('Height(cm)')
plt.ylabel('Weight(kg)')
plt.title('K-means Clustering')
plt.legend()
plt.show()