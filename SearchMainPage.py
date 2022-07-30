from tkinter import *
SearchMainPage = Tk()
SearchMainPage.geometry('500x200')
SearchMainPage.title('DoctorUI - Make a Medical enquiry')


def diseasesearch():
    import Diseasebasedsearch
def hospitalsearch():
    import HospitalBasedSearchEnquiry
DSearchButton = Button(SearchMainPage, text="Find for related illnesses", command=diseasesearch).grid(row=40, column=8)
HSearchButton = Button(SearchMainPage, text="Find for hospital diagnoses", command=hospitalsearch).grid(row=40, column=9)


 