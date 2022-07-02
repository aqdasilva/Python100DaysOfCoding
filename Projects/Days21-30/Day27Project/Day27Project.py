from tkinter import *

def miles_to_km():
    miles = float(milesInput.get())
    km = miles * 1.609
    kilo_result_label.config(text=km)

window = Tk()
window.title("Miles to kilometer converter")
window.config(padx=20, pady=20)

milesInput = Entry(width=7)
milesInput.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="0")
kilo_result_label.grid(column=1, row=1)

kilo_label = Label(text="Km")
kilo_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=0, row=1)
