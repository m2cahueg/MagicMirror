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

        # Print the weather report
        print("Louisville Weather Details:")
        for detail in weather_details:
            label = detail.find_previous(class_='WeatherDetailsListItem--label--2ZacS').get_text(strip=True)
            value = detail.get_text(strip=True)
            # Exclude 'Wind Direction' from the output
            if 'Wind' not in label:
                print(f"{label}: {value}")

    else:
        print("Failed to retrieve weather information.")

if __name__ == "__main__":
    scrape_weather()

