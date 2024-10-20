from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix, accuracy_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred_test = gnb.predict(X_test)

single_pred = gnb.predict([[5.9, 3.0, 5.1, 1.8]])

pred_species = [iris.target_names[p] for p in single_pred]
print("Prediction for sample [[5.9, 3.0, 5.1, 1.8]]:", pred_species)

cm = confusion_matrix(y_test, y_pred_test)
print("Confusion Matrix:\n", cm)

ac = accuracy_score(y_test, y_pred_test)
print("Accuracy Score:", ac)
