# routes/home.py
from flask import Flask,Blueprint,request,render_template, json,jsonify
from flask_cors import CORS
from flask_cors import cross_origin
import subprocess
import os
import logging
# Setup basic logging
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
CORS(app) 
# Create a Blueprint for homeRoutes
homeRoutes = Blueprint('home', __name__)

# Define routes inside the Blueprint
@homeRoutes.route('/', methods=['GET'])
@cross_origin()  # Enable CORS only for this route
def home():
    # Load the JSON data from the homepage.json file
    # with open(os.path.join(os.getcwd(), '9animeHomepage.json'), 'r', encoding='utf-8') as f:
    #     homepage_data = json.load(f)
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeHomePage.json')
    # print(f"JSON file path: {json_file_path}")
    # print(f"Resolved JSON file path: {json_file_path}")
    # Load the JSON data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        homepage_data = json.load(f)

    return jsonify(homepage_data)    

    # Render the Jinja2 template (homepage.html) and pass the JSON data
    # return render_template('9animeHomepage.html', homepageData=homepage_data)


#     return render_template('9animeDetail.html', animeDetailData=homepage_data)
    

#---------------------------------------------------------------
# @homeRoutes.route('/anime_detail', methods=['GET'])
# @cross_origin()  # Enable CORS only for this route
# def anime_detail():
#     # Load the JSON data from the homepage.json file
#     # with open(os.path.join(os.getcwd(), '9animeHomepage.json'), 'r', encoding='utf-8') as f:
#     #     homepage_data = json.load(f)
#     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeDetail.json')
#     # print(f"JSON file path: {json_file_path}")
#     # print(f"Resolved JSON file path: {json_file_path}")
#     # Load the JSON data
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#        anime_detail_data = json.load(f)

#     return jsonify(anime_detail_data)   




# @homeRoutes.route('/anime_detail', methods=['GET'])
# @cross_origin()  # Enable CORS only for this route
# def anime_detail():
#     # Load the JSON data from the homepage.json file
#     # with open(os.path.join(os.getcwd(), '9animeHomepage.json'), 'r', encoding='utf-8') as f:
#     #     homepage_data = json.load(f)
#     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeDetail.json')
#     # print(f"JSON file path: {json_file_path}")
#     # print(f"Resolved JSON file path: {json_file_path}")
#     # Load the JSON data
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#        anime_detail_data = json.load(f)

#     return jsonify(anime_detail_data) 



#---------------------------------------------------------------
# @homeRoutes.route('/anime_episode', methods=['GET'])
# @cross_origin()  # Enable CORS only for this route
# def anime_episode():
#     # Load the JSON data from the homepage.json file
#     # with open(os.path.join(os.getcwd(), '9animeHomepage.json'), 'r', encoding='utf-8') as f:
#     #     homepage_data = json.load(f)
#     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeEpisodePage.json')
#     # print(f"JSON file path: {json_file_path}")
#     # print(f"Resolved JSON file path: {json_file_path}")
#     # Load the JSON data
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#        anime_episode_data = json.load(f)

#     return jsonify(anime_episode_data)  












@homeRoutes.route('/anime_detail',methods=['GET'])
@cross_origin()  # Enable CORS only for this route

