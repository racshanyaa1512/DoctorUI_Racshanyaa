from tkinter import *
from functools import partial


def movetosearch(PatientFullName, PatientNRIC, PatientSymptom1, PatientSymptom2, PatientSymptom3, PatientSymptom4):
   import SearchMainPage

def updatedb (PatientFullName, PatientNRIC, PatientSymptom1, PatientSymptom2, PatientSymptom3, PatientSymptom4):
  import resourcerequest
 
#window
ExistingPatientPage = Tk()
ExistingPatientPage.geometry('500x500')
ExistingPatientPage.title('DoctorUI - Update consultation')

#username label and text entry box
PatientFullName = Label(ExistingPatientPage, text="Patient's Full Name").grid(row=0, column=0)
PatientFullName = StringVar()
PatientFullNameEntry = Entry(ExistingPatientPage, textvariable=PatientFullName).grid(row=0, column=1)

PatientNRIC = Label(ExistingPatientPage, text="NRIC/FIN").grid(row=1, column=0)
PatientNRIC = StringVar()
PatientNRICEntry = Entry(ExistingPatientPage,textvariable=PatientNRIC).grid(row=1, column=1)

PatientSymptom1 = Label(ExistingPatientPage, text="Symptom 1 ").grid(row=2, column=0)
PatientSymptom1 = StringVar()
PatientSymptom1Entry = Entry(ExistingPatientPage, textvariable=PatientSymptom1).grid(row=2, column=1)

PatientSymptom2 = Label(ExistingPatientPage, text="Symptom 2").grid(row=4, column=0)
PatientSymptom2 = StringVar()
PatientSymptom2Entry = Entry(ExistingPatientPage, textvariable=PatientSymptom2).grid(row=4,column=1)

PatientSymptom3 = Label(ExistingPatientPage, text="Symptom 3").grid(row=5, column=0)
PatientSymptom3 = StringVar()
PatientSymptom3Entry = Entry(ExistingPatientPage, textvariable=PatientSymptom3).grid(row=5, column=1)

PatientSymptom4 = Label(ExistingPatientPage, text="Symptom 4").grid(row=6, column=0)
PatientSymptom4 = StringVar()
PatientSymptom4Entry = Entry(ExistingPatientPage,
textvariable=PatientSymptom4).grid(row=6,
column=1)

updatedb = partial(updatedb, PatientFullName, PatientNRIC, PatientSymptom1, PatientSymptom2, PatientSymptom3, PatientSymptom4)
movetosearch = partial(movetosearch, PatientFullName, PatientNRIC, PatientSymptom1, PatientSymptom2, PatientSymptom3, PatientSymptom4)

#save button
updateindbbutton = Button(ExistingPatientPage, text="Update to Database", command=updatedb).grid(row=20, column=1)
makeanenquirybutton = Button(ExistingPatientPage, text = "Make enquiries", command =movetosearch).grid(row = 22, column = 1)

ExistingPatientPage.mainloop()


