import cv2
import numpy as np
from PIL import Image
import os
# Path for face image database
path = 'F:/New Volume(F)/Programming/lab/python/FaceApp1/Dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
# function to get the images and label data
imagePath=[]
def getImagesAndLabels(path):
    faceSamples=[]
    ids = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            imagePath.append(os.path.join(dirname, filename))
#     print(imagePath)

#     imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    for imagePaths in imagePath:
        PIL_img = Image.open(imagePaths).convert('L') # grayscale
        img_numpy = np.array(PIL_img,'uint8')
#         print(imagePaths)
        id = int(os.path.split(imagePaths)[-1].split("_")[0])   # id = int(os.path.split(imagePath)[-1].split(".")[0])  ; this gives 111,112 and the like
#         print(id)
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids
print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
# Save the model into trainer/trainer.yml
recognizer.write('Trainer/tr.yml')
# Print the numer of faces trained and end program
print(ids)
print("\n [INFO] {0} faces trained. Exiting Program".format(len(ids))) #len(np.unique(ids)