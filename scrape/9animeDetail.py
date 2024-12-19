
# import sys
# import os
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # Check if URL is passed as an argument
# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)

# # Get URL from command line argument
# url = sys.argv[1]

# # Set up the WebDriver options
# options = Options()
# options.add_argument("--headless")  # run in headless mode (no UI)
# options.add_argument("--no-sandbox")  # To run in restricted environments like Render
# options.add_argument("--disable-dev-shm-usage")  # To fix Chrome crash issues on limited memory
# options.add_argument("--disable-gpu")  # Disable GPU acceleration (not needed in headless mode)
# options.add_argument("--remote-debugging-port=9222")  # Optional: for debugging in Render

# chrome_binary_path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome"
# # Specify the Chrome binary location for Render environment
# # options.binary_location = "/usr/bin/chromium"  # This is the path where Chrome is usually located in cloud environments like Render
# options.binary_location = chrome_binary_path
# # Set up the WebDriver with ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Use Selenium to get the page content
# driver.get(url)

# # Wait for the page to load (adjust the wait time as per the website's load time)
# try:
#     # Wait for a specific element to be loaded (use a class or tag that will be present when the page is ready)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "entry-title")))
#     print("Page loaded successfully.")
# except Exception as e:
#     print(f"Error waiting for page to load: {e}")
#     driver.quit()
#     sys.exit(1)

# # Get the HTML content of the page
# html_doc = driver.page_source

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')

# # Initialize lists to store the scraped data
# anime_detail = []
# similar_anime = []

# try:
#     # Extract basic anime details
#     titles = soup.find_all(class_="entry-title")
#     title = titles[0].get_text().strip().replace("\n", "") if titles else ""

#     details = soup.find_all(class_="spe")
#     detail = str(details[0]) if details else ""
#     if detail:
#         detail = detail.replace('</span>', '</span><br>')

#     div_tag = soup.find('div', class_='thumb')
#     img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#     div_tag = soup.find('div', class_='ime')
#     cover_img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#     genres = soup.find_all(class_="genxed")
#     genre = str(genres[0]) if genres else ""

#     descriptions = soup.find_all(class_="entry-content")
#     description = str(descriptions).replace('[', '').replace(']', '')

#     episodes = soup.find('div', class_='eplister')
#     ul_tag = episodes.find('ul') if episodes else None
#     ul_html = str(ul_tag).replace('https:', '/home/anime_episode?url=https:') if ul_tag else "No episodes found"

#     # ---------------------------------------- SIMILAR ANIME --------------------------------------------

#     s_titles = soup.find_all('h2', {'itemprop': 'headline'})
#     s_series = soup.find_all(class_=["typez TV", "typez Movie"])
#     s_statuss = soup.find_all(class_="epx")
#     s_languages = soup.find_all(class_=["sb Sub", "sb Dub"])
#     s_links = soup.find_all("a", class_="tip")

#     div_tags = soup.find_all('div', class_='bsx')
#     s_img_tags = [div.find_all('img') for div in div_tags]

#     # Extract data for similar anime
#     for i in range(len(s_titles)):
#         similar_title = s_titles[i].get_text().strip().replace("\n", "") if i < len(s_titles) else ""
#         similar_series = s_series[i].get_text().strip().replace("\n", "") if i < len(s_series) else "TV"
#         similar_status = s_statuss[i].get_text().strip().replace("\n", "") if i < len(s_statuss) else ""
#         similar_language = s_languages[i].get_text().strip().replace("\n", "") if i < len(s_languages) else ""

#         if i < len(s_img_tags) and len(s_img_tags[i]) > 0:
#             similar_img_url = s_img_tags[i][0].get('data-src', '')  # Get the first image in the div
#             if not similar_img_url:
#                 similar_img_url = s_img_tags[i][0].get('src', '')  # Fallback to 'src' if 'data-src' is not present
#         else:
#             similar_img_url = 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#         similar_href = s_links[i]['href'] if i < len(s_links) and 'href' in s_links[i].attrs else None

#         # Append the extracted data to the list as a dictionary
#         similar_anime.append({
#             'title': similar_title,
#             'series': similar_series,
#             'status': similar_status,
#             'language': similar_language,
#             'img': similar_img_url,
#             'link': similar_href
#         })

#     # ---------------------- MAIN ANIME DETAIL ARRAY ------------------------

