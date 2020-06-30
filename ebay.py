from bs4 import BeautifulSoup
import requests

    
def ebay_scrap(item):
   
    url="https://www.ebay.com/sch/i.html?_from=R40&_nkw={item}&_ipg=25"
        
    url=url.replace("{item}",item)
    print(url)
    res=requests.get(url)
    
    soup=BeautifulSoup(res.text,'html.parser')
 
    pamiec = []
    for post in soup.find_all("div", {"class": "s-item__wrapper clearfix"}):
        temp = {
            "1.adres": post.find_next("a",{"class":"s-item__link"})["href"],
            "2.tytul": post.find_next("h3", {"class": "s-item__title"}).text,
            "3.cena": post.find_next("span", {"class": "s-item__price"}).text,
            "4.cena wysylki":post.find_next("span",{"class":"s-item__shipping s-item__logisticsCost"}).text,
            "5.lokalizacja":post.find_next("span",{"class":"s-item__location s-item__itemLocation"}).text
        }

        pamiec.append(temp)

    
    return pamiec
