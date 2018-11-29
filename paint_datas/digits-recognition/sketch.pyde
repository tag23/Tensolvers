#import mnist 
import os
dir = os.listdir(r'C:\Users\Admin\sketch')
os.system(r'python mnist.py')
with open('prediction.txt', 'r') as f:
    prediction = f.read()
print(prediction)
print(dir)