#     # Append the main anime data to the anime_detail list
#     anime_detail.append({
#         'title': title,
#         'status': detail,
#         'img': img_url,
#         'cover_img': cover_img_url,
#         'genres': genre,
#         'description': description,
#         'episodes': ul_html,
#         'Similar_Anime_List': similar_anime
#     })

#     # Define the file path and create the 'data' directory if it doesn't exist
#     # data_dir = '/opt/render/project/src/data'  # Absolute path for Render's environment
#     data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
#     if not os.path.exists(data_dir):
#         os.makedirs(data_dir)

#     json_file_path = os.path.join(data_dir, '9animeDetail.json')

#     # Overwrite the previous content of the file with new data
#     with open(json_file_path, "w", encoding="utf-8") as json_file:
#         json.dump(anime_detail, json_file, ensure_ascii=False, indent=4)

#     print("JSON file created/updated successfully.")

# except Exception as e:
#     print(f"Error processing data: {e}")

# finally:
#     # Close the driver after the operation
#     driver.quit()




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







import sys
import os
import json
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
options = Options()
options.add_argument("--headless")  # run in headless mode (no UI)
options.add_argument("--no-sandbox")  # To run in restricted environments like Render
options.add_argument("--disable-dev-shm-usage")  # To fix Chrome crash issues on limited memory
options.add_argument("--disable-gpu")  # Disable GPU acceleration (not needed in headless mode)

# Set up the WebDriver with ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Use Selenium to get the page content
driver.get(url)

# Wait for the page to load (you may adjust the sleep time based on the website's loading time)
time.sleep(3)  # Wait for JavaScript to load the content

# Get the HTML content of the page
html_doc = driver.page_source

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Initialize lists to store the scraped data
anime_detail = []
similar_anime = []

try:
    # Extract basic anime details
    titles = soup.find_all(class_="entry-title")
    title = titles[0].get_text().strip().replace("\n", "") if titles else ""

    # details = soup.find_all(class_="spe")
    # detail = str(details[0]) if details else ""
    # if detail:
    #     detail = detail.replace('</span>', '</span><br>')

    div_tag = soup.find('div', class_='thumb')
    img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

    div_tag = soup.find('div', class_='ime')
    cover_img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

    # genres = soup.find_all(class_="genxed")
    # genre = str(genres[0]) if genres else ""

    # descriptions = soup.find_all(class_="entry-content")
    # description = str(descriptions).replace('[', '').replace(']', '')

    # episodes = soup.find('div', class_='eplister')
    # ul_tag = episodes.find('ul') if episodes else None
    # ul_html = str(ul_tag).replace('https:', '/home/anime_episode?url=https:') if ul_tag else "No episodes found"

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
        # 'status': detail,
        'img': img_url,
        'cover_img': cover_img_url,
        # 'genres': genre,
        # 'description': description,
        # 'episodes': ul_html,
        'Similar_Anime_List': similar_anime
    })

    # Define the file path and create the 'data' directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    json_file_path = os.path.join(data_dir, '9animeDetail.json')
    
    # Overwrite the previous content of the file with new data
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(anime_detail, json_file, ensure_ascii=False, indent=4)

    print("JSON file created/updated successfully.")

except Exception as e:
    print(f"Error processing data: {e}")

finally:
    # Close the driver after the operation
    driver.quit()









# import sys
# import os
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # Check if URL is passed as an argument
# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)

# # Get URL from command line argument
# url = sys.argv[1]

# # Set up the WebDriver options
# options = Options()
# options.add_argument("--headless")  # run in headless mode (no UI)
# options.add_argument("--no-sandbox")  # To run in restricted environments like Render
# options.add_argument("--disable-dev-shm-usage")  # To fix Chrome crash issues on limited memory
# options.add_argument("--disable-gpu")  # Disable GPU acceleration (not needed in headless mode)
# options.add_argument("--remote-debugging-port=9222")  # Optional: for debugging in Render

# # Set up the WebDriver with ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Use Selenium to get the page content
# driver.get(url)

# # Wait for the page to load (adjust the wait time as per the website's load time)
# try:
#     # Wait for a specific element to be loaded (use a class or tag that will be present when the page is ready)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "entry-title")))
#     print("Page loaded successfully.")
# except Exception as e:
#     print(f"Error waiting for page to load: {e}")
#     driver.quit()
#     sys.exit(1)

# # Get the HTML content of the page
# html_doc = driver.page_source

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')

# # Initialize lists to store the scraped data
# anime_detail = []
# similar_anime = []

