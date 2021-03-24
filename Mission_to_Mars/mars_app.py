from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
mars = db.mars

@app.route("/")
def home():
    # Find one record of data from the mongo database
    mars_data = list(mars.find())

    if len(mars_data) == 8:
        # Return template and data
        return render_template("index.html", mars=mars_data)
    else:
         mars_data = scrape_mars.scrape()
         mars.insert_many(mars_data)
         return render_template("index.html", mars=mars_data)

@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars.drop()
    mars_data = scrape_mars.scrape()

# Update the Mongo database using update and upsert=True
    mars.insert_many(mars_data)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

