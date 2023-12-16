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

pgUrl = 'https://www.tripadvisor.com/Restaurants-g32655-Los_Angeles_California.html'
next_page_sel = 'a.BrOJk[data-smoke-attr="pagination-next-arrow"]'
restaurant_link_sel = 'a.BMQDV._F.Gv.wSSLS.SwZTJ.FGwzt.ukgoS'
rating_sel = 'svg.UctUV[aria-label]'
restaurants_data = []

browser = webdriver.Chrome()

def get_titles(soup):
    titles = []
    result_title_elements = soup.select('div.biGQs._P.fiohW.alXOW.NwcxK.GzNcM.ytVPx.UTQMg.RnEEZ.ngXxk')
   # result_title_elements = soup.select('a.BMQDV._F.Gv.wSSLS.SwZTJ.FGwzt.ukgoS')
    
    for result_title_element in result_title_elements:
        title = result_title_element.text.strip()
        titles.append(title)
    return titles

def get_restaurant_links(soup):
    browser.get(pgUrl)
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


    
def scrape_page(url):
    browser.get(url)
    time.sleep(2)  # Add a short delay to allow dynamic content to load
    pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
    return pgSoup




# Visit the next page
browser.get(pgUrl)
time.sleep(2)  # Add a short delay to allow dynamic content to load

pgSoup = scrape_page(pgUrl)

# Get links from the initial page
links = get_restaurant_links(pgSoup)[:22]

# Get titles from the initial page
titles = get_titles(pgSoup)[:22]

filtered_titles = [title for title in titles if re.match(r"\d+\.", title)]


# Get ratings from the initial page
ratings = get_ratings(pgSoup)[:22]




for name, link, rating in zip(filtered_titles, links, ratings):
    restaurant_dataa = {'name': name, 'link': link, 'rating': rating}
    restaurants_data.append(restaurant_dataa)
        # Get titles from the next page and append to the main list

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
    
# Add ratings to the business_info dictionary
for i in range(len(restaurants_data)):
    restaurants_data[i]['rating'] = ratings[i]

# Sort businesses based on ratings in descending order
top_rated_businessesLA = sorted(restaurants_data, key=lambda x: x['rating'], reverse=True)

# Display the top-rated businesses
for i, business in enumerate(top_rated_businessesLA[:5]):  # Displaying the top 5 businesses
    print(f"{i + 1}. Business Name: {business['name']}")
    print(f"   Business Link: {business['link']}")
    print(f"   Rating: {business['rating']}")
    print()

### Plot a bar chart for the top-rated businesses
##business_namesLA = [business['name'] for business in top_rated_businessesLA[:5]]
##ratingsLA = [business['rating'] for business in top_rated_businessesLA[:5]]
##
##plt.barh(business_namesLA, ratingsLA, color='skyblue')
##plt.xlabel('Rating')
##plt.title('Top-Rated Businesses in Los Angeles')
##plt.show()

# plot for all the ratings


# Plot the histogram
plt.hist(ratings, bins=9, color='skyblue')

plt.xlabel('Rating')
plt.ylabel('Number of Businesses')
plt.title('Business Count by Rating in Los Angeles')

plt.show()



