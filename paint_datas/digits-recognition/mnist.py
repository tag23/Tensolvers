from sklearn import datasets
from skimage import transform
from sklearn.svm import SVC
from scipy.misc import imread
from scipy.misc import bytescale
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt 
answer = None

while answer != "quit":
    print("Press Enter to continue...")
    input()
    commands = ["1.png","2.png","3.png","4.png","5.png","6.png", "7.png", "8.png", "9.png"]
    for i in commands:
        print(i)
    answer = str(input("Type name of image: "))
    if answer.lower() in commands:
       
       #plt.gray() 
       #plt.matshow(digits.images[6]) 
       #plt.show() 
       digits = datasets.load_digits()
       features = digits.data 
       labels = digits.target
       clf = SVC(gamma=0.0001)
       clf.fit(features, labels)
       
       img = imread(answer)
       #print(f"{img}img = imread(i)")
       img = transform.resize(img, (256,256))
       #print(f"{img}img = transform.resize(img, (8,8))")
       img = img.astype(digits.images.dtype)
       img = transform.resize(img, (8,8))
       #print(f"{img}img = img.astype(digits.images.dtype)")
       img = bytescale(img, high=16, low=0)
       #print(f"{img}img = bytescale(img, high=16, low=0)")
       
       x_test = []
       for eachRow in img:
           for eachPixel in eachRow:
               x_test.append(sum(eachPixel)/3)
       clf.predict([x_test])
       print('\n' * 2)
       print(f"{clf.predict([x_test])} - recognized digit :)")
       print('\n' * 2)
