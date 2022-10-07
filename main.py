import requests
import html5lib
import bs4
import urllib.request
from bs4 import BeautifulSoup

URL="https://apod.nasa.gov/apod/astropix.html"
r=requests.get(URL)
soup=BeautifulSoup(r.content,'html5lib')
table=soup.find('img')
part1="https://apod.nasa.gov/apod/"
final_res=part1+table['src']
print(final_res)
urllib.request.urlretrieve(final_res,"C:\\Users\\goldkiller\\Desktop\\wall2\\file01.jpg")




