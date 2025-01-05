
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import json
import os

# Check if URL is passed as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

# Get the base URL from command line argument
# base_url = sys.argv[1]
query = sys.argv[1]

#base_url = "https://9anime.org.lv/page/1/?s=attack"

# Initialize an empty list to store anime details
search_anime = []
page1_url = query + "page/1"
#https://9anime.org.lv/genres/action/page/3/
# Loop through pages 1 to 5
for page_number in range(1, 10):
    
    page2_url = page1_url.replace('page/1', f'page/{page_number}')
    # final_url = page_url.replace('attack', f'{query}')  # Update the page URL dynamically
    # # print(f"Scraping data from: {page_url}")
    # print(f"Scraping data from: {final_url}")

    # Send a GET request to the URL
    # response = requests.get(page_url)
    response = requests.get(page2_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_doc = response.text  # Get the HTML content from the response

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')

        # Find all divs that contain anime details
        popular_divs = soup.find_all('div', class_='bsx')

        if not popular_divs:
            print(f"No data found on page {page_number}. Stopping the scraping.")
            break  # Stop scraping if no data is found

        # Loop through each div and extract anime details
        for i in range(len(popular_divs)):
            show_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
            episode_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
            image_url = popular_divs[i].find('img')['src']
            episode_url = popular_divs[i].find('a')['href']
            episode_number = popular_divs[i].find('span', class_='epx').text.strip()
            language = popular_divs[i].find('span', class_=['sb Sub', 'sb Dub']).text.strip()
            series = popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']).text.strip() if popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']) else "Null"

            search_anime.append({
                'title': show_title,
                'episode_title': episode_title,
                'img': image_url,
                'link': episode_url,
                'episode_number': episode_number,
                'language': language,
                'series': series
            })
    else:
        print(f"Failed to fetch page {page_number}. Status code: {response.status_code}")
        break  # Stop scraping if page fetch fails
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
if not os.path.exists(data_dir):
   os.makedirs(data_dir)

json_file_path = os.path.join(data_dir, '9animeShounene.json')
# # Overwrite the previous content of the file with new data
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(search_anime, json_file, ensure_ascii=False, indent=4)
# with open("9animeShounene.json", "w", encoding="utf-8") as json_file:
#     json.dump(search_anime, json_file, ensure_ascii=False, indent=4)

print("JSON file created/updated successfully.")