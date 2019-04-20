import urllib.request
from bs4 import BeautifulSoup
import time

print("Qual Pagina deseja Ler:")
pagina = input()

url = "https://www.carrefour.com.br/busca?termo=Notebook&isGrid=true&sort=&page={}&foodzipzone=na".format(pagina)
req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urllib.request.urlopen(req).read()
time.sleep(2)
soup = BeautifulSoup(webpage, "html.parser")

formatedname = soup.findAll("h3", "prd-name")
formatedprice = soup.findAll("span", "prd-price-new")
print(len(formatedprice))
print(len(formatedname))
name = []
price = []

for i in formatedname:
    line = str(i).replace('<h3 class="prd-name">', "").replace("</h3>", "").strip()
    name.append(line)

for i in formatedprice:
    line = str(i).replace('<span class="prd-price-new">', "").replace("<bdi>", "").replace("</bdi>", "").replace("</span>", "").strip()
    price.append(line)



i = 0
for info in name:
    print(name[i] + " - " + price[i])
    i += 1 
