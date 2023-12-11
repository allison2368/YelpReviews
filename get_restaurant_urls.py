
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

main_page_url = 'https://www.tripadvisor.com/Restaurants-g659482-Orange_County_California.html'
restaurant_link_sel = 'a.BMQDV._F.Gv.wSSLS.SwZTJ.FGwzt.ukgoS'
next_page_sel = 'a[data-smoke-attr="pagination-next-arrow"][aria-label="Next page"] svg'
all_links = []

browser = webdriver.Chrome()
browser.maximize_window()

def scrape_page(url):
    browser.get(url)
    time.sleep(2)  # Add a short delay to allow dynamic content to load
    pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
    return pgSoup

def get_restaurant_links(soup):
    browser.get(main_page_url)
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
pgSoup = scrape_page(main_page_url)


# Get titles from the initial page
links = get_restaurant_links(pgSoup)
print("Titles on the initial page:")
for link in links:
    print(link)
    

for _ in range(3):  # Change the range according to the number of pages you want to scrape
    try:
        next_page = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, next_page_sel))
        )
        next_page.click()
        time.sleep(2)  # Add a short delay to allow dynamic content to load

        # Scrape the next page
        pgSoup = BeautifulSoup(browser.page_source, 'html.parser')

        # Get titles from the next page
        links = get_restaurant_links(pgSoup)
        all_links.append(links)
    except Exception as e:
        print('Next page not found or unable to click:', str(e))
        break
print(all_links)