def anime_detail():
    # Step 1: Get the URL from query string
    anime_url = request.args.get('url')
    # anime_url = request.headers.get('url')
    # data = request.get_json()  # Get the JSON data from the request body
    # anime_url= data.get('category')
    
    # Step 2: Log the URL (optional for debugging)
    app.logger.debug(f"Anime URL from query parameter: {anime_url}")
    
    if not anime_url:
        return "No URL provided", 400

    # Step 3: Run the 9animeDetail.py script with the URL as an argument
    # You should pass the URL as an argument to the script
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'scrape', '9animeDetail.py')
  

    try:
        result = subprocess.run(
        ['python', json_file_path, anime_url],
        capture_output=True, text=True, check=True
        )
    # Log any output from the script
        app.logger.debug(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
     app.logger.error(f"Error running 9animeDetail.py: {e}")
     app.logger.error(f"stderr: {e.stderr}")  # Log stderr for more details
     return "Error generating anime details", 500
   

    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeDetail.json')
  
    # Load the JSON data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        anime_detail_data = json.load(f)
        

    # Step 5: Pass the JSON data to the template
    #return render_template('9animeDetail.html', animeDetailData=anime_detail_data)
    return jsonify(anime_detail_data) 




@homeRoutes.route('/anime_shounene',methods=['GET'])
@cross_origin()  # Enable CORS only for this route

def anime_shounene():
    # Step 1: Get the URL from query string
    anime_url = request.args.get('url')
    # anime_url = request.headers.get('url')
    # data = request.get_json()  # Get the JSON data from the request body
    # anime_url= data.get('category')
    
    # Step 2: Log the URL (optional for debugging)
    app.logger.debug(f"Anime URL from query parameter: {anime_url}")
    
    if not anime_url:
        return "No URL provided", 400

    # Step 3: Run the 9animeDetail.py script with the URL as an argument
    # You should pass the URL as an argument to the script
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'scrape', '9animeShounene.py')
  

    try:
        result = subprocess.run(
        ['python', json_file_path, anime_url],
        capture_output=True, text=True, check=True
        )
    # Log any output from the script
        app.logger.debug(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
     app.logger.error(f"Error running 9animeShounene.py: {e}")
     app.logger.error(f"stderr: {e.stderr}")  # Log stderr for more details
     return "Error generating anime details", 500
   

    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeShounene.json')
  
    # Load the JSON data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        anime_shounene_data = json.load(f)
        

    # Step 5: Pass the JSON data to the template
    #return render_template('9animeDetail.html', animeDetailData=anime_detail_data)
    return jsonify(anime_shounene_data) 





@homeRoutes.route('/anime_episode',methods=['GET'])
@cross_origin()  # Enable CORS only for this route

def anime_episode():
    # Step 1: Get the URL from query string
    anime_url = request.args.get('url')
    # anime_url = request.headers.get('url')
    # data = request.get_json()  # Get the JSON data from the request body
    # anime_url= data.get('category')
    
    # Step 2: Log the URL (optional for debugging)
    app.logger.debug(f"Anime URL from query parameter: {anime_url}")
    
    if not anime_url:
        return "No URL provided", 400

    # Step 3: Run the 9animeDetail.py script with the URL as an argument
    # You should pass the URL as an argument to the script
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'scrape', '9animeEpisodePage.py')
  

    try:
        result = subprocess.run(
        ['python', json_file_path, anime_url],
        capture_output=True, text=True, check=True
        )
    # Log any output from the script
        app.logger.debug(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
     app.logger.error(f"Error running 9animeDetail.py: {e}")
     app.logger.error(f"stderr: {e.stderr}")  # Log stderr for more details
     return "Error generating anime details", 500
   

    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeEpisodePage.json')
  
    # Load the JSON data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        anime_episode_data = json.load(f)

    # Step 5: Pass the JSON data to the template
    #return render_template('9animeDetail.html', animeDetailData=anime_detail_data)
    return jsonify(anime_episode_data) 




# @homeRoutes.route('/anime_episode',methods=['GET'])
# @cross_origin()
# def anime_ep():
#     # Step 1: Get the URL from query string
#     anime_url = request.args.get('url')
    
#     # Step 2: Log the URL (optional for debugging)
#     app.logger.debug(f"Anime URL from query parameter: {anime_url}")
    
#     if not anime_url:
#         return "No URL provided", 400

#     # Step 3: Run the 9animeDetail.py script with the URL as an argument
#     # You should pass the URL as an argument to the script
#     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'scrape', '9animeEpisodePage.py')
#     try:
#         result = subprocess.run(
#             ['python', json_file_path, anime_url],
#             capture_output=True, text=True, check=True
#         )
#         # Log any output from the script
#         app.logger.debug(f"Script output: {result.stdout}")
#     except subprocess.CalledProcessError as e:
#         app.logger.error(f"Error running 9animeDetail.py: {e}")
#         return "Error generating anime details", 500

#     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeEpisodePage.json')

#     # Load the JSON data
#     with open(json_file_path, 'r', encoding='utf-8') as f:
#         anime_episode_data = json.load(f)

#     # Step 5: Pass the JSON data to the template
#     return render_template('trialPageEp.html', animeEpisodeData=anime_episode_data)

#-----------------------------------------------------------------------------------------

@homeRoutes.route('/search',methods=['GET'])
@cross_origin()  # Enable CORS only for this route
def search():
    name = request.args.get('name')
    if not name:
     #app.logger.error("Search query 'name' is missing.")
     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeSearch.json')
    # print(f"JSON file path: {json_file_path}")
    # print(f"Resolved JSON file path: {json_file_path}")
    # Load the JSON data
     with open(json_file_path, 'r', encoding='utf-8') as f:
        search_data = json.load(f)

     return jsonify(search_data) 
    # return "Error: Missing search query", 400

    # modified_name = name.replace(" ", "+")
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'scrape', 'search.py')
    try:
        result = subprocess.run(
            ['python', json_file_path, name],
            capture_output=True, text=True, check=True
        )
        # Log any output from the script
        app.logger.debug(f"Script output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Error running search.py: {e}")
        return "Error generating anime details", 500

  
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeSearch.json')


     # Load the JSON data from the homepage.json file
    with open(os.path.join(os.getcwd(), json_file_path), 'r', encoding='utf-8') as f:
        search_data = json.load(f)
    # Render the Jinja2 template (homepage.html) and pass the JSON data
    # return render_template('9animeSearchResult.html', searchData=search_data, search_query=name)
    return jsonify(search_data) 

