from sklearn import datasets
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
iris=datasets.load_iris()
features=iris.data
labels=iris.target
features_tain,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.5)
print(features_tain.shape)
#my_classfier = KNeighborsClassifier()
#my_classfier.fit(features_tain,labels_train)
#prediction=my_classfier.predict(features_test)
#print(accuracy_score(labels_test,prediction))



