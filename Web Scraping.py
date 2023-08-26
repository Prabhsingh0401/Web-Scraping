import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

requests.get("https://www.toppr.com/", proxies=proxies)

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path  , "w") as f:
        f.write(r.text)

url="https://www.toppr.com/"

fetchAndSaveToFile(url , "data/Times.html")