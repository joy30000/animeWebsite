# import sys
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import requests
# import json

# # Check if URL is passed as an argument
# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)

# # Get URL from command line argument
# url = sys.argv[1]

# # Set up the WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # run in headless mode (no UI)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# #url = "https://9anime.org.lv/?s=bleach"
# # Send a GET request to the URL
# response = requests.get(url)



# # URL of the webpage to scrape
# #url = "https://9anime.org.lv/anime/dandadan/"  # Replace this with the actual URL you want to scrape
# #url="https://9anime.org.lv/anime/one-piece/"

# # Send a GET request to the URL
# #response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     html_doc = response.text  # Get the HTML content from the response

#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(html_doc, 'html.parser')

#     # Initialize a list to store the scraped data as dictionaries
#     anime_detail = []
#     similar_anime = []

#     try:
       


#         popular_divs = soup.find_all('div', class_='bsx')
#         #print(f"Number of divs found: {len(popular_divs)}")
#         search_anime = []
#         for i in range(len(popular_divs)):
#          show_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#          episode_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#          image_url = popular_divs[i].find('img')['src']
#          episode_url = popular_divs[i].find('a')['href']
#          episode_number = popular_divs[i].find('span', class_='epx').text.strip()
#          language= popular_divs[i].find('span', class_=['sb Sub', 'sb Dub']).text.strip()
#          #series= popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA']).text.strip() 
#          series = popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']).text.strip() if popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']) else "Null"
#          #print(series)
     

#          search_anime.append({
#               'title': show_title, 
#               'episode_title': episode_title,
#               'img':image_url,
#               'link': episode_url,
#               'episode_number': episode_number,
#               'language': language,
#               'series': series
#               })
         

       


#         # Overwrite the previous content of the file with new data
#         with open("9animeSearch.json", "w", encoding="utf-8") as json_file:
#             json.dump(search_anime, json_file, ensure_ascii=False, indent=4)

#         print("JSON file created/updated successfully.")
#         exit()
#     except Exception as e:
#         print(f"Error processing data: {e}")

# else:
#     print(f"Failed to fetch the webpage. Status code: {response.status_code}")



import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import json
import os

#Check if URL is passed as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

# Get URL base from command line argument (without the page number)
query = sys.argv[1]
print(query)
# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run in headless mode (no UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Initialize a list to store all scraped data
all_search_anime = []

# Loop through pages 1 to 5 (or as needed)
for page_num in range(1, 6):  # Pages 1 to 5
    # Update the URL to point to the current page
    #url = f"{url_base}page/{page_num}/"
    
    #url="https://9anime.org.lv/page/1/?s=naruto"

    # Send a GET request to the current page URL
    response = requests.get(f"https://9anime.org.lv/page/{page_num}/?s={query}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        html_doc = response.text  # Get the HTML content from the response

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')

        try:
            popular_divs = soup.find_all('div', class_='bsx')
            search_anime = []  # Temporarily store the data for the current page

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

            # Define the file path and create the 'data' directory if it doesn't exist
            data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
            if not os.path.exists(data_dir):
              os.makedirs(data_dir)

            # Append the current page's data to the overall list
            all_search_anime.extend(search_anime)
            print(f"Scraped page {page_num}")

        except Exception as e:
            print(f"Error processing data on page {page_num}: {e}")

    else:
        print(f"Failed to fetch page {page_num}. Status code: {response.status_code}")
json_file_path = os.path.join(data_dir, '9animeSearch.json')
# Overwrite the previous content of the file with all data from pages 1 to 5
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(all_search_anime, json_file, ensure_ascii=False, indent=4)

print("JSON file created/updated successfully.")