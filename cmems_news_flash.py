import requests
from bs4 import BeautifulSoup
import datetime

def retrieve_feed(url, limit):
    '''url (str): URL downnload HTML content
       limit (int): to apply a limit on a result'''
    
    # List to store the scraped data in
    feed = []

    # Extract news flash from http://marine.copernicus.eu/
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
        exit()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
        exit()
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        exit()
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        exit()

    html_soup = BeautifulSoup(response.text, 'html.parser')
    news_flash = html_soup.find_all('div', class_='views-row', limit=limit)

    for item in news_flash:
        date = item.find('div', class_='created').text     # date
        rec = item.find('div', class_='title').text        # info 
        stat = item.find('div', class_='category').text    # status 
        
        feed.append((date, rec, stat))
        
    return feed

def print_feed(feed, category):
    '''feed (list): list with data in the form (date, info, status) 
       category (str): the notification category'''
    print()
    print(10 * '*' + category + 10 * '*')
    for r in feed:  
        print("{}: {} [{}]".format(r[0], r[1], r[2]))
    
if __name__ == '__main__':
    
    today = datetime.date.today()
    print(80 * '#')
    print(today.strftime('%Y-%m-%d:'),'http://marine.copernicus.eu/','LATEST NEWS FLASH')
    print('Warning Messages Regarding CMEMS Products and Services')
    print('For More Infos Check the User Notification Service:')
    print('https://marine.copernicus.eu/user-corner/user-notification-service')
    print(80 * '#')
    
    category = ['GENERAL', 'IMPROVEMENTS', 'INCIDENTS', 'MAINTENANCE']
    nout = 5  # number of results per category
    
    for i, n in enumerate(range(26,30)):
        _feed = retrieve_feed('https://marine.copernicus.eu/user-corner/user-notification-service?field_category=' + str(n), nout)
        print_feed(_feed, category[i])
