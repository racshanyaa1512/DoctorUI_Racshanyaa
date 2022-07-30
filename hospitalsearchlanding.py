from tkinter import *
HospitalSearch = Tk()
HospitalSearch.geometry('500x200')
HospitalSearch.title('DoctorUI - Search Results')
import pandas as pd
df = pd.read_csv('DoctorUI-CentralDB (1).csv')
print(df.to_string()) 

