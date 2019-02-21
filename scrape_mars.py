# Dependencies
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import time

def marsScrape():

    def scrapeLatestNews():

        #Open Browser in URL

        executable_path = {'executable_path': 'chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        time.sleep(2)

        # retrive HTML from browser
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # find the news and the paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text

        # Display scrapped data 
        print(news_title)
        print(news_p)

        # Close Browser

        browser.quit()

        return news_title,news_p

    def marsFeatImg():

        #Open URL in Browser

        executable_path = {'executable_path': 'chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)

        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)

        browser.find_by_id('full_image').click()
        
        time.sleep(5)

         # retrive HTML from browser

        html = browser.html

        # Parse HTML with Beautiful Soup

        soup= BeautifulSoup(html,'html.parser')

        print(soup)

        # find the image partial Path

        image_path=soup.find("img",class_="fancybox-image")["src"]

        url='https://www.jpl.nasa.gov'

        #complete the imag url path

        featured_image=url+image_path       

        print(featured_image)

        # close browser

        browser.quit()

        return featured_image


    def marsWeather():

        #Open URL in Browser

        executable_path = {'executable_path': 'chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)
        mars_twitter = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(mars_twitter)

        # retrive HTML from browser
        twitter_html = browser.html

        # Parse HTML

        soup = BeautifulSoup(twitter_html, 'html.parser')

        # Find the tweets

        mars_tweets = soup.find_all('div', class_='js-tweet-text-container')

        # list of weather tweets
        mars_weather=[]

        for tweet in mars_tweets: 
            #find the tweet text
            mars_tweet = tweet.find('p').text

            #append only the weather tweets

            if 'Sol' and 'high' and 'low' and 'pressure'  in mars_tweet:
                print(mars_tweet)
                
                mars_weather.append(mars_tweet)
                    
            else: 
                pass

        #Close Browser
        browser.quit()

        #Return the latest tweet
        return mars_weather[0]


    def marsHemisphers():


        #Open URL in Browser

        executable_path = {'executable_path': 'chromedriver'}
        browser = Browser('chrome', **executable_path, headless=False)
        hemispheres_url = 'https://astrogeology.usgs.gov/maps/mars-viking-hemisphere-point-perspectives'
        browser.visit(hemispheres_url)

        # HTML from URL
        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('a', class_='item')

        # List for hemisphere images urls
        hemisphere_image_urls = []

        # Core site URL
        hemispheres_url = 'https://astrogeology.usgs.gov'

        # loop the urls list
        for element in items: 
            
            title = element.find('h3').text 
             
            image_path = element['href']
            
            # Go to the full image 
            browser.visit(f"{hemispheres_url}{image_path}")

            # HTML Object of individual hemisphere information website 
            img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup(img_html, 'html.parser')
            
            complete_image_path=soup.find('img', class_='wide-image')['src']
            
            # Retrieve full image source 
            full_img_url= f"{hemispheres_url}{complete_image_path} "
            
            
            # Append the retreived information into a list of dictionaries 
            hemisphere_image_urls.append({"title" : title, "img_url" : full_img_url})
            
        browser.quit()
        
        print (hemisphere_image_urls)
        # Display hemisphere_image_urls
        return hemisphere_image_urls


    def marsFacts():

        # Mars facts URL
        facts_url = 'http://space-facts.com/mars/'

        # Read HTML with pandas
        mars_facts = pd.read_html(facts_url)

        # retrive the facts table
        marsDF = mars_facts[0]

        marsDF.columns = ['concept','value']

        marsDF.set_index('concept', inplace=True)

        dataDic = marsDF.to_dict(orient='index')  
        
        print('------------------------------------')

        print(dataDic)

        print('------------------------------------')

        return dataDic



    marsData={'latestNews':scrapeLatestNews(),
              'featImage':marsFeatImg(),
              'marsWeather':marsWeather(),
              'marsHemisphers':marsHemisphers(),
              'marsFacts':marsFacts()                        
             }


    return marsData




































