import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Generate dataset
X, y = make_classification(n_samples=300, n_features=2, n_informative=2, n_redundant=0,n_clusters_per_class=1,random_state=42)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Evaluate model
accuracy = accuracy_score(y_test, knn.predict(X_test))
print(f"Accuracy: {accuracy:.2f}")

# Plot decision boundary and data
xx, yy = np.meshgrid(
    np.arange(X[:, 0].min() - 1, X[:, 0].max() + 1, 0.1),
    np.arange(X[:, 1].min() - 1, X[:, 1].max() + 1, 0.1)
)
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, alpha=0.5, label='Training Data')
plt.scatter(X_test[:, 0], X_test[:, 1], color='red', label='Testing Data', marker='x')
plt.title('K-Nearest Neighbors')
plt.xlabel('Feauture 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()
