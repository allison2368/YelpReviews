from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import re
import matplotlib.pyplot as plt
import numpy as np
import requests

pageUrl = 'https://www.tripadvisor.com/Restaurants-g60713-San_Francisco_California.html'
next_page_sel = 'a.BrOJk[data-smoke-attr="pagination-next-arrow"]'
restaurant_link_sel = 'a.BMQDV._F.Gv.wSSLS.SwZTJ.FGwzt.ukgoS'
rating_sel = 'svg.UctUV[aria-label]'

browser = webdriver.Chrome()
browser.maximize_window()

def get_titles(soup):
    titles = []
    result_title_elements = soup.select('div.biGQs._P.fiohW.alXOW.NwcxK.GzNcM.ytVPx.UTQMg.RnEEZ.ngXxk')
   # result_title_elements = soup.select('a.BMQDV._F.Gv.wSSLS.SwZTJ.FGwzt.ukgoS')
    
    for result_title_element in result_title_elements:
        title = result_title_element.text.strip()
        titles.append(title)
    return titles

def get_restaurant_links(soup):
    browser.get(pageUrl)
    time.sleep(5)  # Add a short delay to allow dynamic content to load

    restaurant_links = []
    # Find all restaurant links on the page
    for restaurant_link in soup.select(restaurant_link_sel):
        href = restaurant_link.get('href')
        if href:
            restaurant_url = f'https://www.tripadvisor.com{href}'
            if "Restaurant_Review" in restaurant_url:
                restaurant_links.append(restaurant_url)

    return restaurant_links

def get_ratings(soup):
    ratings = []
    rating_elements = soup.select(rating_sel)
    
    for rating_element in rating_elements:
        aria_label = rating_element.get('aria-label')
        if aria_label:
            # Extract numeric part from the TripAdvisor "aria-label"
            bubble_rating = float(re.search(r'(\d+(\.\d+)?)', aria_label).group(1))
            
            # Append "star rating" to the numeric value
            star_rating_label = f"{bubble_rating:.1f} star rating"
            ratings.append(star_rating_label)

    
    return ratings

##def get_review_count(soup):
##    reviews = []
##    review_count = soup.select('span.IiChw')
##    for element in review_count:
##        numeric_part = element.contents[0].strip() if element.contents else None
##        print(numeric_part)
    
def scrape_page(url):
    browser.get(url)
    time.sleep(2)  # Add a short delay to allow dynamic content to load
    pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
    return pgSoup

# Scrape the initial page
pgSoup = scrape_page(pageUrl)

# Get links from the initial page
links = get_restaurant_links(pgSoup)[:20]

# Get titles from the initial page
titles = get_titles(pgSoup)[:20]

filtered_titles = [title for title in titles if re.match(r"\d+\.", title)]


# Get ratings from the initial page
ratings = get_ratings(pgSoup)[:20]



restaurants_data = []
for name, link, rating in zip(filtered_titles, links, ratings):
    restaurant_data = {'name': name, 'link': link, 'rating': rating}
    restaurants_data.append(restaurant_data)
    
### Print all business names, links, and ratings
##for business in restaurants_data:
##    print(f"Business Name: {business['name']}")
##    print(f"   Business Link: {business['link']}")
##    print(f"   Rating: {business['rating']}\n")

browser.quit()


import requests
from bs4 import BeautifulSoup
import re

# Function to get business information from a page
def get_business_info(page_url):
    response = requests.get(page_url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    business_name_elements = soup.find_all('h3', class_='css-1agk4wl')

    
    for business_name_element in business_name_elements:
        business_name = business_name_element.text.strip()
        business_link = business_name_element.find('a')['href']

        # Make a request for the individual business page
        business_page_url = f"https://www.yelp.com{business_link}"
        business_page_response = requests.get(business_page_url)
        business_page_soup = BeautifulSoup(business_page_response.text, 'html.parser')

        # Extract the rating from the individual business page
        rating_div = business_page_soup.find('div', {'aria-label': re.compile(' star rating')})
        rating = rating_div['aria-label'] if rating_div else None

        restaurants_data.append({'name': business_name, 'link': business_link, 'rating': rating})

    return 

# URL template with the start parameter
url_templateLA = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&start={}"

# Number of pages to scrape
num_pages = 2  # Change this to the desired number of pages

# List to store all business information


# Iterate through pages
for page_number in range(0, num_pages * 10, 10):
    page_url = url_templateLA.format(page_number)
    business_info = get_business_info(page_url)
    restaurants_data.append(business_info)


# Print all business names, links, and ratings


for business in restaurants_data:
    try:
        print(f"Business Name: {business['name']}")
        print(f"   Business Link: {business['link']}")
        print(f"   Rating: {business['rating']}\n")
    except TypeError:
        continue

# convert ratings into a numerical list
ratings = []
for business in restaurants_data:
    try:
        if 'rating' in business and business['rating'] is not None:
            # Use a regular expression to extract the first number
            match = re.search(r'(\d+(\.\d+)?)', business['rating'])
            if match:
                first_number = float(match.group(1))
                ratings.append(first_number)
            else:
                print(f"Could not extract a number from the rating: {business['rating']}")
        else:
            print(f"Skipping business with incomplete or missing rating: {business}")

    except TypeError:
        continue

# Calculate average rating
average_rating = sum(ratings) / len(ratings) if ratings else None

# Print the average rating
print(f"Average Rating SF: {average_rating:.2f}")

for business in restaurants_data:
    print(business)

# get the valid ratings from list
valid_ratings = [float(re.search(r'(\d+(\.\d+)?)', str(rating)).group(1)) for rating in ratings if rating is not None]

# Plot the histogram
plt.hist(valid_ratings, bins=5, color='skyblue', edgecolor='black')

plt.xlabel('Rating')
plt.ylabel('Number of Businesses')
plt.title('Business Count by Rating in San Francisco')

plt.show()





