import PySimpleGUI as sg
import time
#running split to mph
leftCol = [
        [sg.Text("Split in minutes")],
        [sg.Text("Minutes:"),sg.Input(key = "-splitMin-",size=(3,1), ),sg.Text("Seconds:"),sg.Input(key="-splitSec-",size=(4,1))]

]

rightCol = [[sg.Text("Scalar Speed")],
            [sg.Input(key = "-scalarInput-",size=(3,1)),sg.DropDown(["Miles per Hour","Feet per Second","Kilometer per Hour","Meters per second"], default_value="Select Speed Scalar", key = "-scalarDropdown-") ]]



layout = [
    [sg.Text("Select the conversion you would like to make")],
    [sg.Column(leftCol),sg.VerticalSeparator(pad=None),sg.Column(rightCol) ],
    [sg.Button("Calulate"),sg.Button("Clear")]


]

window = sg.Window("Split to Speed", layout) 

def textBoxCap(length,windowKey):
    if len(values(windowKey)) > length:
        pass

def minSectoWholeMin(minutes,seconds):
    m = int(minutes)
    s = int(seconds)
    return m+((s*(5/3))/100)

    pass

while True:
    event, values = window.read()   
    
    if event == sg.WIN_CLOSED: #closes window if x is pressed
        break

    if event == "Calulate":
        if values["-splitMin-"] != "" or values["-splitSec-"] != "" and values["-scalarInput-"] == "":
            wholeTimeSplit = minSectoWholeMin(values["-splitMin-"], values["-splitSec-"])
            mphValue = 60/wholeTimeSplit
            if values["-scalarDropdown-"] == "Miles per Hour":
                window["-scalarInput-"].update(mphValue)
            elif values["-scalarDropdown-"] == "Feet per Second":
                window["-scalarInput-"].update(mphValue*1.46666667)
            elif values["-scalarDropdown-"] == "Kilometer per Hour":
                window["-scalarInput-"].update(mphValue*1.609344)
            elif values["-scalarDropdown-"] == "Meters per second":
                window["-scalarInput-"].update(mphValue/2.23693629)

    if event == "Clear":
        window["-splitMin-"].update("")
        window["-splitSec-"].update("")
        window["-scalarInput-"].update("")
        window["-scalarDropdown-"].update("Select Speed Scalar")
            
        

window.close()
