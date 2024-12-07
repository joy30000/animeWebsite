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
# # response = requests.get(url)



# # URL of the webpage to scrape
# #url = "https://9anime.org.lv/anime/dandadan/"  # Replace this with the actual URL you want to scrape
# # url="https://9anime.org.lv/anime/one-piece/"

# #Send a GET request to the URL
# response = requests.get(url)

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



# import sys
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import requests
# import json
# import os

# #Check if URL is passed as an argument
# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)

# # Get URL base from command line argument (without the page number)
# query = sys.argv[1]
# print(query)
# # Set up the WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # run in headless mode (no UI)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Initialize a list to store all scraped data
# all_search_anime = []

# # Loop through pages 1 to 5 (or as needed)
# for page_num in range(1, 5):  # Pages 1 to 5
#     # Update the URL to point to the current page
#     #url = f"{url_base}page/{page_num}/"
    
#     #url="https://9anime.org.lv/page/1/?s=naruto"

#     # Send a GET request to the current page URL
#     response = requests.get(f"https://9anime.org.lv/page/{page_num}/?s={query}")

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         html_doc = response.text  # Get the HTML content from the response

#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(html_doc, 'html.parser')

#         try:
#             popular_divs = soup.find_all('div', class_='bsx')
#             print(popular_divs)
#             search_anime = []  # Temporarily store the data for the current page

#             for i in range(len(popular_divs)):
#                 show_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#                 episode_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#                 image_url = popular_divs[i].find('img')['src']
#                 episode_url = popular_divs[i].find('a')['href']
#                 episode_number = popular_divs[i].find('span', class_='epx').text.strip()
#                 language = popular_divs[i].find('span', class_=['sb Sub', 'sb Dub']).text.strip()
#                 series = popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']).text.strip() if popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']) else "Null"
                
#                 search_anime.append({
#                     'title': show_title,
#                     'episode_title': episode_title,
#                     'img': image_url,
#                     'link': episode_url,
#                     'episode_number': episode_number,
#                     'language': language,
#                     'series': series
#                 })

        

#             # Append the current page's data to the overall list
#             all_search_anime.extend(search_anime)
#             print(f"Scraped page {page_num}")

#         except Exception as e:
#             print(f"Error processing data on page {page_num}: {e}")

#     else:
#         print(f"Failed to fetch page {page_num}. Status code: {response.status_code}")
#     # Define the file path and create the 'data' directory if it doesn't exist
# # data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
# # if not os.path.exists(data_dir):
# #   os.makedirs(data_dir)    
      
# # json_file_path = os.path.join(data_dir, '9animeSearch.json')
# # Overwrite the previous content of the file with all data from pages 1 to 5
# with open('9animeSearch.json', "w", encoding="utf-8") as json_file:
#     json.dump(all_search_anime, json_file, ensure_ascii=False, indent=4)

# print("JSON file created/updated successfully.")


# import sys
# import os
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup

# # Check if URL is passed as an argument
# if len(sys.argv) < 2:
#     print("Usage: python script.py <search_query>")
#     sys.exit(1)

# # Get search query from the command line
# query = sys.argv[1]
# print(f"Searching for: {query}")

# # Set up the WebDriver options for headless Chrome
# options = Options()
# options.add_argument("--headless")  # run in headless mode (no UI)
# options.add_argument("--no-sandbox")  # Required for running on cloud services like Render
# options.add_argument("--disable-dev-shm-usage")  # Overcome memory issues on cloud servers
# options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration

# # Initialize the Selenium WebDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Initialize a list to store all scraped data
# all_search_anime = []

# # Loop through pages 1 to 5 (or as needed)
# for page_num in range(1, 6):  # Pages 1 to 5
#     # URL for the current page
#     url = f"https://9anime.org.lv/page/{page_num}/?s={query}"

#     # Use Selenium to open the URL and get the page source
#     driver.get(url)
    
#     # Give the page time to load (adjust the sleep time if needed)
#     time.sleep(3)  # Wait for JavaScript to load the content
    
#     # Get the page source after JavaScript is loaded
#     html_doc = driver.page_source
    
#     # Parse the HTML content with BeautifulSoup
#     soup = BeautifulSoup(html_doc, 'html.parser')

#     try:
#         # Find the divs containing the search results
#         popular_divs = soup.find_all('div', class_='bsx')
#         search_anime = []  # Temporarily store the data for the current page

#         for i in range(len(popular_divs)):
#             show_title = popular_divs[i].find('h2', itemprop='headline').text.strip() if popular_divs[i].find('h2', itemprop='headline') else "Unknown Title"
#             episode_title = show_title  # You are using the same title for episode
#             image_url = popular_divs[i].find('img')['src'] if popular_divs[i].find('img') else 'https://example.com/default-image.jpg'
#             episode_url = popular_divs[i].find('a')['href'] if popular_divs[i].find('a') else 'No URL'
#             episode_number = popular_divs[i].find('span', class_='epx').text.strip() if popular_divs[i].find('span', class_='epx') else "Unknown"
#             language = popular_divs[i].find('span', class_=['sb Sub', 'sb Dub']).text.strip() if popular_divs[i].find('span', class_=['sb Sub', 'sb Dub']) else "Unknown Language"
#             series = popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']).text.strip() if popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']) else "Null"
            
