from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris=load_iris
x=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
gnb=GaussianNB()
gnb.fit(X_train,y_train)
y_test=gnb.predict(X_test)
y_pred=gnb.predict([[5.9,3.0,5.1,1.8]])

pred_species=[iris.target_names[p] for p in y_pred]
print("Predictions:",pred_species)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test,y_pred)

print("Confusion Matrix:\n", cm)
print("Accuracy:", ac)
