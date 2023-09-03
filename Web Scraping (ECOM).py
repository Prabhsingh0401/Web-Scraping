import requests
from bs4 import BeautifulSoup

# use proxy here if needed 
# proxies = {
#  "http": "http://10.10.1.10:3128",
#  "https": "https://10.10.1.10:1080",
# }


url="https://www.amazon.in/s?k=macbook&ref=nb_sb_noss_1"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

#Its not printing the API here amazon is not allowing 

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

#print(soup.prettify())
# Now instead of printing the whole html document we gonna target certain data that we want to fetch

spans = soup.find(class_="a-size-medium")
print(spans)

# This code will print the span attributes having class a-size-medium.