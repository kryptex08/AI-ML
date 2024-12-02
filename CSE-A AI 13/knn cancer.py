import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score

#load dataset into cancer variable
cancer=load_breast_cancer()
X=cancer.data
y=cancer.target

#use only 1st 2 features
X=X[:,:2]

#split the dataset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

#knn
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)

#evaluate the model
y_pred_test=knn.predict(X_test)
ac=accuracy_score(y_test,y_pred_test)
print(f"Accuracy:{ac:.2f}")

xx,yy=np.meshgrid(
    (X[:,0].min()-1,X[:,0].max()+1,0.1),
    (X[:,1].min()-1,X[:,1].max()+1,0.1)
)
Z=knn.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)

plt.contourf(xx,yy,Z,cmap='coolwarm',alpha=0.3)
plt.scatter(X_train[:,0],X_train[:,1],c=y_train,marker='o',alpha=0.5,label='Training Data')
plt.scatter(X_test[:,0],X_test[:,1],color='red',marker='x',label='Testing Data')
plt.title('KNN Breast Cancer')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.grid()
plt.show()
