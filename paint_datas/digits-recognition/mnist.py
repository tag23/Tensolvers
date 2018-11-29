from sklearn import datasets
from skimage import transform
from sklearn.svm import SVC
from scipy.misc import imread
from scipy.misc import bytescale
from matplotlib.pyplot import imshow
from sklearn.datasets import load_digits
digits = load_digits()
print(digits.data.shape)

import matplotlib.pyplot as plt 
plt.gray() 
plt.matshow(digits.images[8]) 
plt.show() 
try:
    digits = datasets.load_digits()
    features = digits.data 
    labels = digits.target
    
    clf = SVC(gamma=0.0001)
    clf.fit(features, labels)
    img = None
    images = ["1.png","2.png","3.png","4.png","5.png","6.png", "7.png", "8.png", "9.png"]
    #images = ["8.png"]
    result = []
    for i in images:
        img = imread(i)
        
        #img = np.invert(img)
        #print(f"{img}img = imread(i)")
        img = transform.resize(img, (256,256))
        #print(f"{img}img = transform.resize(img, (8,8))")
        
        img = img.astype(digits.images.dtype)
        #print(f"{img}img = img.astype(digits.images.dtype)")
        imshow(img)
        img = transform.resize(img, (8,8))
        img = bytescale(img, high=16, low=0)
        
        #print(f"{img}img = bytescale(img, high=16, low=0)")

        x_test = []
        for eachRow in img:
        	for eachPixel in eachRow:
        		x_test.append(sum(eachPixel)/3)
        clf.predict([x_test])
        
        print(f"{clf.predict([x_test])} - {i}")
    
    print([i for i in list(result)])
except Exception as e:
    print(e)