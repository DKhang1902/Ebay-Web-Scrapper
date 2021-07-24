# TODO 
# 1. Make a request to the ebay.com and get a page

import requests
from bs4 import BeautifulSoup
def get_page(url):
    response = requests.get(url)    
    if not response.ok:
        print('Sever responded'+ str(response.status_code))
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_detailed_data(soup):
    # title
    try:
        title = soup.find('h1', id="itemTitle", class_="it-ttl").text.strip("Details about").strip()
        print(title)
    except:
        title=""
    # price
    try:
        price = soup.find('span',id='prcIsum').text.strip()
        print(price)
    except:
        price=""
    # rating
    try:
        rating = soup.find('span', class_ = "ebay-review-start-rating").text.strip()
        print(rating)
    except:
        rating=""

# 2. Collect data from each deatail page
# 3. Collect all links to detail pages of each product
# 4. Write scraped data to a csv file



def main():
    url = "https://www.ebay.com/itm/114904191716?epid=5044602417&hash=item1ac0d2d2e4:g:2UEAAOSw3fJg-3Cu"
    the_soup = get_page(url)
    get_detailed_data(the_soup)





if __name__ == '__main__':
    main()