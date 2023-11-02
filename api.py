import requests
from bs4 import BeautifulSoup

# URL of the web page you want to scrape
url = "https://ftc-api.firstinspires.org/v2.0/2021/rankings/ILYAS1"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract data from the HTML content using BeautifulSoup's methods
    # For example, you can find a specific element by its tag and class
    data = soup.find('tag_name', class_='class_name').text

    # Print or process the extracted data
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")
