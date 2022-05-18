from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

# from DataBase import Database
# from RegisterWin import RegisterClass
# from facial_req import FaceRecognitionClass
import main

class MasterClass:

    def showMain(self):
        self.mainWindow = Tk()

        self.tree = ttk.Treeview(self.mainWindow, column=("rollNumber","id", "fname", "lname","gender","department",
                                                          "position","gate","date", "time","pic"),
                                 show="headings",
                                 height=30)
        self.tree.heading('rollNumber', text="#")
        self.tree.heading('id', text="ID")
        self.tree.heading('fname', text="First Name")
        self.tree.heading('lname', text="Last Name")
        self.tree.heading('gender', text="Gender")
        self.tree.heading('department', text="Department")
        self.tree.heading('position', text="Position")
        self.tree.heading('gate', text="Gate Number")
        self.tree.heading('date', text="Date")
        self.tree.heading('time', text="Time")
        self.tree.heading('pic', text="Pic at the entry")

        self.tree.column('rollNumber', width=15)
        self.tree.column('id', width=15)
        self.tree.column('fname', width=75)
        self.tree.column('lname', width=75)
        self.tree.column('gender', width=50)
        self.tree.column('gate', width=35)
        self.tree.column('department', width=60)
        self.tree.column('date', width=75)
        self.tree.column('position', width=75)
        self.tree.column('time', width=75)
        self.tree.column('pic', width=330)

        width = self.mainWindow.winfo_screenwidth()
        height = self.mainWindow.winfo_screenheight()
        self.mainWindow.geometry("%dx%d" % (width, height))
        self.mainWindow.title("AASTU -->Main window")
        style = ttk.Style()
        style.theme_use('winnative')
        label = Label(self.mainWindow,
                      text="Addis Ababa Science and Technology University Facial recognition based gate opening system",
                      font=('times', 20, 'bold'),fg ='blue',bg="#88cffa", pady=13)
        label.grid(row=0, column=0, columnspan=4, sticky='nsew')
        label = Label(self.mainWindow,
                      font=('times', 20, 'bold'), fg='blue', bg="#81cffa", pady=8)
        label.grid(row=10, column=0, columnspan=4, sticky='nsew')

#===================push button===========================================================
        openDor =Button(self.mainWindow,text = "Open Door",
                      font=('times', 15, 'bold'), fg='blue', bg="gray", pady=5,command=self.startFaceRecognition)
        openDor.grid(row=10, column=0, columnspan=2)
#=======================================================================================
        requiestButton = Button(self.mainWindow, text="Ask a request",
                         font=('times', 15, 'bold'), fg='blue', bg="gray", pady=5)
        requiestButton.grid(row=10, column=1, columnspan=2)

# ===================push button==============================
        buttonFrame = LabelFrame(self.mainWindow, fg='blue', text="For only the admins", padx=20, pady=20,
                                 font=('times', 15, 'bold'))
        buttonFrame.grid(row=1, column=0)

        Button(buttonFrame, text="New Registration", font=('times', 13, 'bold italic'), fg='blue',
                             width='15', bg="#88cffa",command = self.register,
                             pady=5 ).pack(pady = 5)

        Button(buttonFrame, text="Total List", font=('times', 13, 'bold italic'), fg='blue',
                         width='15', bg="#88cffa", command=self.registerList,
                         pady=5).pack(pady=5)

        Button(buttonFrame, text="Remove", font=('times', 13, 'bold italic'), fg='blue',
                         width='15', bg="#88cffa", command=self.remove,
                         pady=5).pack(pady=5)

        # ===============================button frame===============================
        # # lis of today entry
        # db = Database()
        # registerdPersons =db.getReportTable()
        # for person in registerdPersons:
        #     self.tree.insert('',0, values=person)
        # add scrollbar to the tablez
        scrollbar = ttk.Scrollbar(self.mainWindow, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky='ns')
        self.tree.grid(row=1, column=1, sticky='nsew')

        self.mainWindow.mainloop()

    def startFaceRecognition(self):
        # instance of the recognizer class
        faceDetection  = FaceRecognitionClass()
        name ='Unknown'
        for i in range(10):
            name = faceDetection.startRecognition()
            if name != 'Unknown':
                print('returned name ====', name)
                break
        if name != 'Unknown':
            db = Database()
            db.insertReportTable(name)
            registerdPerson = db.getReportOf(name)
            #to remove the initial value of table to avoid redendency
            for row in self.tree.get_children():
                self.tree.delete(row)

            for person in registerdPerson:
                self.tree.insert('',0, values=person)
        self.mainWindow.update_idletasks()

    def register(self):
        registerWindow = RegisterClass()
        registerWindow.showWindow()
    def registerList(self):
        lilst = Database()
        lilst.showRegisterdPersonsList()
        root = Tk()
        root.geometry('950x560')
        root.title('Removing...')
        labelTitle = Label(root, text="New Registration", fg='blue', font=('times', 25, 'bold'), bg="#88cffa",
                              pady=10,
                              width=850)
        labelTitle.pack()
        self.buttonTrain = Button(self.frame, text="Train", font=('times', 13, 'bold italic'), fg='blue', width='50',
                                     bg="#88cffa",
                                     pady=5, command=train_model).pack()
        root.mainloop()
    def remove(self):
        lilst = Database()
        lilst.removeRegisterdPerson(2)


test = MasterClass()
test.showMain()

