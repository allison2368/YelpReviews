# this code gets all of the titles for given range of pages, and i started trying to get the review count too 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


##pgNum, maxPages = 0, 3
##pageUrl = 'https://www.tripadvisor.com/Search?searchSessionId=0003ccec9815a719.ssid&searchNearby=false&q=san%20francisco&sid=9931FB556823418C8BF15A1F6F49F4901701980987127&blockRedirect=true&geo=1&ssrc=e&rf=1'
##nxt_pg_sel = 'a.ui_button.nav.next.primary'
##
##browser = webdriver.Chrome()
##
##browser.maximize_window() # maximize window
##browser.get(pageUrl)
##pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
####next_page = pgSoup.select_one(nxt_pg_sel)
####if next_page:
####    pageUrl = 'https://www.tripadvisor.co.uk' + next_page.get('href')
####    print(next_page)
##
### Extract the onclick attribute value
##onclick_value = pgSoup.select_one('div.result-title').text
##
##if onclick_value:
##    print(onclick_value)
##else:
##    print('did not work')
##browser.quit()


##from selenium import webdriver
##from bs4 import BeautifulSoup
##import time
##
##pageUrl = 'https://www.tripadvisor.com/Search?searchSessionId=001d354476208901.ssid&searchNearby=false&ssrc=e&q=irvine&sid=BBAD01B8056845199B4AB59A4DF325051701993262872&blockRedirect=true&geo=1'
##next_page_sel = 'a.ui_button.nav.next.primary'
##
##browser = webdriver.Chrome()
##browser.maximize_window()
##
##def get_titles(soup):
##    titles = []
##    result_title_elements = soup.select('div.result-title')
##    for result_title_element in result_title_elements:
##        title = result_title_element.text.strip()
##        titles.append(title)
##    return titles
##
##def scrape_page(url):
##    browser.get(url)
##    time.sleep(2)  # Add a short delay to allow dynamic content to load
##    pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
##    return pgSoup
##
### Scrape the initial page
##pgSoup = scrape_page(pageUrl)
##
### Get titles from the initial page
##titles = get_titles(pgSoup)
##print("Titles on the initial page:")
##for title in titles:
##    print(title)
##
### Loop through multiple pages (change the range according to your needs)
##for _ in range(3):  # Change the range according to the number of pages you want to scrape
##    next_page = browser.find_element(next_page_sel)
##    if next_page:
##        next_page.click()
##        time.sleep(2)  # Add a short delay to allow dynamic content to load
##
##        # Scrape the next page
##        pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
##
##        # Get titles from the next page
##        titles = get_titles(pgSoup)
##        print("Titles on the next page:")
##        for title in titles:
##            print(title)
##    else:
##        print('Next page not found')
##        break
##
##browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

pageUrl = 'https://www.tripadvisor.com/Restaurants-g56764-The_Woodlands_Texas.html'
next_page_sel = 'a.BrOJk[data-smoke-attr="pagination-next-arrow"]'

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

def get_review_count(soup):
    reviews = []
    review_count = soup.select('span.IiChw')
    for element in review_count:
        numeric_part = element.contents[0].strip() if element.contents else None
        print(numeric_part)
    
def scrape_page(url):
    browser.get(url)
    time.sleep(2)  # Add a short delay to allow dynamic content to load
    pgSoup = BeautifulSoup(browser.page_source, 'html.parser')
    return pgSoup

# Scrape the initial page
pgSoup = scrape_page(pageUrl)

# Get titles from the initial page
titles = get_titles(pgSoup)
print("Titles on the initial page:")
for title in titles:
    print(title)

numbers = get_review_count(pgSoup)
print("review counts on initial page:")

# Loop through multiple pages (change the range according to your needs)
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
        titles = get_titles(pgSoup)
        print("Titles on the next page:")
        for title in titles:
            print(title)
    except Exception as e:
        print('Next page not found or unable to click:', str(e))
        break

browser.quit()

