
from urllib import response
import bs4
import requests
from bs4 import BeautifulSoup 

url= "https://www.flipkart.com/search?q=dslr&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response= requests.get(url)
    #print(response.status_code)
print(response.content)
htmlcontent=response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
#print(soup.prettify())
print(soup.title)               ## Buy Products Online at Best Price in India - All Categories
print(soup.title.name)          #Dslr- Buy Products Online at Best Price in India
print(soup.title.parent.name)   # head
print(soup.a)
print(soup.p)
#for image in soup.findAll('img'):
   # print(image.get('src'))
product=soup.find_all ('div', attrs_={'class': '_2QcLo-'})
print(product.string)








