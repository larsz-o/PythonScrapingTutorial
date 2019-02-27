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
quote_page = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']

# for scraping just one page:
# query the website and return the html to the variable page
# page =  urlopen(quote_page)

# for loop
data = []
for pg in quote_page:
 # query the website and return the html to the variable page
 page = urlopen(pg)

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

# save the data in tuple
data.append((name, content))

# for adding data from just one site to a csv
# open a csv file with append, so old data will not be erased
# with open('index.csv', 'a') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([name, content, datetime.now()])

# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 # The for loop
 for name, content in data:
    writer.writerow([name, content, datetime.now()])