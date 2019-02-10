
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import date

base_url = "https://www.cineplex.com/Showtimes/any-movie/cineplex-cinemas-mississauga?Date="
date = "2/10/2019"
made_url= base_url+date

#Open and close connection to obtain page html
uclient = uReq(base_url)
page_html = uclient.read()
uclient.close()

#parse soup
page_soup = soup(page_html,'html.parser')
showtime_boxes = page_soup.find_all('div',{"class":"showtime-card showtime-single"})
print(len(showtime_boxes))

