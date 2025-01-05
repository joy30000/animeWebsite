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

# # Get URL from command line argument
# url = sys.argv[1]

# # Set up the WebDriver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # run in headless mode (no UI)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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
#         # Extract all matching elements
#         titles = soup.find_all(class_="entry-title")
#         title = titles[0].get_text().strip().replace("\n", "") if titles else ""


#         details = soup.find_all(class_="spe")
#         detail = str(details[0]) if details else ""
#         if detail:
#          detail = detail.replace('</span>', '</span><br>')

          
#         div_tag = soup.find('div', class_='thumb')
#         if div_tag:
#          img_tag = div_tag.find('img')  # Finds the first <img> tag inside the div
#          if img_tag:
#           img_url = img_tag.get('src')  
#          else:
#           img_url='https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg' 
#         else:
#           img_url='https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg' 
         
       

#         div_tag = soup.find('div', class_='ime')
#         if div_tag:
#          cover_img_tag = div_tag.find('img') 
#          if cover_img_tag:
#           cover_img_url = cover_img_tag.get('src')  
#          else:
#           cover_img_url='https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg' 
#         else:
#           cover_img_url='https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'    


#         genres = soup.find_all(class_="genxed")
#         genre= str(genres[0]) if genres else "" 


#         descriptions = soup.find_all(class_="entry-content")
#         description=str(descriptions)
#         description = description.replace('[', '').replace(']', '')


#         episodes = soup.find('div', class_='eplister')
#         ul_tag = episodes.find('ul') if episodes else None 
#         if ul_tag:
#          ul_html = str(ul_tag)
#          ul_html = ul_html.replace('https:', '/home/anime_episode?url=https:') 
#         else:
#          print("No <ul> found inside the 'eplister' div.")


        

       


        



        
       

#         #---------------------------------------- SIMILAR ANIME --------------------------------------------#
        
#         s_titles = soup.find_all('h2', {'itemprop': 'headline'})
#         s_series = soup.find_all(class_=["typez TV", "typez Movie"])
#         s_statuss = soup.find_all(class_="epx")
#         s_languages = soup.find_all(class_=["sb Sub", "sb Dub"])
#         s_links = soup.find_all("a", class_="tip")

#         div_tags = soup.find_all('div', class_='bsx')
#         s_img_tags = [div.find_all('img') for div in div_tags]


#         # # Extract data for similar anime
#         for i in range(len(s_titles)):
#             similar_title = s_titles[i].get_text().strip().replace("\n", "") if i < len(s_titles) else ""
#             similar_series = s_series[i].get_text().strip().replace("\n", "") if i < len(s_series) else "TV"
#             similar_status = s_statuss[i].get_text().strip().replace("\n", "") if i < len(s_statuss) else ""
            
#             similar_language = s_languages[i].get_text().strip().replace("\n", "") if i < len(s_languages) else ""

    
#             if i < len(s_img_tags) and len(s_img_tags[i]) > 0:
#             # For each div, we need to check if the image has the 'data-src' attribute
#              similar_img_url = s_img_tags[i][0].get('data-src', '')  # Get the first image in the div
#             if not similar_img_url:
#              similar_img_url = s_img_tags[i][0].get('src', '')  # Fallback to 'src' if 'data-src' is not present
#             else:
#              similar_img_url = 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'  # Default image URL

#             similar_href = s_links[i]['href'] if i < len(s_links) and 'href' in s_links[i].attrs else None
       

#             # Append the extracted data to the list as a dictionary
#             similar_anime.append({
#                 'title': similar_title,
#                 'series': similar_series,
#                 'status': similar_status,
#                 'language': similar_language,
#                 'img': similar_img_url,
#                 'link': similar_href
#             })


# #----------------------  MAIN ANIME DETAIL ARRAY-----------------------------------------------------------------
            
#          # Append the main anime data to the anime_detail list
#         anime_detail.append({
#             'title': title,
#             'status': detail,
#             'img': img_url,
#             'cover_img': cover_img_url,
#             'genres': genre,
#             'description': description,
#             'episodes': ul_html,
#             'Similar_Anime_List': similar_anime
#         })

#         json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeDetail.json')
#         # Overwrite the previous content of the file with new data
#         with open(json_file_path, "w", encoding="utf-8") as json_file:
#             json.dump(anime_detail, json_file, ensure_ascii=False, indent=4)

