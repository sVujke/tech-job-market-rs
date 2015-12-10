from bs4 import BeautifulSoup
import requests, time

response = requests.get("http://startit.rs/poslovi/java")

result = response.content

soup = BeautifulSoup(result, 'html.parser')
demand = soup.h1.get_text()
d = str(demand)
#d = demand[4:]
print (soup.a.prettify())
print(d)
print type(d)
