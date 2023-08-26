from flask import Flask, render_template  
from chicken_dinner.pubgapi import PUBG
from dotenv import load_dotenv
import os
app = Flask(__name__)

@app.route("/")
def home():

    return render_template("home.html")
    
if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv('API_KEY')
    pubg = PUBG(api_key, "steam")
    app.run(debug=True)