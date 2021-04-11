#!/usr/bin/env python
# coding: utf-8

# In[24]:


from bs4 import BeautifulSoup as bs
import requests
import pymongo
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd


# In[14]:
def init_browser():
        executable_path = {'executable_path': ChromeDriverManager().install()}
        return Browser("chrome", **executable_path, headless=False)


def scrape():
        
        browser = init_browser()

        #setup url
        url1 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'


        # In[15]:


        # URL of page to be scraped
        url = 'https://mars.nasa.gov/news/'

        browser.visit(url)

        #retrieve the page with the requests module
        response = browser.html

        #create a BeautifulSoup object; parse with 'html parser'
        soup = bs(response, 'html.parser')
        
        news_p = None
        news_title = None

        while (news_p == None) or (news_title == None):
                try:
                        news_title = soup.find_all('div', class_ = 'content_title')[1].text.strip()
                        news_p = soup.find_all('div', class_ = 'article_teaser_body')[0].text.strip()
                except:
                        pass
        # In[17]:
        

        # Visit URL using browser
        browser.visit(url1)

        # Use splinter to click into featured image to retrieve the image url
        browser.links.find_by_partial_text('FULL IMAGE').click()

        #set variable to this html to use soup and find end path for image
        html = browser.html

        # create soup object
        soup_featured = bs(html, 'html.parser')

        # retrieve the end_path and concatenate with the orginal url

        url_first = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'
        end_path = None
        while end_path == None:
                try:
                        end_path = soup_featured.find('img', class_='fancybox-image').get('src')
                except:
                        pass
        featured_image_url = url_first + end_path
        # In[18]:


        # create URL for scraping
        url2 = 'https://space-facts.com/mars/'

        # create table
        tables = pd.read_html(url2)[0]

        tables.columns = ['description', 'mars']
        table_html = tables.to_html(index = False, classes = "table table-striped")
      
        # In[19]:

        # create a for loop to retrive the images for each hemisphere. 
        hemisphere_image_urls = []
        for x in range(4):
                url3 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
                # Visit URL using browser
                browser.visit(url3)

                # Use splinter to click into featured image to retrieve the image url
                browser.find_by_css('a.product-item img')[x].click()

                #set variable to this html to use soup and find end path for image
                html1 = browser.html

                # create soup object
                soup_images = bs(html1, 'html.parser')
                title = None
                link = None

                while (title == None) or (link == None):
                        try:
                                title = soup_images.find_all('h2', class_ = 'title')[0].text
                                link = soup_images.find_all('div', class_ = 'downloads')[0].find('a')['href']
                        except:
                                pass

                # retrieve the end_path and concatenate with the orginal url
                hemisphere_image_urls.append({'title':title, 'img_url': link})
                
                browser.back()


        # In[20]:


        # Combine all the the information gathered into one dictrionary to return
        mars_data = hemisphere_image_urls
        mars_data.append({'news_title':news_title})
        mars_data.append({'news_p' :news_p })
        mars_data.append({'featured_image_url' : featured_image_url})
        mars_data.append({"mars_facts": table_html})

        browser.quit()

        return(mars_data)
