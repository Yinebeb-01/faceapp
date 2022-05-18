### GUI FRONT-END ###

from tkinter import *
from tkinter import ttk
import time as t
from datetime import *
import os, csv
import time

from registerr import RegisterClass
from main import main

global key
key = ''
ts = t.time()
date = datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")
mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }


class maingui():

    # def tick(self):
    #     time_string = time.strftime('%H:%M:%S')
    #     clock.config(text=time_string)
    #     clock.after(200, self.tick)

    def main(self):
        ma = main()
        rg = RegisterClass()

        window = Tk()
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))
        # window.geometry("1280x720")
        window.resizable(True, False)

        p1 = PhotoImage(file='aastu.png')
        # Setting icon of master window
        window.iconphoto(False, p1)

        style = ttk.Style()
        style.theme_use('winnative')

        window.title("CV Based Attendance System")
        window.configure(background='#262523')

        frame1 = Frame(window, bg="#00aeff")
        frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

        frame2 = Frame(window, bg="#00aeff")
        frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

        message = Label(frame2, text="", bg="#00aeff", fg="black", width=39, height=1, activebackground="yellow",
                           font=('times', 16, ' bold '))
        message.place(x=7, y=470)
        message3 = Label(window, text="Face Recognition Based Attendance System", fg="blue", width=55,
                         height=1, font=('times', 29, ' bold '), bg="#88cffa", pady=10)
        message3.place(x=10, y=10)

        # Admin LabelFrame
        buttonFrame = LabelFrame(window, fg='orange', text="*For Admins*", padx=15, pady=15,
                                 font=('times', 15, 'bold'))
        buttonFrame.grid(row=1, column=0)

        Button(buttonFrame, text="New Registration", font=('times', 13, 'bold italic'), fg='blue',
               width='15', bg="#88cffa", command=rg.showWindow(),
               pady=5).pack(pady=5)
        # Button(buttonFrame, text="Total List", font=('times', 13, 'bold italic'), fg='blue',
        #        width='15', bg="#88cffa", command=registerList,
        #        pady=5).pack(pady=5)

        # Date LabelFrame
        frame3 = LabelFrame(window, bg="#c4c6ce")
        frame3.place(relx=0.62, rely=0.09, relwidth=0.09, relheight=0.07)
        datef = Label(frame3, text=day + "-" + mont[month] + "-" + year + "  |  ", fg="orange", bg="#262523", width=50,
                      height=1, font=('times', 18, ' bold '))
        datef.pack(fill='both', expand=1)
        bb = Label(frame3, fg="orange", bg="#262523", width=35, height=1, font=('times', 18, ' bold '))
        bb.pack(fill='both', expand=1)

        clock = Label(frame3, fg="orange", bg="#262523", width=55, height=1, font=('times', 22, ' bold '))
        clock.pack(fill='both', expand=1)
        time_string = time.strftime('%H:%M:%S')
        clock.config(text=time_string)
        # clock.after(200, self.tick)
        # # self.tick()

        lbl3 = Label(window, text="Attendance", width=20, fg="black", bg="#00aeff", height=1, font=('times', 17, ' bold '))
        lbl3.place(x=100, y=115)

        res = 0
        exists = os.path.isfile("StudentDetails/StudentDetails.csv")
        if exists:
            with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
                reader1 = csv.reader(csvFile1)
                for l in reader1:
                    res = res + 1
            res = (res // 2) - 1
            csvFile1.close()
        else:
            res = 0
        message.configure(text='Total Registrations till now  : ' + str(res))

        ##################### MENUBAR #################################

        menubar = Menu(window, relief='ridge')
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Change Password', command=m.change_pass())
        filemenu.add_command(label='Contact Us', command=m.contact())
        filemenu.add_command(label='Exit', command=window.destroy)
        menubar.add_cascade(label='Help', font=('times', 29, ' bold '), menu=filemenu)

        ### TREEVIEW ATTENDANCE TABLE ###

        tree = ttk.Treeview(window, column=("rollNumber", "id", "fname", "lname", "gender", "department",
                                            "position", "gate", "date", "time", "pic"),
                            show="headings", height=30)

        tree.heading('rollNumber', text="No")
        tree.heading('id', text="ID")
        tree.heading('fname', text="First Name")
        tree.heading('lname', text="Last Name")
        tree.heading('gender', text="Gender")
        tree.heading('department', text="Department")
        tree.heading('position', text="Position")
        tree.heading('gate', text="Gate No")
        tree.heading('date', text="Date")
        tree.heading('time', text="Time")
        tree.heading('pic', text="Pic at the entry")

        tree.column('rollNumber', width=15)
        tree.column('id', width=15)
        tree.column('fname', width=75)
        tree.column('lname', width=75)
        tree.column('gender', width=20)

        tree.column('gate', width=30)
        tree.column('department', width=75)
        tree.column('date', width=75)
        tree.column('position', width=60)
        tree.column('time', width=70)
        tree.column('pic', width=250)

        # SCROLLBAR #
        scroll = Scrollbar(window, orient='vertical', command=tree.yview)
        scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
        tree.configure(yscrollcommand=scroll.set)
        tree.grid(row=1, column=1, sticky='nsew')

        # BUTTONS #

        # clearButton = Button(frame2, text="Clear", command=m.clear, fg="black", bg="#ea2a2a", width=11,
        #                      activebackground="white", font=('times', 11, ' bold '))
        # clearButton.place(x=335, y=86)
        # clearButton2 = Button(frame2, text="Clear", command=clear2, fg="black", bg="#ea2a2a", width=11,
        #                       activebackground="white", font=('times', 11, ' bold '))
        # clearButton2.place(x=335, y=172)

        trainImg = Button(frame2, text="Save Profile", command=m.psw(), fg="white", bg="blue", width=34, height=1,
                          activebackground="white", font=('times', 15, ' bold '))
        trainImg.place(x=30, y=420)
        trackImg = Button(frame1, text="Take Attendance", command=ma.TrackImages(), fg="black", bg="yellow", width=35, height=1,
                          activebackground="white", font=('times', 15, ' bold '))
        trackImg.place(x=30, y=50)
        quitWindow = Button(frame1, text="Quit", command=window.destroy, fg="black", bg="red", width=35, height=1,
                            activebackground="white", font=('times', 15, ' bold '))
        quitWindow.place(x=30, y=470)

        window.configure(menu=menubar)
        window.mainloop()


tt= maingui()
tt.main()
### END ###
