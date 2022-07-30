from tkinter import *
from functools import partial


PatientType = Tk()
PatientType.geometry('500x200')
PatientType.title('DoctorUI - Patient Selection')

def nextstepnewpatient():
  import NewProfileCreation
def nextstepexpatient():
  import ExistingPatientPage
NewPatientButton = Button(PatientType, text="New patient", command=nextstepnewpatient).grid(row=40, column=8)
ExPatientButton = Button(PatientType, text="Existing patient", command=nextstepexpatient).grid(row=40, column=9)