# try:
#     # Extract basic anime details
#     titles = soup.find_all(class_="entry-title")
#     title = titles[0].get_text().strip().replace("\n", "") if titles else ""

#     details = soup.find_all(class_="spe")
#     detail = str(details[0]) if details else ""
#     if detail:
#         detail = detail.replace('</span>', '</span><br>')

#     div_tag = soup.find('div', class_='thumb')
#     img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#     div_tag = soup.find('div', class_='ime')
#     cover_img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#     genres = soup.find_all(class_="genxed")
#     genre = str(genres[0]) if genres else ""

#     descriptions = soup.find_all(class_="entry-content")
#     description = str(descriptions).replace('[', '').replace(']', '')

#     episodes = soup.find('div', class_='eplister')
#     ul_tag = episodes.find('ul') if episodes else None
#     ul_html = str(ul_tag).replace('https:', '/home/anime_episode?url=https:') if ul_tag else "No episodes found"

#     # ---------------------------------------- SIMILAR ANIME --------------------------------------------

#     s_titles = soup.find_all('h2', {'itemprop': 'headline'})
#     s_series = soup.find_all(class_=["typez TV", "typez Movie"])
#     s_statuss = soup.find_all(class_="epx")
#     s_languages = soup.find_all(class_=["sb Sub", "sb Dub"])
#     s_links = soup.find_all("a", class_="tip")

#     div_tags = soup.find_all('div', class_='bsx')
#     s_img_tags = [div.find_all('img') for div in div_tags]

#     # Extract data for similar anime
#     for i in range(len(s_titles)):
#         similar_title = s_titles[i].get_text().strip().replace("\n", "") if i < len(s_titles) else ""
#         similar_series = s_series[i].get_text().strip().replace("\n", "") if i < len(s_series) else "TV"
#         similar_status = s_statuss[i].get_text().strip().replace("\n", "") if i < len(s_statuss) else ""
#         similar_language = s_languages[i].get_text().strip().replace("\n", "") if i < len(s_languages) else ""

#         if i < len(s_img_tags) and len(s_img_tags[i]) > 0:
#             similar_img_url = s_img_tags[i][0].get('data-src', '')  # Get the first image in the div
#             if not similar_img_url:
#                 similar_img_url = s_img_tags[i][0].get('src', '')  # Fallback to 'src' if 'data-src' is not present
#         else:
#             similar_img_url = 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#         similar_href = s_links[i]['href'] if i < len(s_links) and 'href' in s_links[i].attrs else None

#         # Append the extracted data to the list as a dictionary
#         similar_anime.append({
#             'title': similar_title,
#             'series': similar_series,
#             'status': similar_status,
#             'language': similar_language,
#             'img': similar_img_url,
#             'link': similar_href
#         })

#     # ---------------------- MAIN ANIME DETAIL ARRAY ------------------------

#     # Append the main anime data to the anime_detail list
#     anime_detail.append({
#         'title': title,
#         'status': detail,
#         'img': img_url,
#         'cover_img': cover_img_url,
#         'genres': genre,
#         'description': description,
#         'episodes': ul_html,
#         'Similar_Anime_List': similar_anime
#     })

#     # Define the file path and create the 'data' directory if it doesn't exist
#     # data_dir = '/opt/render/project/src/data'  # Absolute path for Render's environment
#     data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
#     if not os.path.exists(data_dir):
#         os.makedirs(data_dir)

#     json_file_path = os.path.join(data_dir, '9animeDetail.json')

#     # Overwrite the previous content of the file with new data
#     with open(json_file_path, "w", encoding="utf-8") as json_file:
#         json.dump(anime_detail, json_file, ensure_ascii=False, indent=4)

#     print("JSON file created/updated successfully.")

# except Exception as e:
#     print(f"Error processing data: {e}")

# finally:
#     # Close the driver after the operation
#     driver.quit()




# import sys
# import os
# import json
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from bs4 import BeautifulSoup

# # Check if URL is passed as an argument
# if len(sys.argv) < 2:
#     print("Usage: python script.py <URL>")
#     sys.exit(1)

# # Get URL from command line argument
# url = sys.argv[1]

# # Set up the WebDriver options
# options = Options()
# options.add_argument("--headless")  # run in headless mode (no UI)
# options.add_argument("--no-sandbox")  # To run in restricted environments like Render
# options.add_argument("--disable-dev-shm-usage")  # To fix Chrome crash issues on limited memory
# options.add_argument("--disable-gpu")  # Disable GPU acceleration (not needed in headless mode)
# options.add_argument("--remote-debugging-port=9222")  # Optional: for debugging in Render

