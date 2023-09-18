# This line imports the requests module, which allows you to send HTTP requests to websites and retrieve data from them. 
import requests

# This line uses the input function to prompt the user to enter the name of a city. The user's input is stored in the city variable. 
city = input('Input the city name: ')
# This line simply prints the city name that the user entered to the console.
print(city)

# This line prints a message indicating that you are about to display the weather report for the entered city.
#  It includes the city name provided by the user.
print('Displaying Weather report for: ', city)

# This line constructs a URL for retrieving weather information. It uses an f-string to insert the city variable into the URL, 
# so you get weather data for the specific city the user entered.
url = 'https://wttr.in/{}'.format(city)

# Here, you use the requests.get() function to send an HTTP GET request to the URL you constructed in the previous step. 
# This request is sent to the website 'wttr.in' with the specified city name.
res = requests.get(url)

# Finally, this line prints the text content of the HTTP response received from the weather website. 
# This content typically contains weather information for the specified city.
print(res.text)




