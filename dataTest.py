'''
Reference: https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348
stackoverflow ,and others...
'''

import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# For each person, enter one numeric face id
face_id = input('\n enter user id')
user = input('\n enter user name')
# Initialize individual sampling face count
count = 0

# Parent Directory path2
parent_dir = "F:/New Volume(F)/Programming/lab/python/FaceApp1/Dataset"
# Path
path = os.path.join(parent_dir, user)
# Create the directory
new_path = os.mkdir(path)
print("Directory '% s' created" % user)
print(path)
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

while (True):
    ret, img = cam.read()
    #  img = cv2.flip(img, -1) # flip video image vertically  // why?
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        img_gray = gray[y:y + h, x:x + w]
        # Save the captured image into the datasets folder
        cv2.imwrite(str(path) + '/' + str(face_id) + '_' + str(count) + '.jpg', img_gray)

        cv2.imshow('Taking image', img)
    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 30:  # Take 30 face sample and stop video
        break
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()