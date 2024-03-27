import re
from bs4 import BeautifulSoup
import requests
import openpyxl

# Creating Excel sheet
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Dealer List"

# Adding headers in Excel sheet
sheet.append(['Outlet_Name', 'Address', 'Phone', 'Timing'])

try:
    # Iterating the pages
    for page_num in range(1, 575):  # Assuming to scrap all pages in the website
        # Website URL
        url = f"https://dealers.tvsmotor.com/tvs-motors?page={page_num}"
        responsive = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36''(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
        soup = BeautifulSoup(responsive.text, 'html.parser')
        dealers = soup.find('div', class_="outlet-list").find_all('div')

        # Iterate over each dealer
        for dealer in dealers:
            # Extract data if available, else assign None
            dealer_name = dealer.find('li', class_="outlet-name").find('div', class_="info-text").a.text.strip() if dealer.find(
                'li', class_="outlet-name") else None
            address = dealer.find('li', class_="outlet-address").find('div', class_="info-text").span.text.strip() if dealer.find(
                'li', class_="outlet-address") else None
            phone = dealer.find('li', class_="outlet-phone").find('div', class_="info-text").a.text.strip() if dealer.find(
                'li', class_="outlet-phone") else None
            timings = dealer.find('li', class_="outlet-timings").find('div', class_="info-text").span.text.strip() if dealer.find(
                'li', class_="outlet-timings") else None

            # Remove extra spaces
            dealer_name = re.sub(r'\s+', ' ', dealer_name).strip() if dealer_name else None
            address = re.sub(r'\s+', ' ', address).strip() if address else None
            phone = re.sub(r'\s+', ' ', phone).strip() if phone else None
            timings = re.sub(r'\s+', ' ', timings).strip() if timings else None

            # Print and append data to Excel sheet
            if all((dealer_name, address, phone, timings)):
                print(dealer_name, address, phone, timings)
                sheet.append([dealer_name, address, phone, timings])

except requests.RequestException as e:
    print("Failed to fetch data:", e)

except Exception as e:
    print("An error occurred:", e)

# Save Excel file
excel.save("TVS Motor dealers.xlsx")

