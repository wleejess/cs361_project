import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import requests, json

# Links to external APIs.
# API-Ninjas has multiple APIs we can connect to using the same API key.
# Weather API is a standalone API with more details.
dictURL = 'https://api.api-ninjas.com/v1/dictionary?word='
apiKey = 'MHAI7hT+sM3bb5qHPgNJAQ==l8JMQvodCsgrjMAm'
weatherURL = 'http://api.weatherapi.com/v1/forecast.json?key=d50dc7dd12384f2a80f173407232907'


# Create our GUI
window = tk.Tk()
window.title("API Link")
window.geometry("500x300")
frame = Frame(window)
frame.pack()

def display():
    """
    Function to display additional fields based on the selected API.
    These fields are customized for each API and will request query parameters from the user.
    """
    if apiSelector.get() == 'Weather API':
        word.pack_forget()
        textBox.pack_forget()
        apiBtn.pack_forget()

        location.pack()
        textBox.pack()
        aqi.pack()
        aqiSelected.pack()
        apiBtn.pack()
    elif apiSelector.get() == 'Dictionary API':
        location.pack_forget()
        aqi.pack_forget()
        aqiSelected.pack_forget()
        textBox.pack_forget()
        apiBtn.pack_forget()

        word.pack()
        textBox.pack()
        apiBtn.pack()

def submitInfo():
    """
    When all necessary parameters have been filled out, this function will call the API.
    If the request is successful, data is written to a request.txt file. 
    If the request is unsucessful, an error message will be printed.
    """
    if apiSelector.get() == 'Weather API':
        locationParam = textBox.get("1.0",'end-1c')
        aqiParam = aqiSelected.get()
        keyString = "&q=" + locationParam + "&days=1" + "&aqi=" + aqiParam.lower() + "&alerts=no"
        fullString = weatherURL + keyString
        print(fullString)
        response = requests.get(fullString)

        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
        else:
            f = open("request.txt", "w")
            f.write(response.text)
            f.close()
    elif apiSelector.get() == 'Dictionary API':
        wordParam = textBox.get("1.0",'end-1c')
        fullURL = dictURL + wordParam.lower()
        print(fullURL)
        response = requests.get(fullURL, headers={'X-Api-Key':apiKey})
        if response.status_code == requests.codes.ok:
            f = open("request.txt", "w")
            f.write(response.text)
            f.close()
        else:
            print("Error:", response.status_code, response.text)

# Additional styling/layout of GUI.
# Widgets are displayed/hidden depending on which API is selected.
ttk.Label(window, text="").pack(side = TOP)
ttk.Label(window, text="Please select an API you'd like to connect to.", font=("Consolas", 12)).pack(side = TOP)
apiSelector = tk.StringVar()
appSelected = ttk.Combobox(window, width = 20, textvariable = apiSelector)
appSelected['values'] = ('Weather API', 'Dictionary API')
appSelected.pack(side = TOP)
apiBtn = ttk.Button(window, text="Choose this API", command=display).pack(side = TOP)

location = ttk.Label(window, text="Enter City Name or Zipcode")
word = ttk.Label(window, text="Enter ONE word to look up in the dictionary")
textBox = Text(window, height = 2, width = 35)

aqi = ttk.Label(window, text="Air Quality Info: Y/N")
aqiSelector = tk.StringVar()
aqiSelected = ttk.Combobox(window, width = 27, textvariable = aqiSelector)
aqiSelected['values'] = ('Yes', 'No')

apiBtn = ttk.Button(window, text="Get data!", command=submitInfo)

window.mainloop()