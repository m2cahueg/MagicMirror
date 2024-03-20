import datetime
from dateutil.relativedelta import relativedelta
import requests
from bs4 import BeautifulSoup

# Declaring Variables
owner = 'Greg'
birth_date = datetime.datetime.strptime('8/16/1987', '%m/%d/%Y')
birthday_countdown = 0
time = datetime.datetime.now()
age = 0
part_of_day = ''
printed_time = time.strftime("%I:%M %p")
printed_day = time.strftime("%A, %B %d of %Y")

# Determining the Part of Day
if time.hour < 6:
    part_of_day = 'Night'
elif time.hour < 12:
    part_of_day = 'Morning'
elif time.hour < 18:
    part_of_day = 'Afternoon'
else:
    part_of_day = 'Evening'

# Determining the owner's age and next_age
if time.month < birth_date.month:
    age = time.year - birth_date.year - 1
elif time.month == birth_date.month:
    if time.day < birth_date.day:
        age = time.year - birth_date.year - 1
    else:
        age = time.year - birth_date.year
else:
    age = time.year - birth_date.year

next_age = age + 1
next_birthday = birth_date + relativedelta(years=next_age)

# Determining the number of days until the owner's next birthday.
birthday_countdown = next_birthday - time
retirement_countdown = birth_date + relativedelta(years=67) - time

# Parsing Data
greeting = f"Good {part_of_day}, {owner}!"
time_statement = f"It is {printed_time} on {printed_day}.\n"
birthday_statement = f"There are {birthday_countdown.days} days until you turn {next_age} years old.\n"
retirement_statement = f"There are {retirement_countdown.days} days until you retire.\n"
greeting_html = f"<P> <h1> {greeting} </h1>"
time_statement_html = f"<P> {time_statement}"
birthday_statement_html = f"<P> {birthday_statement}"
retirement_statement_html = f"<P> {retirement_statement}"

# Outputing Data
print(greeting)
print(time_statement)
print(birthday_statement)
print(retirement_statement)

# Writing HTML content to a file
with open('/var/www/html/index.html', 'w') as file:
    file.write('<HTML>\n')
    file.write('<body style="background-color:black;">\n')
    file.write('<body text="#ffffff" link="#ff0000" vlink="#ff0000" alink="#ff0000">\n')
    file.write('<HEAD>\n')
    file.write('<style>\n')
    file.write('h1 {text-align: center;}\n')
    file.write('p {text-align: left;}\n')
    file.write('div {text-align: center;}\n')
    file.write('</style>\n')
    file.write(greeting_html)
    file.write('</HEAD>\n')
    file.write(time_statement_html)
    file.write(birthday_statement_html)
    file.write(retirement_statement_html)

    
    # Scraping Weather Details
def scrape_weather():
    # URL of the weather website for Louisville, Kentucky
    url = 'https://weather.com/weather/today/l/40202'

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the weather information
        weather_details = soup.find_all(class_='WeatherDetailsListItem--wxData--kK35q')

        # Construct HTML string with weather details
        html_content = "<html><head><title>Weather Details</title></head><body><h1>Weather Details</h1>"
        for detail in weather_details:
            label = detail.find_previous(class_='WeatherDetailsListItem--label--2ZacS').get_text(strip=True)
            value = detail.get_text(strip=True)
            # Exclude 'Wind Direction' from the output
            if 'Wind' not in label:
                html_content += f"<p><strong>{label}:</strong> {value}</p>"
        html_content += "</body></html>"

        # Write HTML content to a file
        with open('/var/www/html/index.html', 'a', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print("Weather details saved to weather_details.html.")

    else:
        print("Failed to retrieve weather information.")

scrape_weather()

with open('/var/www/html/index.html', 'a') as file:
    file.write('</BODY>\n')
    file.write('</HTML>\n')