#---------------------------------------------------------------------------------------------------------

# @homeRoutes.route('/search',methods=['POST'])
# def search():
#     name = request.form.get('name')
#     modified_name = name.replace(" ", "+")
#     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'scrape', 'search.py')
#     try:
#         result = subprocess.run(
#             ['python', json_file_path, modified_name],
#             capture_output=True, text=True, check=True
#         )
#         # Log any output from the script
#         app.logger.debug(f"Script output: {result.stdout}")
#     except subprocess.CalledProcessError as e:
#         app.logger.error(f"Error running search.py: {e}")
#         return "Error generating anime details", 500

  
#     json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeSearch.json')


#      # Load the JSON data from the homepage.json file
#     with open(os.path.join(os.getcwd(), json_file_path), 'r', encoding='utf-8') as f:
#         search_data = json.load(f)
#     # Render the Jinja2 template (homepage.html) and pass the JSON data
#     return render_template('9animeSearchResult.html', searchData=search_data, search_query=name)



@homeRoutes.route('/trial')
def trialSearch():
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeSearch.json')
    # Load the JSON data from the homepage.json file
    with open(os.path.join(os.getcwd(), json_file_path), 'r', encoding='utf-8') as f:
        search_data = json.load(f)
    # Render the Jinja2 template (homepage.html) and pass the JSON data
    return render_template('9animeSearchResult.html', searchData=search_data)


@homeRoutes.route('/trialCat')
def trialCategory():
    anime_cat = request.args.get('category')
    
    # Step 2: Log the URL (optional for debugging)
    app.logger.debug(f"Anime URL from query parameter: {anime_cat}")
    json_file_path = os.path.join(os.path.dirname(__file__),'..', 'data', '9animeHomePage.json')
    # Load the JSON data from the homepage.json file
    with open(os.path.join(os.getcwd(), json_file_path), 'r', encoding='utf-8') as f:
        homepage_data = json.load(f)
    # Render the Jinja2 template (homepage.html) and pass the JSON data
    return render_template('9animeCategory.html', homepageData=homepage_data, anime_category=anime_cat)



    
