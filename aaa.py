'''
Reference: https://towardsdatascience.com/real-time-face-recognition-an-end-to-end-project-b738bb0f7348
stackoverflow ,and others...
'''

import cv2
cam = cv2.VideoCapture(0)
# cam.set(3, 640)  # set video width
# cam.set(4, 480)  # set video height
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")

while (True):
    ret, img = cam.read()
    cv2.imshow('Taking image', img)
    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    if k == 27:
        break
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()