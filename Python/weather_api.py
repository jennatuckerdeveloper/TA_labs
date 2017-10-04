import requests

def weather_search(entry):

        if entry.isalpha():
            my_key = "q"
        else:
            my_key = "zip"


        package = {'APPID': 'ea3221716f0c2399c03894713e73deaf', my_key: entry}

        r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

        response = r.json()

        temp = response['main']['temp']

        ftemp = temp * (9/5) - 459.6

        ctemp = temp - 273.15

        return "Current {} weather is {}, {} degrees Fahrenheit {} degrees celsius.".format(response['name'], response['weather'][0]['description'], ftemp, ctemp)

def this():

# print(weather_search(input("Enter a city or zipcode: ")))
    print(weather_search("London"))
    print("Another test line.")
    return

# this()