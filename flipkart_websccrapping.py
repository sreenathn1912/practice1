
from turtle import title
from urllib import response
from attr import attrs
import bs4
import requests
from bs4 import BeautifulSoup 

url= "https://www.flipkart.com/search?q=dslr&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

response= requests.get(url)
    #print(response.status_code)
print(response.content)
htmlcontent=response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

titles=[]
prices=[]
images=[]

for d in soup.find_all('div',attrs={'class':'_1AtVbE col-12-12'}):
   title = d.find('div', attrs={'class':'_4rR01T'})
   print(title)
   price =d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
   print(price)
   image=d.find('img', attrs={'class':'_396cs4 _3exPp9'})
   print(image)














