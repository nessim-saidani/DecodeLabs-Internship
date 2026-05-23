import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix



df=pd.read_csv('Iris.csv')
x=df.drop('Species',axis=1)
y=df['Species']


print(df.head)
print(df.shape)
print(df.describe)
print(df.info())


#split the test part
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)



#classification
# 1 KNN Algorithm
modal=KNeighborsClassifier(n_neighbors=3)
modal.fit(x_train,y_train)


#testing 
y_pred=modal.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print ("Accuracy : " , accuracy)
print (classification_report(y_test,y_pred))
print(confusion_matrix(y_test, y_pred))
