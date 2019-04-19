import urllib.request
from bs4 import BeautifulSoup
import time

url = "https://www.submarino.com.br/categoria/informatica/notebook/f/entrega-prime/processador-intel%20core%20i5?ordenacao=lowerPrice&origem=omega"
req = urllib.request.Request(url , headers={'User-Agent': 'Mozilla/5.0'})

webpage = urllib.request.urlopen(req).read()
time.sleep(10)
soup = BeautifulSoup(webpage, "html.parser")



formatedname = soup.findAll("h1", "TitleUI-sc-1m3ayw0-16 cvOkHP TitleH1-c6mv26-0 hPNDEG")
formatedprice = soup.findAll("span", "PriceUI-sc-1m3ayw0-10 pYYOk PriceUI-pftkg3-0 hDaJyt TextUI-sc-1hrwx40-0 hbVZKK")
print(len(formatedprice))
print(len(formatedname))
name = []
price = []

for i in formatedname:
    line = str(i).replace('<h1 class="TitleUI-sc-1m3ayw0-16 cvOkHP TitleH1-c6mv26-0 hPNDEG" icon="[object Object]">', "").replace("</h1>", "")
    name.append(line)

for i in formatedprice:
    line = str(i).replace('<span class="PriceUI-sc-1m3ayw0-10 pYYOk PriceUI-pftkg3-0 hDaJyt TextUI-sc-1hrwx40-0 hbVZKK">', "").replace("<!-- -->", "").replace("</span>", "")
    price.append(line)



"""i = 0
for info in price:
    print(name[i] + "-" + price[i])
    i += 1 
"""