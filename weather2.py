import requests
from bs4 import BeautifulSoup

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
        with open('weather_details.html', 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print("Weather details saved to weather_details.html.")

    else:
        print("Failed to retrieve weather information.")

if __name__ == "__main__":
    scrape_weather()
