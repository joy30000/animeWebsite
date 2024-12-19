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

    details = soup.find_all(class_="spe")
    detail = str(details[0]) if details else ""
    if detail:
        detail = detail.replace('</span>', '</span><br>')

    div_tag = soup.find('div', class_='thumb')
    img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

    div_tag = soup.find('div', class_='ime')
    cover_img_url = div_tag.find('img').get('src') if div_tag else 'https://png.pngtree.com/thumb_back/fh260/background/20220114/pngtree-no-image-available-available-wooden-blackboard-photo-image_4846882.jpg'

    genres = soup.find_all(class_="genxed")
    genre = str(genres[0]) if genres else ""

    descriptions = soup.find_all(class_="entry-content")
    description = str(descriptions).replace('[', '').replace(']', '')

    episodes = soup.find('div', class_='eplister')
    ul_tag = episodes.find('ul') if episodes else None
    ul_html = str(ul_tag).replace('https:', '/home/anime_episode?url=https:') if ul_tag else "No episodes found"

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
        'genres': genre,
        'description': description,
        'episodes': ul_html,
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

    data_fir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    if not os.path.exists(data_fir):
        os.makedirs(data_fir)
    # Create the HTML file to display the JSON data
    html_file_path = os.path.join(data_fir, '9animeDetailtrial.html')

    # Create HTML content embedding the JSON data
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Anime Details</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                width: 80%;
                margin: 0 auto;
            }}
            h1 {{
                text-align: center;
                margin-top: 20px;
            }}
            .anime-detail {{
                display: flex;
                margin-top: 20px;
            }}
            .anime-detail img {{
                max-width: 300px;
                margin-right: 20px;
            }}
            .anime-detail .content {{
                max-width: 700px;
            }}
            .similar-anime {{
                margin-top: 40px;
            }}
            .similar-anime .anime-card {{
                display: inline-block;
                width: 200px;
                margin: 10px;
                text-align: center;
            }}
            .similar-anime .anime-card img {{
                width: 100%;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Anime Detail</h1>
            <div class="anime-detail" id="anime-detail">
                <!-- Anime details will be inserted here -->
            </div>

            <div class="similar-anime" id="similar-anime">
                <!-- Similar anime will be inserted here -->
            </div>
        </div>

        <script>
            // Fetch the JSON data from the file and display it
            fetch('9animeDetail.json')
                .then(response => response.json())
                .then(data => {{
                    // Display the main anime details
                    const animeDetail = data[0]; // Assuming we have a single anime entry in the array
                    const animeDetailElement = document.getElementById('anime-detail');
                    animeDetailElement.innerHTML = `
                        <img src="${{animeDetail.img}}" alt="${{animeDetail.title}}">
                        <div class="content">
                            <h2>${{animeDetail.title}}</h2>
                            <p><strong>Status:</strong> ${{animeDetail.status}}</p>
                            <p><strong>Genres:</strong> ${{animeDetail.genres}}</p>
                            <p><strong>Description:</strong> ${{animeDetail.description}}</p>
                            <p><strong>Episodes:</strong> ${{animeDetail.episodes}}</p>
                        </div>
                    `;

                    // Display similar anime
                    const similarAnimeElement = document.getElementById('similar-anime');
                    animeDetail.Similar_Anime_List.forEach(similarAnime => {{
                        similarAnimeElement.innerHTML += `
                            <div class="anime-card">
                                <img src="${{similarAnime.img}}" alt="${{similarAnime.title}}">
                                <p>${{similarAnime.title}}</p>
                                <p>${{similarAnime.series}}</p>
                                <p>${{similarAnime.language}}</p>
                            </div>
                        `;
                    }});
                }})
                .catch(error => console.error('Error loading JSON data:', error));
        </script>
    </body>
    </html>
    """

    # Write the HTML content to the file
    with open(html_file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print("HTML file created successfully.")

except Exception as e:
    print(f"Error processing data: {e}")

finally:
    # Close the driver after the operation
    driver.quit()