# routes/home.py
from flask import Flask,Blueprint,request,render_template, json
import subprocess
import os
import logging
# Setup basic logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# Create a Blueprint for homeRoutes
homeRoutes = Blueprint('home', __name__)

# Define routes inside the Blueprint
@homeRoutes.route('/')
def home():
    # Load the JSON data from the homepage.json file
    # with open(os.path.join(os.getcwd(), '9animeHomepage.json'), 'r', encoding='utf-8') as f:
    #     homepage_data = json.load(f)
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeHomePage.json')
    print(f"JSON file path: {json_file_path}")
    print(f"Resolved JSON file path: {json_file_path}")
    # Load the JSON data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        homepage_data = json.load(f)

    # Render the Jinja2 template (homepage.html) and pass the JSON data
    return render_template('9animeHomepage.html', homepageData=homepage_data)



# @homeRoutes.route('/anime_detail')
# def anime_detail():
#     anime_url = request.args.get('url')
    
#     # Log the captured URL
#     app.logger.debug(f"Anime URL from query parameter: {anime_url}")
#     # Load the JSON data from the homepage.json file
#     with open(os.path.join(os.getcwd(), '9animeDetail.json'), 'r', encoding='utf-8') as f:
#         homepage_data = json.load(f)
#     # Render the Jinja2 template (homepage.html) and pass the JSON data
#     return render_template('9animeDetail.html', animeDetailData=homepage_data)
    

@homeRoutes.route('/anime_detail')
def anime_detail():
    # Step 1: Get the URL from query string
    anime_url = request.args.get('url')
    
    # Step 2: Log the URL (optional for debugging)
    app.logger.debug(f"Anime URL from query parameter: {anime_url}")
    
    if not anime_url:
        return "No URL provided", 400

    # Step 3: Run the 9animeDetail.py script with the URL as an argument
    # You should pass the URL as an argument to the script
    try:
        result = subprocess.run(
            ['python', '9animeDetail.py', anime_url],
            capture_output=True, text=True, check=True
        )
        # Log any output from the script
        app.logger.debug(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Error running 9animeDetail.py: {e}")
        return "Error generating anime details", 500

    # Step 4: Read the generated JSON file (9animeDetail.json)
    json_file_path = os.path.join(os.getcwd(), '9animeDetail.json')
    
    if not os.path.exists(json_file_path):
        app.logger.error(f"Generated JSON file not found: {json_file_path}")
        return "Error: JSON file not found", 500

    with open(json_file_path, 'r', encoding='utf-8') as f:
        anime_detail_data = json.load(f)

    # Step 5: Pass the JSON data to the template
    return render_template('9animeDetail.html', animeDetailData=anime_detail_data)



# @homeRoutes.route('/animeEp')
# def animeEp():
#     # Load the JSON data from the homepage.json file
#     with open(os.path.join(os.getcwd(), '9animeEpisodePage.json'), 'r', encoding='utf-8') as f:
#         animeEpData = json.load(f)
#     # Render the Jinja2 template (homepage.html) and pass the JSON data
#     return render_template('trialPageEp.html', animeDetailData=animeEpData)


@homeRoutes.route('/anime_episode')
def anime_ep():
    # Step 1: Get the URL from query string
    anime_url = request.args.get('url')
    
    # Step 2: Log the URL (optional for debugging)
    app.logger.debug(f"Anime URL from query parameter: {anime_url}")
    
    if not anime_url:
        return "No URL provided", 400

    # Step 3: Run the 9animeDetail.py script with the URL as an argument
    # You should pass the URL as an argument to the script
    try:
        result = subprocess.run(
            ['python', '9animeEpisodePage.py', anime_url],
            capture_output=True, text=True, check=True
        )
        # Log any output from the script
        app.logger.debug(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Error running 9animeDetail.py: {e}")
        return "Error generating anime details", 500

    # Step 4: Read the generated JSON file (9animeDetail.json)
    json_file_path = os.path.join(os.getcwd(), '9animeEpisodePage.json')
    
    if not os.path.exists(json_file_path):
        app.logger.error(f"Generated JSON file not found: {json_file_path}")
        return "Error: JSON file not found", 500

    with open(json_file_path, 'r', encoding='utf-8') as f:
        anime_episode_data = json.load(f)

    # Step 5: Pass the JSON data to the template
    return render_template('trialPageEp.html', animeEpisodeData=anime_episode_data)



@homeRoutes.route('/search',methods=['POST'])
def search():
    name = request.form.get('name')
    modified_name = name.replace(" ", "+")

    try:
        result = subprocess.run(
            ['python', 'search.py', modified_name],
            capture_output=True, text=True, check=True
        )
        # Log any output from the script
        app.logger.debug(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Error running 9animeDetail.py: {e}")
        return "Error generating anime details", 500

    # Step 4: Read the generated JSON file (9animeDetail.json)
    json_file_path = os.path.join(os.getcwd(), '9animeEpisodePage.json')
    
    if not os.path.exists(json_file_path):
        app.logger.error(f"Generated JSON file not found: {json_file_path}")
        return "Error: JSON file not found", 500
    
    #return f"Name: {modified_name}"
     # Load the JSON data from the homepage.json file
    with open(os.path.join(os.getcwd(), '9animeSearch.json'), 'r', encoding='utf-8') as f:
        search_data = json.load(f)
    # Render the Jinja2 template (homepage.html) and pass the JSON data
    return render_template('9animeSearchResult.html', searchData=search_data, search_query=name)



@homeRoutes.route('/trial')
def trialSearch():
    # Load the JSON data from the homepage.json file
    with open(os.path.join(os.getcwd(), '9animeSearch.json'), 'r', encoding='utf-8') as f:
        search_data = json.load(f)
    # Render the Jinja2 template (homepage.html) and pass the JSON data
    return render_template('9animeSearchResult.html', searchData=search_data)


@homeRoutes.route('/trialCat')
def trialCategory():
    anime_cat = request.args.get('category')
    
    # Step 2: Log the URL (optional for debugging)
    app.logger.debug(f"Anime URL from query parameter: {anime_cat}")
    # Load the JSON data from the homepage.json file
    with open(os.path.join(os.getcwd(), '9animeHomePage.json'), 'r', encoding='utf-8') as f:
        homepage_data = json.load(f)
    # Render the Jinja2 template (homepage.html) and pass the JSON data
    return render_template('9animeCategory.html', homepageData=homepage_data, anime_category=anime_cat)

    
