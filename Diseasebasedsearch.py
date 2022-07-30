from tkinter import *
import tkinter
from functools import partial

criteriafulfilled = 1 
def resourcerequest(PatientFullName, PatientNRIC, PatientSymptom1, PatientSymptom2, PatientSymptom3, PatientSymptom4, PatientSymptom5):
  open(resourcerequest.py)
Diseasebasedsearch = Tk()

SymptomsList = Listbox(Diseasebasedsearch)
SymptomsList.insert(1, "Nausea")
SymptomsList.insert(2, "Weakness in face")
SymptomsList.insert(3, "Confusion and lack of coordination")
SymptomsList.insert(4, "Dizziness")
SymptomsList.insert(5, "Numbness")
SymptomsList.insert(6, "Vision blurring")
SymptomsList.insert(7, "Memory loss and poor judgement")
SymptomsList.insert(8, "Halluncination")
SymptomsList.insert(9, "Fever")
SymptomsList.insert(10, "Chills")

from ExistingPatientPage import * 
if criteriafulfilled == 1:
  criteriafulfilled = Label(Diseasebasedsearch, text="Illness confirmed : Stroke - REQUIRES IMMEDIATE MEDICAL TREATMENT").grid(row=0, column=0)

ExtraButton = Button(Diseasebasedsearch, text="Resources required", command=resourcerequest).grid(row=40, column=9)
