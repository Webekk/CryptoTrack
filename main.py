import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen("https://coinmarketcap.com/pl/currencies/litecoin/").read()

soup = bs.BeautifulSoup(sauce,'lxml')

price = soup.find("div",{"class":"priceValue"})

print(price)