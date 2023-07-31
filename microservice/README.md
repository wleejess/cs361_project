To use this microservice programmatically:
1. REQUEST data by writing to a "request.txt" file.
  Please use new lines for each parameter: API, zipcode, y/n air quality information.
  Example:
    Weather API
    92122
    no
2. RECEIVE data by reading from "response.txt" file.
  Currently contains a lot of information - recommend keys to access are:
    current, forecast, temp_c, temp_f.
------------------------------------------------------
To use this microservice with the provided GUI (see apiLinkGUI.py)
1. Select an API from dropdown.
2. Based on API, additional fields will be displayed. User must fill out these fields 
as they are necessary query parameters for the request.
------------------------------------------------------

<img width="573" alt="Screenshot 2023-07-31 at 12 24 58 PM" src="https://github.com/wleejess/cs361_project/assets/29618012/0559789e-6e40-43fd-aff1-c4710c6062a2">

------------------------------------------------------

APIs:
- Weather app
parameters = location, days, air quality index.
API key: d50dc7dd12384f2a80f17340723907

- Dictionary api.
parameters = word

-----------------------------------------------------
RESPONSES
Weather App response will be formatted as JSON.
Keys to access: "current" > "temp_c" or "temp_f"
  "precip_mm", "precip_in", "feelslike_c", "feelslike_f", etc.

Dictionary App response will be formatted as JSON.
Keys to access: "definition", "word"
