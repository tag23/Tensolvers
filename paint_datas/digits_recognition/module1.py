# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 17:41:23 2018

@author: Admin
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
digits = datasets.load_digits()
clf = svm.SVC(gamma=0.0001, C=1)
print(len(digits.data))
x,y = digits.data, digits.target
clf.fit(x,y)

print('Prediction: {}'.format(clf.predict([digits.data[14]])))
plt.imshow(digits.images[14], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()