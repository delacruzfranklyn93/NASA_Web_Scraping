# Mars HTML with scraping capabilities

## Summary: 
   The purpose of this project is to create an HTML page that will scrape various websites for Mars data and insert them into our page. Images of my HTML page can be found in the    images folder. 
## Steps: 
   1)	The first step was to create a python script that would scrape the various websites for new information when the “Scrape New Data” button was clicked. To do this I first           used a splinter browser to visit the URL and then used beautiful soup to find the certain html element that contained the data and extracted it and stored it into a               dictionary that contained all my NASA information.  All of this is done within my scrape_mars.py script.

   2)	I then created a connection to MongoDB using PyMongo and stored my data in a new collection. I then retrieved the data from the collection and inserted it into the html           using render_template from the flask library. Every time the “Scrape New Button” is selected, these 2 steps would run so that we get all the new information from all the            websites I scraped. 

Tools Used: Flask, render_template, PyMongo, Beautiful Soup, Splinter, Pandas, MongoDB

### Websites Scraped:

https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html

https://mars.nasa.gov/news

https://space-facts.com/mars/

https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    
   ![image](https://user-images.githubusercontent.com/63375741/114313466-a3f5e200-9ac4-11eb-8e65-a0a8e20d99f1.png)

 


