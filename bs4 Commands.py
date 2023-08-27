import requests
from bs4 import BeautifulSoup

with open("Landing Page.html", "r") as f: #insert the name of html file which you want to read 
    html_doc = f.read() 

soup = BeautifulSoup(html_doc, 'html.parser') # here beautiful soap is going to convert the html file which is easily readable by it.

#COMMANDS FOR BS4 

# print(soup.prettify())  # the file is read by this command 
# print(soup.title.string, type(soup.title.string))  # Gives the title of html file - type gives the type of title 
# print (soup.div)  # this only gives the first Div also you can replace the word div with any element like a , p  etc 
print (soup.find_all("div"))  # to get all the divs and element entered in bracket 
