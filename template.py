import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = 'https://example.com'

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    response.raise_for_status()

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find elements by their HTML tags, classes, IDs, etc. and extract data
    # For example, to find all <a> tags with class 'link' and extract their text and href attributes
    links = soup.find_all('a', class_='link')
    for link in links:
        link_text = link.text
        link_href = link['href']
        print(f"Link Text: {link_text}, Link Href: {link_href}")

    # You can extract other types of data similarly using BeautifulSoup methods
    # For example, to find all <p> tags and extract their text
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        print("Paragraph:", paragraph.text)

except requests.RequestException as e:
    print("Error fetching webpage:", e)
except Exception as e:
    print("An error occurred:", e)
