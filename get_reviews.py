from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

pageUrl = 'https://www.tripadvisor.com/Restaurant_Review-g32655-d348825-Reviews-Brent_s_Deli_Northridge-Los_Angeles_California.html'
next_page_sel = 'a.ui_button'

browser = webdriver.Chrome()
browser.maximize_window()


def get_review_body(soup):
    reviews = []
    text_reviews = soup.select('div.prw_rup.prw_reviews_text_summary_hsx div.entry p.partial_entry')
# Extract and print each text review
    for review in text_reviews:
        print(review.get_text(strip=True))
    
def scrape_page(url):
    browser.get(url)
    time.sleep(5)  # Add a short delay to allow dynamic content to load
    pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
    return pgSoup

# Scrape the initial page
pgSoup = scrape_page(pageUrl)

# Get titles from the initial page
reviews = get_review_body(pgSoup)
print(reviews)


# Loop through multiple pages (change the range according to your needs)
for _ in range(5):  # Change the range according to the number of pages you want to scrape
    try:
        next_page = WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, next_page_sel))
        )
        next_page.click()
        time.sleep(5)  # Add a short delay to allow dynamic content to load

        # Scrape the next page
        pgSoup = BeautifulSoup(browser.page_source, 'html.parser')

        # Get titles from the next page
        titles = get_review_body(pgSoup)
        print("Titles on the next page:")
        for title in titles:
            print(title)
    except Exception as e:
        print('Next page not found or unable to click:', str(e))
        break

browser.quit()
