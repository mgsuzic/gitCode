#coding: utf-8

from sklearn.datasets import load_digits

#get dataset
digits = load_digits()
print digits.data.shape

#split data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size = 0.25, random_state = 33)

#标准化数据集
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

# model LogigsticRegression
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(X_train, y_train)
lr_y_predict = lr.predict(X_test)

# model SGDClassifier
from sklearn.linear_model import SGDClassifier
sgdc = SGDClassifier()
sgdc.fit(X_train, y_train)
sgdc_y_predict = sgdc.predict(X_test)

#model LinearSVC
from sklearn.svm import LinearSVC
lsvc = LinearSVC()
lsvc.fit(X_train, y_train)
svc_y_predict = lsvc.predict(X_test)

##score
print 'The Accurary of LR Regression is',  str(lr.score(X_test, y_test))
print 'The Accurary of SGDClassifier is',  str(sgdc.score(X_test, y_test))
print 'The Accurary of LinearSVC is',  str(lsvc.score(X_test, y_test))

#更详细的预测
from sklearn.metrics import classification_report
print classification_report(y_test, lr_y_predict, target_names = digits.target_names.astype(str))
print classification_report(y_test, sgdc_y_predict, target_names = digits.target_names.astype(str))
print classification_report(y_test, svc_y_predict, target_names = digits.target_names.astype(str))
