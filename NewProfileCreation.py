from tkinter import *
from functools import partial


def nextstep(PatientFullName, PatientNRIC, PatientCoverage1, PatientCoverage2, PatientDOB, PatientBlood, PatientPastDiag):
  print("patient full name (as in entry) :", PatientFullName.get())
  print("patient nric (as in entry) :", PatientNRIC.get())
  print("patient coverage 1 (as in entry)", PatientCoverage1.get())
  print("patient coverage2 (as in entry) :", PatientCoverage2.get())
  print("patient past diagnosis (as in entry) :", PatientPastDiag.get())
  
  


#window
PatientRecordWindow = Tk()
PatientRecordWindow.geometry('500x200')
PatientRecordWindow.title('DoctorUI - Create New Patient Profile')

#username label and text entry box
PatientFullName = Label(PatientRecordWindow, text="Patient's Full Name").grid(row=0, column=0)
PatientFullName = StringVar()
PatientFullNameEntry = Entry(PatientRecordWindow, textvariable=PatientFullName).grid(row=0, column=1)

PatientNRIC = Label(PatientRecordWindow, text="NRIC/FIN").grid(row=1, column=0)
PatientNRIC = StringVar()
PatientNRICEntry = Entry(PatientRecordWindow,textvariable=PatientNRIC).grid(row=1, column=1)

PatientDOB = Label(PatientRecordWindow, text="Date of Birth of Patient").grid(row=2, column=0)
PatientDOB = StringVar()
PatientDOBEntry = Entry(PatientRecordWindow, textvariable=PatientDOB).grid(row=2, column=1)

PatientCoverage1 = Label(PatientRecordWindow,
text="Insurance Coverage 1 ").grid(row=3, column=0)
PatientCoverage1 = StringVar()
PatientCoverage1Entry = Entry(PatientRecordWindow, textvariable=PatientCoverage1).grid(row=3,column=1)

PatientCoverage2 = Label(PatientRecordWindow, text="Insurance coverage 2").grid(row=4, column=0)
PatientCoverage2 = StringVar()
PatientCoverage2Entry = Entry(PatientRecordWindow, textvariable=PatientCoverage2).grid(row=4,column=1)

PatientBlood = Label(PatientRecordWindow, text="Blood Group").grid(row=5, column=0)
PatientBlood = StringVar()
PatientBloodEntry = Entry(PatientRecordWindow, textvariable=PatientBlood).grid(row=5, column=1)

PatientPastDiag = Label(PatientRecordWindow, text="Past Diagnoses").grid(row=6, column=0)
PatientPastDiag = StringVar()
PatientPastDiagEntry = Entry(PatientRecordWindow,
textvariable=PatientPastDiag).grid(row=6,
column=1)

nextstep = partial(nextstep, PatientFullName, PatientNRIC, PatientCoverage1, PatientCoverage2, PatientDOB,
PatientBlood, PatientPastDiag)

#save button
savebutton = Button(PatientRecordWindow, text="Save Profile", command=nextstep).grid(row=20, column=1)

PatientRecordWindow.mainloop()