#         print("JSON file created/updated successfully.")
#         exit()
#     except Exception as e:
#         print(f"Error processing data: {e}")

# else:
#     print(f"Failed to fetch the webpage. Status code: {response.status_code}")




#//----------------------------------------------------------------------------------------------------

import sys
import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Check if URL is passed as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

# Get URL from command line argument
url = sys.argv[1]

# Set up the WebDriver options
# options = Options()
# options.add_argument("--headless")  # run in headless mode (no UI)
# options.add_argument("--no-sandbox")  # To run in restricted environments like Render
# options.add_argument("--disable-dev-shm-usage")  # To fix Chrome crash issues on limited memory
# options.add_argument("--disable-gpu")  # Disable GPU acceleration (not needed in headless mode)

# # # Set up the WebDriver with ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Use Selenium to get the page content
# driver.get(url)

# # Wait for the page to load (you may adjust the sleep time based on the website's loading time)
# time.sleep(3)  # Wait for JavaScript to load the content

response = requests.get(url)

    # Check if the request was successful (status code 200)
if response.status_code == 200:
      html_doc = response.text
# Get the HTML content of the page
#html_doc = driver.page_source

# Parse the HTML content with BeautifulSoup
      soup = BeautifulSoup(html_doc, 'html.parser')

# Initialize lists to store the scraped data
      anime_detail = []
      similar_anime = []

   
    # Extract basic anime details
      titles = soup.find_all(class_="entry-title")
      title = titles[0].get_text().strip().replace("\n", "") if titles else ""

      details = soup.find_all(class_="spe")
      detail = str(details[0]) if details else ""
      if detail:
        detail = detail.replace('</span>', '</span><br>')

      div_tag = soup.find('div', class_='thumb')
      img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

      div_tag = soup.find('div', class_='ime')
      cover_img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

      # genres = soup.find_all(class_="genxed")
      # genre = str(genres[0]) if genres else ""
      genres_data = []
       # genres = soup.find_all(class_="genxed")
      genres = soup.find('div', class_='genxed')
       #genre= str(genres[0]) if genres else "" 
        # Find all <a> tags and extract the text and href
      links = genres.find_all('a')
      for link in links:
         text = link.get_text()  # Extract text
         href = link.get('href')  # Extract href attribute

         genres_data.append({
        'text': text,
        'link': href
        
        })

      descriptions = soup.find_all(class_="entry-content")
      description = str(descriptions).replace('[', '').replace(']', '')

      # episodes = soup.find('div', class_='eplister')
      # ul_tag = episodes.find('ul') if episodes else None
      # ul_html = str(ul_tag).replace('https:', '/anime_episode?url=https:').replace('<a','<Link').replace('a>','Link>') if ul_tag else "No episodes found"
      eplister = soup.find('div', class_='eplister')

# Find all <li> tags within the 'eplister' div (episodes list)
      episodes = eplister.find_all('li')
    #   episodes = soup.find_all('li')

# Loop through each episode and extract the data
      episode_data = []

      for episode in episodes:
    # Extract the relevant information for each episode
       episode_num = episode.find('div', class_='epl-num').text.strip()
       episode_title = episode.find('div', class_='epl-title').text.strip()
       episode_sub = episode.find('span', class_='status Sub').text.strip() if episode.find('span', class_='status Sub') else 'N/A'
       episode_date = episode.find('div', class_='epl-date').text.strip()
       episode_url = episode.find('a')['href']

    # Store the data as a dictionary
       episode_data.append({
        'episode_number': episode_num,
        'title': episode_title,
        'sub_status': episode_sub,
        'release_date': episode_date,
        'url': episode_url
    })

    # ---------------------------------------- SIMILAR ANIME --------------------------------------------

      s_titles = soup.find_all('h2', {'itemprop': 'headline'})
      s_series = soup.find_all(class_=["typez TV", "typez Movie"])
      s_statuss = soup.find_all(class_="epx")
      s_languages = soup.find_all(class_=["sb Sub", "sb Dub"])
      s_links = soup.find_all("a", class_="tip")

      div_tags = soup.find_all('div', class_='bsx')
      s_img_tags = [div.find_all('img') for div in div_tags]

    # Extract data for similar anime
      for i in range(len(s_titles)):
        similar_title = s_titles[i].get_text().strip().replace("\n", "") if i < len(s_titles) else ""
        similar_series = s_series[i].get_text().strip().replace("\n", "") if i < len(s_series) else "TV"
        similar_status = s_statuss[i].get_text().strip().replace("\n", "") if i < len(s_statuss) else ""
        similar_language = s_languages[i].get_text().strip().replace("\n", "") if i < len(s_languages) else ""

        if i < len(s_img_tags) and len(s_img_tags[i]) > 0:
            similar_img_url = s_img_tags[i][0].get('data-src', '')  # Get the first image in the div
            if not similar_img_url:
                similar_img_url = s_img_tags[i][0].get('src', '')  # Fallback to 'src' if 'data-src' is not present
        else:
            similar_img_url = 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

        similar_href = s_links[i]['href'] if i < len(s_links) and 'href' in s_links[i].attrs else None

        # Append the extracted data to the list as a dictionary
        similar_anime.append({
            'title': similar_title,
            'series': similar_series,
            'status': similar_status,
            'language': similar_language,
            'img': similar_img_url,
            'link': similar_href
        })

    # ---------------------- MAIN ANIME DETAIL ARRAY ------------------------

    # Append the main anime data to the anime_detail list
      anime_detail.append({
        'title': title,
        'status': detail,
        'img': img_url,
        'cover_img': cover_img_url,
        'genres': genres_data,
        'description': description,
        'episodes': episode_data,
        'Similar_Anime_List': similar_anime
    })

