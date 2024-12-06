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

# Get URL from command line argument
url = sys.argv[1]

# Set up the WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run in headless mode (no UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    html_doc = response.text  # Get the HTML content from the response

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Initialize a list to store the scraped data as dictionaries
    anime_detail = []
    similar_anime = []

    try:
        # Extract all matching elements
        # titles = soup.find_all(class_="entry-title")
        # title = titles[0].get_text().strip().replace("\n", "") if titles else ""


        details = soup.find_all(class_="lm")
        detail = str(details[0]) if details else ""
        if detail:
         detail = detail.replace('<i class="status Sub">Sub</i>', '')

        videos = soup.find_all(class_="video-content")
        video = str(videos[0]) if videos else "Episodes Not Available" 

        servers = soup.find_all(class_="item video-nav")
        server = str(servers[0]) if servers else "Server Not Available" 

        download_links = soup.find_all('a', {'aria-label': 'Download'})

# Convert the first download link to a string (HTML content)
        download_link = str(download_links[0]) if download_links else "Not Available"
        


        # episodes = soup.find_all(id="mainepisode")
        # episode = str(episodes[0]) if episodes else "Episodes Not released Yet"
        # if episode:
        #  episode = episode.replace('class="episodes-ul hidden"', 'class="episodes-ul"')
         
    
        # div_tag = soup.find('div', class_='thumb')
        # img_tag = div_tag.find('img')  # Finds the first <img> tag inside the div
        # if img_tag:
        #  img_url = img_tag.get('src')  
        # else:
        #  img_url='https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg' 
       

        # div_tag = soup.find('div', class_='ime')
        # cover_img_tag = div_tag.find('img') 
        # if cover_img_tag:
        #  cover_img_url = cover_img_tag.get('src')  
        # else:
        #  cover_img_url='https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'  


        # genres = soup.find_all(class_="genxed")
        # genre= str(genres[0]) if genres else "" 


        # descriptions = soup.find_all(class_="entry-content")
        # description=str(descriptions)
        # description = description.replace('[', '').replace(']', '')


        # episodes = soup.find('div', class_='eplister')
        # ul_tag = episodes.find('ul') if episodes else None 
        # if ul_tag:
        #  ul_html = str(ul_tag)  
        # else:
        #  print("No <ul> found inside the 'eplister' div.")


        

       


        



        
       

        #---------------------------------------- SIMILAR ANIME --------------------------------------------#
        
        # s_titles = soup.find_all('h2', {'itemprop': 'headline'})
        # s_series = soup.find_all(class_=["typez TV", "typez Movie"])
        # s_statuss = soup.find_all(class_="epx")
        # s_languages = soup.find_all(class_=["sb Sub", "sb Dub"])
        # s_links = soup.find_all("a", class_="tip")

        # div_tags = soup.find_all('div', class_='bsx')
        # s_img_tags = [div.find_all('img') for div in div_tags]


        # # # Extract data for similar anime
        # for i in range(len(s_titles)):
        #     similar_title = s_titles[i].get_text().strip().replace("\n", "") if i < len(s_titles) else ""
        #     similar_series = s_series[i].get_text().strip().replace("\n", "") if i < len(s_series) else "TV"
        #     similar_status = s_statuss[i].get_text().strip().replace("\n", "") if i < len(s_statuss) else ""
            
        #     similar_language = s_languages[i].get_text().strip().replace("\n", "") if i < len(s_languages) else ""

    
        #     if i < len(s_img_tags) and len(s_img_tags[i]) > 0:
        #     # For each div, we need to check if the image has the 'data-src' attribute
        #      similar_img_url = s_img_tags[i][0].get('data-src', '')  # Get the first image in the div
        #     if not similar_img_url:
        #      similar_img_url = s_img_tags[i][0].get('src', '')  # Fallback to 'src' if 'data-src' is not present
        #     else:
        #      similar_img_url = 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'  # Default image URL

        #     similar_href = s_links[i]['href'] if i < len(s_links) and 'href' in s_links[i].attrs else None
       

        #     # Append the extracted data to the list as a dictionary
        #     similar_anime.append({
        #         'title': similar_title,
        #         'series': similar_series,
        #         'status': similar_status,
        #         'language': similar_language,
        #         'img': similar_img_url,
        #         'link': similar_href
        #     })


#----------------------  MAIN ANIME DETAIL ARRAY-----------------------------------------------------------------
            
         # Append the main anime data to the anime_detail list
        anime_detail.append({
            # 'title': title,
            'status': detail,
            'video_src':video,
            'server': server,
            'download_link': download_link
            # 'img': img_url,
            # 'cover_img': cover_img_url,
            # 'genres': genre,
            # 'description': description,
            # 'episodes': episode
            # 'Similar_Anime_List': similar_anime
        })

        json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeEpisodePage.json')
        # Save the data as JSON with proper formatting
        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(anime_detail, json_file, ensure_ascii=False, indent=4)

        print("JSON file created successfully.")

    except Exception as e:
        print(f"Error processing data: {e}")

else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")