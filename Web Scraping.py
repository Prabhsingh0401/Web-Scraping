import requests

#visit this website to get a soup commands <https://www.crummy.com/software/BeautifulSoup/bs4/doc/>

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path  , "w") as f:
        f.write(r.text)

url="https://www.toppr.com/"

fetchAndSaveToFile(url , "data/Times.html")