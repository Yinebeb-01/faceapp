import tkinter as tk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2, os
import csv
import numpy as np
import pandas as pd
import datetime
import time
from registerr import RegisterClass
from gui import  maingui
from tkinter import filedialog

# import for Raspberry PI for the door.

# import RPi.GPIO as GPIO
# from time import sleep

# relay_pin = [26]
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(relay_pin, GPIO.OUT)
# GPIO.output(relay_pin, 0)
class main:

    path = 'F:/New Volume(F)/Programming/lab/python/FaceApp1/Dataset'
    ### FUNCTIONS ###

    def assure_path_exists(path):
        dir = os.path.dirname(path)
        if not os.path.exists(dir):
            os.makedirs(dir)

    # def clear():
    #     cl = RegisterClass()
    #     cg = maingui()
    #     cl.fNameE.delete(0, 'end')
    #     res = "1)Take Images       2)Save Profile"
    #     cg.message3.configure(text=res)

    def contact(self):
        mess._show(title='Contact us', message="Please contact us on : 'info@hulu.com' ")


    def save_pass(self):
        self.assure_path_exists("Trainer/")
        exists1 = os.path.isfile("Trainer/psd.txt")
        if exists1:
            tf = open("Trainer/psd.txt", "r")
            key = tf.read()
        else:
            master.destroy()
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open("Trainer/psd.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        op = (old.get())
        newp = (new.get())
        nnewp = (nnew.get())
        if (op == key):
            if (newp == nnewp):
                txf = open("Trainer/psd.txt", "w")
                txf.write(newp)
            else:
                mess._show(title='Error', message='Confirm new password again!!!')
                return
        else:
            mess._show(title='Wrong Password', message='Please enter correct old password.')
            return
        mess._show(title='Password Changed', message='Password changed successfully!!')
        master.destroy()


    def change_pass(self):
        global master
        master = tk.Tk()
        master.geometry("400x160")
        master.resizable(False, False)
        master.title("Change Password")
        master.configure(background="white")
        lbl4 = tk.Label(master, text='    Enter Old Password', bg='white', font=('times', 12, ' bold '))
        lbl4.place(x=10, y=10)
        global old
        old = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        old.place(x=180, y=10)
        lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('times', 12, ' bold '))
        lbl5.place(x=10, y=45)
        global new
        new = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        new.place(x=180, y=45)
        lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('times', 12, ' bold '))
        lbl6.place(x=10, y=80)
        global nnew
        nnew = tk.Entry(master, width=25, fg="black", relief='solid', font=('times', 12, ' bold '), show='*')
        nnew.place(x=180, y=80)
        cancel = tk.Button(master, text="Cancel", command=master.destroy, fg="black", bg="red", height=1, width=25,
                           activebackground="white", font=('times', 10, ' bold '))
        cancel.place(x=200, y=120)
        save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height=1, width=25,
                          activebackground="white", font=('times', 10, ' bold '))
        save1.place(x=10, y=120)
        master.mainloop()


    def psw(self):
        self.assure_path_exists("Trainer/")
        exists1 = os.path.isfile("TrainingImageLabel/psd.txt")
        if exists1:
            tf = open("Trainer/psd.txt", "r")
            key = tf.read()
        else:
            new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
            if new_pas == None:
                mess._show(title='No Password Entered', message='Password not set!! Please try again')
            else:
                tf = open("Trainer/psd.txt", "w")
                tf.write(new_pas)
                mess._show(title='Password Registered', message='New password was registered successfully!!')
                return
        password = tsd.askstring('Password', 'Enter Password', show='*')
        if (password == key):
            self.TrainImages()
        elif (password == None):
            pass
        else:
            mess._show(title='Wrong Password', message='You have entered wrong password')


    # def clear2():
    #     txt2.delete(0, 'end')
    #     res = "1)Take Images      2)Save Profile"
    #     message1.configure(text=res)


    def TakeImages(self):
        cg =maingui()
        cl =RegisterClass()
        columns = ['SERIAL NO.', '', 'ID', '', 'User_Name']
        self.assure_path_exists("StudentDetails/")
        self.assure_path_exists("Dataset/")
        serial = 0
        exists = os.path.isfile("StudentDetails/StudentDetails.csv")
        if exists:
            with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    serial = serial + 1
            serial = (serial // 2)  # since the student file jumps one line per entry,...
            csvFile1.close()
        else:
            with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(columns)
                serial = 1
            csvFile1.close()
        Id = serial
        name = (cl.fNameE.get())
        if ((name.isalpha()) or (' ' in name)):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0

            # Parent Directory path
            parent_dir = "F:/New Volume(F)/Programming/lab/python/FaceApp1/Dataset/"
            path = os.path.join(parent_dir, name)
            # Create the directory
            new_path = os.mkdir(path)
            print("Directory '% s' created" % name)
            print(path)
            print("\n [INFO] Initializing face capture. Look the camera ; try to reflect all smells, and wait ...")

            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    # incrementing sample number
                    sampleNum = sampleNum + 1
                    img_gray = gray[y:y + h, x:x + w]
                    # saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite(str(path) + '/' + Id + '_' + str(sampleNum) + '.jpg', img_gray)
                    # display the frame
                    cv2.imshow('Taking Images', img)
                # wait for 100 miliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                # break if the sample number is morethan 100
                elif sampleNum > 60:
                    break
            cam.release()
            cv2.destroyAllWindows()
            res = "Images Taken for ID : " + Id
            # row = [serial]
            # row1 =row.append(cl.trainer)
            # with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            #     writer = csv.writer(csvFile)
            #     writer.writerow(row1)
            # csvFile.close()
            cg.message.configure(text=res)
        else:
            if (name.isalpha() == False):
                res = "Enter Correct name"
                cg.message.configure(text=res)


    ###################################################


    def getImagesAndLabels(path):
        imagePath = []
        detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faceSamples = []
        ids = []
        for dirname, dirnames, filenames in os.walk(path):
            for filename in filenames:
                imagePath.append(os.path.join(dirname,
                                              filename))  # append all the images path, upto the .jpg by trackiing from the dataset into one array called image path
        for imagePaths in imagePath:

            image = cv2.imread(imagePaths)
            PIL_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # PIL_img = Image.open(imagePaths).convert('L')  # grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePaths)[-1].split("_")[
                         0])  # id = int(os.path.split(imagePath)[-1].split(".")[0])  ; this gives 111,112 and the like
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])
                ids.append(id)
        return faceSamples, ids


    ########################np


    def TrainImages(self):
        cg =maingui()
        self.assure_path_exists("Trainer/")  # trianer
        recognizer = cv2.face_LBPHFaceRecognizer.create()
        faces, ids = self.getImagesAndLabels(self.path)
        try:
            recognizer.train(faces,
                             np.array(ids))  # this generate a training - the trained file , that going to be saved as .yml
        except:
            mess._show(title='No Registrations', message='Please Register someone first!!!')
            return
        recognizer.write("Trainer/Trainer.yml")

        res = "Trianed Successfully"
        cg.message3.configure(text=res)
        cg.message.configure(text='Total Registrations till now  : ' + str(ids[0] + 1))
        # out of ids array,, the last which s place in the begining is hte last user and since start from 0 we add 1/.

    ###########################################
    def TrackImages(self):
        cg =maingui()
        self.assure_path_exists("Attendance/")
        self.assure_path_exists("StudentDetails/")
        for k in cg.tree.get_children():
            cg.tree.delete(k)
        msg = ''
        i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        exists3 = os.path.isfile("Trainer/Trainer.yml")
        if exists3:
            recognizer.read("Trainer/Trainer.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', '', 'Name', '', 'Date', '', 'Time']
        exists1 = os.path.isfile("StudentDetails/StudentDetails.csv")
        if exists1:
            df = pd.read_csv("StudentDetails/StudentDetails.csv")
            print(df)  # for test
        else:
            mess._show(title='Details Missing', message='Students details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
            # window.destroy()
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h,
                                                  x:x + w])  # regarding to the imported trianer .yml; this predict teh ID by taking images as input.
                print(serial)
                if (conf < 100):  # <50 ?
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SERIAL NO.'] == serial]['Name'].values  # df = pd.read_csv("StudentDetails/StudentDetails.csv")
                    # hence aa is the name of the corresponding serial no. where the predicted serial number matches.
                    # print(aa)    # fortest
                    # ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                    ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values

                    print(ID)
                    # why this return ID with decimal point like [1.]?
                    ID = str(ID)
                    print(ID)
                    aa = str(aa)  # to parse below this line may necessary..?
                    # ID is the ID of the corresponding serial no. where the predicted serial number matches.
                    ID = ID[1:-2]
                    print(ID)
                    aa = aa[2:-2]  # taking the name only by removing [' xxx'] = xxx
                    attendance = [str(ID), '', aa, '', str(date), '', str(timeStamp)]
                    # open the door if the user is a known .
                # GPIO.output(relay_pin, 1)

                else:
                    aa = 'Unknown'
                    # leave the door close if the user is unknown.
                    # GPIO.output(relay_pin, 1)

                cv2.putText(im, str(aa), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('Taking Attendance', im)
            if (cv2.waitKey(1) == ord('q')):  # the attendance will taken at the time of q press.
                break

        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
        exists = os.path.isfile("Attendance/Attendance_" + date + ".csv")
        if exists:
            with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(attendance)
            csvFile1.close()
        else:
            with open("Attendance/Attendance_" + date + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        with open("Attendance/Attendance_" + date + ".csv", 'r') as csvFile1:
            reader1 = csv.reader(csvFile1)
            for lines in reader1:
                i = i + 1
                if (i > 1):
                    if (i % 2 != 0):
                        iidd = str(lines[0]) + '   '
                        cg.tree.insert('', 0, text=iidd, values=(str(lines[2]), str(lines[4]), str(lines[6])))
        csvFile1.close()
        cam.release()
        cv2.destroyAllWindows()
