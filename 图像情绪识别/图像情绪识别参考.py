import numpy as np 
import cv2 
from sklearn.decomposition import PCA 
from sklearn.ensemble import AdaBoostClassifier
files = open("表情数据/fer2013.csv", "r", encoding="utf-8") 
files_data = files.readlines()[1:]#去掉表头
files_data = [itr.split(",") \
                for itr in files_data]
label = [int(itr[0]) for itr in files_data] 
image = [[float(pix) for pix in itr[1].split(" ")] \
                for itr in files_data] 
label = np.array(label) 
image = np.array(image) 
image -= np.mean(image, axis=0, keepdims=True)
image /= (np.std(image, axis=0, keepdims=True)+1e-6)

pca = PCA(n_components=64)
vect = pca.fit_transform(image)

classifier_method = AdaBoostClassifier() 
classifier_method.fit(vect, label) 

pred_label = classifier_method.predict(vect) 
print("acc", np.sum(pred_label==label)/len(label))