# # Explicitly set the path to the Chrome binary
# options.binary_location = "/usr/bin/google-chrome-stable"  # Update this path if necessary

# # Set up the WebDriver with ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Use Selenium to get the page content
# driver.get(url)

# # Wait for the page to load (adjust the wait time as per the website's load time)
# try:
#     # Wait for a specific element to be loaded (use a class or tag that will be present when the page is ready)
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "entry-title")))

#     print("Page loaded successfully.")
# except Exception as e:
#     print(f"Error waiting for page to load: {e}")
#     driver.quit()
#     sys.exit(1)

# # Get the HTML content of the page
# html_doc = driver.page_source

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(html_doc, 'html.parser')

# # Initialize lists to store the scraped data
# anime_detail = []
# similar_anime = []

# try:
#     # Extract basic anime details
#     titles = soup.find_all(class_="entry-title")
#     title = titles[0].get_text().strip().replace("\n", "") if titles else ""

#     details = soup.find_all(class_="spe")
#     detail = str(details[0]) if details else ""
#     if detail:
#         detail = detail.replace('</span>', '</span><br>')

#     div_tag = soup.find('div', class_='thumb')
#     img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#     div_tag = soup.find('div', class_='ime')
#     cover_img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#     genres = soup.find_all(class_="genxed")
#     genre = str(genres[0]) if genres else ""

#     descriptions = soup.find_all(class_="entry-content")
#     description = str(descriptions).replace('[', '').replace(']', '')

#     episodes = soup.find('div', class_='eplister')
#     ul_tag = episodes.find('ul') if episodes else None
#     ul_html = str(ul_tag).replace('https:', '/home/anime_episode?url=https:') if ul_tag else "No episodes found"

#     # Extract similar anime details
#     s_titles = soup.find_all('h2', {'itemprop': 'headline'})
#     s_series = soup.find_all(class_=["typez TV", "typez Movie"])
#     s_statuss = soup.find_all(class_="epx")
#     s_languages = soup.find_all(class_=["sb Sub", "sb Dub"])
#     s_links = soup.find_all("a", class_="tip")

#     div_tags = soup.find_all('div', class_='bsx')
#     s_img_tags = [div.find_all('img') for div in div_tags]

#     for i in range(len(s_titles)):
#         similar_title = s_titles[i].get_text().strip().replace("\n", "") if i < len(s_titles) else ""
#         similar_series = s_series[i].get_text().strip().replace("\n", "") if i < len(s_series) else "TV"
#         similar_status = s_statuss[i].get_text().strip().replace("\n", "") if i < len(s_statuss) else ""
#         similar_language = s_languages[i].get_text().strip().replace("\n", "") if i < len(s_languages) else ""

#         if i < len(s_img_tags) and len(s_img_tags[i]) > 0:
#             similar_img_url = s_img_tags[i][0].get('data-src', '')  # Get the first image in the div
#             if not similar_img_url:
#                 similar_img_url = s_img_tags[i][0].get('src', '')  # Fallback to 'src' if 'data-src' is not present
#         else:
#             similar_img_url = 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

#         similar_href = s_links[i]['href'] if i < len(s_links) and 'href' in s_links[i].attrs else None

#         similar_anime.append({
#             'title': similar_title,
#             'series': similar_series,
#             'status': similar_status,
#             'language': similar_language,
#             'img': similar_img_url,
#             'link': similar_href
#         })

#     # Append the main anime data to the anime_detail list
#     anime_detail.append({
#         'title': title,
#         'status': detail,
#         'img': img_url,
#         'cover_img': cover_img_url,
#         'genres': genre,
#         'description': description,
#         'episodes': ul_html,
#         'Similar_Anime_List': similar_anime
#     })

#     # Define the file path and create the 'data' directory if it doesn't exist
#     data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
#     if not os.path.exists(data_dir):
#         os.makedirs(data_dir)

#     json_file_path = os.path.join(data_dir, '9animeDetail.json')

#     # Overwrite the previous content of the file with new data
#     with open(json_file_path, "w", encoding="utf-8") as json_file:
#         json.dump(anime_detail, json_file, ensure_ascii=False, indent=4)

#     print("JSON file created/updated successfully.")

# except Exception as e:
#     print(f"Error processing data: {e}")

# finally:
#     # Close the driver after the operation
#     driver.quit()