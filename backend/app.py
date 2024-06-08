from flask import Flask, request, jsonify
from flask_cors import CORS
from genai import GenAI
from jigsawstack import JigsawStack
from dotenv import load_dotenv
from os import getenv


load_dotenv()
GOOGLE_GENAI_KEY = getenv("GOOGLE_GENAI_KEY")
JIGSAWSTACK_SECRET_KEY = getenv("JIGSAWSTACK_SECRET_KEY")

genAI = GenAI(GOOGLE_GENAI_KEY)
jigsawStack = JigsawStack(JIGSAWSTACK_SECRET_KEY)

app = Flask(__name__)
CORS(app)

@app.route("/getrecommendations")
def getVolunteeringRecommendations():
  location = request.args.get("location")
  keyword = request.args.get("keyword")
  
  opportunities = jigsawStack.scrapeVolunteeringOpportunities(location, keyword)
  volunteering = genAI.getVolunteeringSuggestions(opportunities)
  occupations = jigsawStack.getOccupationSuggestions(keyword)

  response = { 
    "volunteering": volunteering,
    "occupations": occupations,
  }
  
  return jsonify(response)
