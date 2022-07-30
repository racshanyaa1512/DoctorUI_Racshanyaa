from tkinter import *
from functools import partial

HospitalSearch = Tk()
HospitalSearch.geometry('500x200')
HospitalSearch.title('DoctorUI - Search in hospital for illness encounters')

def nextstep(DiseaseName):
    import hospitalsearchlanding

DiseaseNameLabel = Label(HospitalSearch, text="Enter the disease/illness title").grid(row=0, column=0)
DiseaseName = StringVar()
DiseaseNameEntry = Entry(HospitalSearch, textvariable=DiseaseName).grid(row=0, column=1)  

HSearchButton = Button(HospitalSearch, text="Search", command=lambda:nextstep).grid(row=40, column=9)
