import tkinter as tk  # importing tkinter lib for GUI
from tkinter import *  # this is for button lable and input
from tkinter import ttk  # (themed Tkinter)provides several additional widgets, such as themed buttons,comboboxes
import requests  # send HTTP requests and receive responses from web services and APIs.
import json  # (JavaScript Object Notation) data. format that is easy to read and write for humans, and easy to parse and generate for machines.
from PIL import ImageTk, Image  # ImageTk and Image are classes provided by
# the Pillow library that allow you to work with images in tkinter.

def convertr():   #this function is converting the currencies using API
    # global symbol
    app_id = '5d22fa3247fe4a58a520a75e7dd64f98'

    # Make a request to the latest exchange rates API endpoint
    response = requests.get(f'https://openexchangerates.org/api/latest.json?app_id={app_id}')

    # Check if the request was successful
    if response.status_code == 200:

        # Parse the JSON response and extract the exchange rates data
        exchange_rates = response.json()['rates']  # is a dictionary that contains the exchange rates of different
        # currencies with respect to a base currency.
        # print(exchange_rates)
        currency_1 = list.get()  # here we get the option from list 1
        currency_2 = option.get()  # here i get the option from list 2
        amount = float(inputt.get())  # here the value user will give
        rate_1 = exchange_rates[currency_1]
        rate_2 = exchange_rates[currency_2]
        converted_amount = round(amount / rate_1 * rate_2,
                                 2)  # The result is rounded to two decimal places using the round()
        formated = '{:,.2f}'.format(converted_amount)
        Result['text'] = formated
        print(converted_amount, formated)

    else:
        print(f'Request failed with status code {response.status_code}')


def reset():  # this function reset the all values
    inputt.delete(0, END)  # the value  user will enter will be deleted
    list.set('')  # the value from list will be empty
    option.set('')  # the value to list will be empty
    Result['text'] = ''  # result box will also empty


GUI = tk.Tk()  # simply make windows
GUI.geometry("500x500")  # size of window
GUI.title("Sana's Curency Convertor")
GUI.resizable(height=False, width=False)  #fixed the size
# Fram for heading
heading = Frame(GUI, width=470, height=100)    # rectangular area
heading.place(x=15, y=30)

# logo

logo = Image.open('logo.png')
logo = logo.resize((40, 40))
logo = ImageTk.PhotoImage(logo)   # used to display images in labels, buttons,

Frame_heading = Label(heading, image=logo, compound=LEFT, text='Currency Convertor', height=5, padx=13,
                      pady=30, font=("Arial 16 bold"), fg='black', bg='white')
Frame_heading.place(x=90, y=14)

Result = Label(GUI, text='', width=16, height=2, pady=2, relief="solid", font=("Ivy 16 bold"), fg='black')
Result.place(x=140, y=140)

Currency = ['PKR', 'INR', 'EUR', 'USD', 'CAD', 'QR']
From = Label(GUI, text='From', width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=("Ivy 10"), fg='black')
From.place(x=100, y=220)

list = ttk.Combobox(GUI, width=8, justify=CENTER, font=("Ivy 12 bold"))
list['values'] = Currency
list.place(x=140, y=220)
To_label = Label(GUI, text='To', width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=("Ivy 10"),
                 fg='black')
To_label.place(x=250, y=220)
option = ttk.Combobox(GUI, width=8, justify=CENTER, font=("Ivy 12 bold"))
option['values'] = Currency
option.place(x=280, y=220)

# input
inputt = Entry(GUI, width=22, justify=CENTER, relief='solid', font=("Ivy 12 bold"))
inputt.place(x=150, y=270)

# button
button = Button(GUI, text="Convertor", width=7, padx=5, height=1, bg="blue", fg='white',
                font=("Ivy 10 bold"), command=convertr)
button.place(x=170, y=310)
reset_button = Button(GUI, text="Reset", width=7, padx=5, height=1, bg="red", fg='white',
                      font=("Ivy 10 bold"), command=reset)
reset_button.place(x=260, y=310)

GUI.mainloop()
