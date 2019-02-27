try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup
import csv
from datetime import datetime


# specify the url
quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

# query the website and return the html to the variable page
page =  urlopen(quote_page)

# parse the html using beautiful soup and store in variable soup
soup = BeautifulSoup(page, 'html.parser')
print(soup)
# # Take out the <div> of name and get its value
name_box = soup.find('h1')
print(name_box)
name = name_box.text.strip() # strip() is used to remove starting and trailing
print(name)

# get the h2 value
subtitle = soup.find('p', attrs={'class': 'continue'}) #, attrs={'class':'priceText__1853e8a5'}
content = subtitle.text
print(content)

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([name, content, datetime.now()])