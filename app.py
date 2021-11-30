
# Import tools 

# Use Flask to render a template, redirecting to another url, and creating a URL
from flask import Flask, render_template, redirect, url_for
# Use PyMongo to interact with our Mongo DB
from flask_pymongo import PyMongo
# Use the scraping code - convert Jupyter notebook to Python
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Next route and function
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# Flask run
if __name__ == "__main__":
   app.run(debug=True)


# if __name__=="__main__":
#     app.run(debug=True)