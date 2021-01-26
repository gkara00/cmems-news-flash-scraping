# cmems-news-flash-scraping
Simple scraper to get warning messages regarding CMEMS (https://marine.copernicus.eu/) products and services using the BeautifulSoup Python module

#### Prerequisites
- Python 3.6.x
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
(installation using pip: $ pip3 install beautifulsoup4 
or using conda: 
$ conda install -c anaconda beautifulsoup4 )

#### Usage 
python cmems_news_flash.py 

OR send email from terminal:

python cmems_news_flash.py | mail -s "CMEMS NEWS FLASH" john@example.com
