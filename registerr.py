import csv
import datetime
import time
import tkinter as tk
from main import main
global key
key = ''
ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }


class RegisterClass:

    def showWindow(self):
        ma = main()

        root = tk.Tk()
        root.geometry('860x540')
        root.title('Registration Page')
        root.configure(background='orange')
        labelTitle = tk.Label(root, text="New Registration", fg='blue', font=('times', 20, 'bold'), bg="#88cffa",
                              pady=10,
                              width=850)
        labelTitle.pack()
        self.frame = tk.LabelFrame(root, text="Fill all the required fields", padx=30, pady=30,
                                   font=('times', 15, 'italic'), fg='#9a1e1e')
        self.frame.pack(pady=40)

        tk.Label(self.frame, text="First Name", font=('times', 13, 'bold')).grid(row=0, column=0)
        self.fNameE = tk.Entry(self.frame, font=('times', 13, 'italic'), width=45,
                               fg='blue')
        self.fNameE.grid(row=0, column=1)

        tk.Label(self.frame, text="Last Name", font=('times', 13, 'bold')).grid(row=1, column=0)
        self.lNameE = tk.Entry(self.frame, textvariable=tk.StringVar(), font=('times', 13, 'italic'), width=45,
                               fg='blue')
        self.lNameE.grid(row=1, column=1)

        tk.Label(self.frame, text="Department", font=('times', 13, 'bold')).grid(row=2, column=0)
        self.departmentE = tk.Entry(self.frame, font=('times', 13, 'italic'), width=45, fg='blue')
        self.departmentE.grid(row=2, column=1)

        # gender frame with radio button widget
        frame_gender = tk.LabelFrame(self.frame, text="Gender ", font=('times', 13, 'bold'), padx=40, pady=5)
        frame_gender.grid(row=3, column=0, columnspan=2)
        # variable to hold the selected of gender
        self.v_g = tk.StringVar(frame_gender, '1')
        options_gender = {"Male": "Male",
                          "Female": "Female", }
        for (text, option) in options_gender.items():
            tk.Radiobutton(frame_gender, text=text, variable=self.v_g, value=option,
                           font=('times', 13, 'italic')).pack(side="left", padx=67)

        # for position frame
        frame_Position = tk.LabelFrame(self.frame, text="Position ", font=('times', 13, 'bold'), padx=5, pady=5)
        frame_Position.grid(row=4, column=0, columnspan=2)
        self.v_p = tk.StringVar(frame_Position, '1')
        options_Position = {"Student": "Student",
                            "Lecture": "Lecture",
                            "Head": "Head",
                            "Dean": "Dean",
                            "Staff": "Staff",
                            "Other": "Other"}
        for (text, option) in options_Position.items():
            tk.Radiobutton(frame_Position, text=text, variable=self.v_p, value=option,
                           font=('times', 13, 'italic')).pack(side="left", padx=4)

        self.buttonTakeCapture = tk.Button(self.root, text=fr'Take images {{self.fNameE.get()}}', font=('times', 13, 'italic'), fg='blue', width='20',
                                           bg="#88cffa",
                                           pady=5, command=ma.TakeImages).grid(row=6, column=0, pady =5, columnspan=2)
        # self.buttonTakeCapture.place(x=30, y=300)

        self.buttonTrain = tk.Button(self.root, text="Train images", font=('times', 13, 'bold italic'), fg='blue', width='50',
                                bg="#88cffa",height=1,
                         activebackground="white",
                                pady=5, command=ma.TrainImages).grid(row=7, column=0,pady=10, columnspan=2)
        # self.buttonTrain.place(x=30, y=360)

        today = datetime.now()
        registrationTime = today.strftime("%d/%m/%Y  %I:%M:%S")
        self.trainer = [self.fNameE.get(), self.lNameE.get(), self.v_g.get(), self.departmentE.get(), self.v_p.get(),
                        registrationTime]

        # row = [serial]
        row1 = self.trainer
        with open('StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row1)
        csvFile.close()


        root.mainloop()

    # def modelTrain(self):
    #     trainer = Trainer()
    #     trainer.startprocess()

        # trainer is the person to be registerd


    # def imputValidate(self,event):
    #     print("imputValidate")
        # if self.fNameE.get()!= "":
        #     print('name != equal')
        #     self.lNameE.config(state = "normal")
        #     if self.fNameE.get()!="":
        #         self.buttonTakeCapture.config(state = "normal")
        #         if str(self.buttonTakeCapture['state']) != 'disabled':
        #             self.buttonTrain.config(state = "normal")
        #         else:
        #             self.buttonTrain.config(state="disabled")
        #     else:
        #         self.buttonTakeCapture.config(state="disabled")
        # else:
        #     self.lNameE.config(state="disabled")
        #     print('name equal')