else:
     print(f"Failed to fetch page  Status code: {response.status_code}")
     



    # Define the file path and create the 'data' directory if it doesn't exist
data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

json_file_path = os.path.join(data_dir, '9animeDetail.json')
    
    # Overwrite the previous content of the file with new data
with open(json_file_path, "w", encoding="utf-8") as json_file:
     json.dump(anime_detail, json_file, ensure_ascii=False, indent=4)

print("JSON file created/updated successfully.")


    # Close the driver after the operation
    # driver.quit()


#//----------------------------------------------------------------------------------------------------
# 
# 
#     

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

# # Get the base URL from command line argument
# # base_url = sys.argv[1]
# query = sys.argv[1]
# base_url = "https://9anime.org.lv/page/1/?s=attack"
# # Initialize an empty list to store anime details
# search_anime = []

# # Loop through pages 1 to 5
# for page_number in range(1, 6):
#     page_url = base_url.replace('page/1', f'page/{page_number}')
#     final_url = page_url.replace('attack', f'{query}')  # Update the page URL dynamically
#     # print(f"Scraping data from: {page_url}")
#     print(f"Scraping data from: {final_url}")

#     # Send a GET request to the URL
#     # response = requests.get(page_url)
#     response = requests.get(final_url)

#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         html_doc = response.text  # Get the HTML content from the response

#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(html_doc, 'html.parser')

#         # Find all divs that contain anime details
#         popular_divs = soup.find_all('div', class_='bsx')

#         if not popular_divs:
#             print(f"No data found on page {page_number}. Stopping the scraping.")
#             break  # Stop scraping if no data is found

#         # Loop through each div and extract anime details
#         for i in range(len(popular_divs)):
#             show_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#             episode_title = popular_divs[i].find('h2', itemprop='headline').text.strip()
#             image_url = popular_divs[i].find('img')['src']
#             episode_url = popular_divs[i].find('a')['href']
#             episode_number = popular_divs[i].find('span', class_='epx').text.strip()
#             language = popular_divs[i].find('span', class_=['sb Sub', 'sb Dub']).text.strip()
#             series = popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']).text.strip() if popular_divs[i].find('div', class_=['typez TV', 'typez Movie', 'typez Special', 'typez OVA', 'typez ONA']) else "Null"

#             search_anime.append({
#                 'title': show_title,
#                 'episode_title': episode_title,
#                 'img': image_url,
#                 'link': episode_url,
#                 'episode_number': episode_number,
#                 'language': language,
#                 'series': series
#             })
#     else:
#         print(f"Failed to fetch page {page_number}. Status code: {response.status_code}")
#         break  # Stop scraping if page fetch fails
# data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
# if not os.path.exists(data_dir):
#    os.makedirs(data_dir)

# json_file_path = os.path.join(data_dir, '9animeSearch.json')
# # Overwrite the previous content of the file with new data
# with open(json_file_path, "w", encoding="utf-8") as json_file:
#     json.dump(search_anime, json_file, ensure_ascii=False, indent=4)

# print("JSON file created/updated successfully.")