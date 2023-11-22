import PySimpleGUI as sg
import csv

sg.theme('DarkGreen')  # Add a touch of color
sg.set_options(font='Arial 16')

# All the stuff inside your window
layout = [
    [sg.Text('Enter First Name'), sg.Push(), sg.InputText(key='-fname-')],
    [sg.Text('Enter Last Name'), sg.Push(), sg.InputText(key='-lname-')],
    [sg.Text('Enter Phone Number'), sg.Push(), sg.InputText(key='-phone-')],
    [sg.Text('Enter Email'), sg.Push(), sg.InputText(key='-email-')],
    [sg.Text('Enter Address'), sg.Push(), sg.InputText(key='-address-')],
    [sg.Button('Save'), sg.Button('Cancel')],
    [sg.Text("Search by Last name"), sg.Push(), sg.InputText(key='-searchText-')],
    [sg.Button('Search')],
    [sg.Text(key='-searchOutput-', )],
]

# Create the window
Window = sg.Window('Contact Book', layout, icon='favicon.ico')

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = Window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    fname = values['-fname-']
    lname = values['-lname-']
    phone = values['-phone-']
    email = values['-email-']
    address = values['-address-']
    info = [fname, lname, phone, email, address]
    if event == 'Save':
        with open('info.csv', 'a', newline="") as w:
            cw = csv.writer(w)
            cw.writerow(info)
            Window['-fname-'].update('')
            Window['-lname-'].update('')
            Window['-phone-'].update('')
            Window['-email-'].update('')
            Window['-address-'].update('')

    searchText = values['-searchText-']
    if event == 'Search':
        with open('info.csv', 'r') as r:
            cr = csv.reader(r)
            for i in cr:
                if i[1] == searchText:
                    Window['-searchOutput-'].update(
                        f"First Name: {i[0]}\nLast Name: {i[1]}\nPhone Number: {i[2]}\nEmail:{i[3]}\nAddress: {i[4]}")

Window.close()
