# TODO 
# 1. Make a request to the ebay.com and get a page
# 2. Collect data from each deatail page
# 3. Collect all links to detail pages of each product
# 4. Write scraped data to a csv file

import requests
from bs4 import BeautifulSoup
import csv
import io
def get_page(url):
    response = requests.get(url)    
    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        soup = ""
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
    data = {
        "title": title,
        "price": price,
        "rating": rating
    }
    return data

def write_csv(data,link):
    with open('output.csv','a',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        row = [data["title"],data['price'],data['rating'], link]
        writer.writerow(row) 

def get_index_data(soup):
    links = soup.find_all("a", class_= 's-item__link')
    urls = [item.get("href") for item in links]
    return urls

def main():
    the_url = "https://www.ebay.com/sch/i.html?_nkw=rtx+3060&_pgn=1"
    the_soup = get_page(the_url)
    get_detailed_data(the_soup)
    urls = get_index_data(the_soup)
    for url in urls:
        hot_soup = get_page(url)
        data = get_detailed_data(hot_soup)
        write_csv(data,url)

if __name__ == '__main__':
    main()