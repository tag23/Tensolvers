from sklearn import datasets
from skimage import transform
from sklearn.svm import SVC
from scipy.misc import imread
from scipy.misc import bytescale
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt 

path = "data/"
def save_data(data):
    with open(path+"data.txt", "w") as f:
        f.write(str(data))
    f.close()

#commands = ["1.png","2.png","3.png","4.png", "9.png", "5.png", "6.png", "7.png", "8.png"]
def main(image):
    #global path
    #a = 0
    #stop = False
    #while not stop:
        #if a < len(commands):
           #for n, i in enumerate(commands):
               #i = path + i

    digits = datasets.load_digits()

    n_samples = len(digits.images)

    #features = digits.data
    features = digits.images.reshape((n_samples, -1))
    labels = digits.target
    clf = SVC(gamma=0.0001, C=100)
    clf.fit(features[:n_samples], labels[:n_samples])
               
    img = imread(image)
            #print(f"{img}img = imread(i)")
    img = transform.resize(img, (8, 8))
            #print(f"{img}img = transform.resize(img, (8,8))")
    img = img.astype(digits.images.dtype)
            #img = transform.resize(img, (8,8))
            #print(f"{img}img = img.astype(digits.images.dtype)")
    img = bytescale(img, high=16, low=0)
    imshow(img)
            #print(f"{img}img = bytescale(img, high=16, low=0)")
               
    x_test = []
    for eachRow in img:
        for eachPixel in eachRow:
            x_test.append(sum(eachPixel)/3)
    clf.predict([x_test])
            #print('\n' * 2)
            #print(f"{clf.predict([x_test])} - recognized digit :)")
            #print('\n' * 2)
            #a += 1
    save_data(clf.predict([x_test]))#

    #    else:
    #        stop = True
