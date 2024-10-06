from flask import Flask
from dotenv import load_dotenv
import os

app_path = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(app_path, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config.update(
    
    DEBUG= bool(os.environ.get("DEBUG", False)),
    PORT=os.environ.get("PORT"),
    DEPLOYMENT=os.environ.get("DEPLOYMENT")

)
@app.route("/")
def index():
    return "Welcome to TarotReader" 
@app.route('/about')
def about():
    return "This is about page"  
if __name__=="__main__":
    app.run(debug=app.config["DEBUG"], host='0.0.0.0',port=int (app.config["PORT"]))