#             # Append the scraped data to the search_anime list
#             search_anime.append({
#                 'title': show_title,
#                 'episode_title': episode_title,
#                 'img': image_url,
#                 'link': episode_url,
#                 'episode_number': episode_number,
#                 'language': language,
#                 'series': series
#             })
#         print(search_anime)

#         # Define the file path and create the 'data' directory if it doesn't exist
#         data_dir = os.path.join(os.path.dirname(__file__),'..', 'data')
#         if not os.path.exists(data_dir):
#             os.makedirs(data_dir)

#         # Append the current page's data to the overall list
#         # all_search_anime.extend(search_anime)
#         print(f"Scraped page {page_num}")

#     except Exception as e:
#         print(f"Error processing data on page {page_num}: {e}")

# # Save the data to a JSON file after all pages are scraped
# json_file_path = os.path.join(data_dir, '9animeSearch.json')
# with open(json_file_path, "w", encoding="utf-8") as json_file:
#     json.dump(search_anime, json_file, ensure_ascii=False, indent=4)

# print("JSON file created/updated successfully.")

# # Close the WebDriver after scraping
# driver.quit()



# import sys
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import requests
# import json
# import os

# # Check if URL is passed as an argument
# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)

# # Get URL base from command line argument (without the page number)
# query = sys.argv[1]
# print(query)

# # Set up the WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # run in headless mode (no UI)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Initialize a list to store all scraped data
# all_search_anime = []

# # Loop through pages 1 to 5 (or as needed)
# for page_num in range(1, 6):  # Pages 1 to 5
#     # Send a GET request to the current page URL
#     response = requests.get(f"https://9anime.org.lv/page/{page_num}/?s={query}")

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         html_doc = response.text
        
#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(html_doc, 'html.parser')
#         # soup.prettify(html_doc)  # Get the HTML content from the response
#         # print(html_doc) 
#         try:
#             popular_divs = soup.find_all('div', class_='bsx')
#             print(popular_divs)
#             search_anime = []  # Temporarily store the data for the current page

#             # If there is no data on the page, break out of the loop
#             if not popular_divs:
#                 print(f"No data found on page {page_num}. Stopping scraping.")
#                 break

#             for i in range(len(popular_divs)):
#                 show_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#                 episode_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#                 image_url = popular_divs[i].find('img')['src']
#                 episode_url = popular_divs[i].find('a')['href']
#                 episode_number = popular_divs[i].find('span', class_='epx').text.strip()
#                 language = popular_divs[i].find('span', class_=['sb Sub', 'sb Dub']).text.strip()
#                 series = popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']).text.strip() if popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']) else "Null"
                
#                 search_anime.append({
#                     'title': show_title,
#                     'episode_title': episode_title,
#                     'img': image_url,
#                     'link': episode_url,
#                     'episode_number': episode_number,
#                     'language': language,
#                     'series': series
#                 })

#             # Append the current page's data to the overall list
#             all_search_anime.extend(search_anime)
#             print(f"Scraped page {page_num}")

#         except Exception as e:
#             print(f"Error processing data on page {page_num}: {e}")

#     else:
#         print(f"Failed to fetch page {page_num}. Status code: {response.status_code}")

# # Define the file path and create the 'data' directory if it doesn't exist
# data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
# if not os.path.exists(data_dir):
#     os.makedirs(data_dir)

# # Write the collected data into a JSON file
# json_file_path = os.path.join(data_dir, '9animeSearch.json')
# with open(json_file_path, "w", encoding="utf-8") as json_file:
#     json.dump(all_search_anime, json_file, ensure_ascii=False, indent=4)

# print("JSON file created/updated successfully.")



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
base_url = "https://9anime.org.lv/page/1/?s=attack"
# Initialize an empty list to store anime details
search_anime = []

# Loop through pages 1 to 5
for page_number in range(1, 6):
    page_url = base_url.replace('page/1', f'page/{page_number}')
    final_url = page_url.replace('attack', f'{query}')  # Update the page URL dynamically
    # print(f"Scraping data from: {page_url}")
    print(f"Scraping data from: {final_url}")

    # Send a GET request to the URL
    # response = requests.get(page_url)
    response = requests.get(final_url)

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

json_file_path = os.path.join(data_dir, '9animeSearch.json')
# Overwrite the previous content of the file with new data
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(search_anime, json_file, ensure_ascii=False, indent=4)

print("JSON file created/updated successfully.")