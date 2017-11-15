from bs4 import BeautifulSoup as soup
import requests

class carousellScrapEngine:

	def scrapIt(self, cconcatURL):
		
		#my_url  = 'https://carousell.com/search/products/?query=iphone'
		my_url = cconcatURL
		#headers used to treat like human request 
		#not using urllib because  it is like treat of bot
		headers = {'User-Agent':'Mozilla/5.0'}
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")
		allCarousellProduct = []

		gadgetname_h4 = page_soup.findAll("h4",{"class":"ProductCard__cardTitleContent___LESPy"})
		for container in gadgetname_h4:
			namelist = container.text
			#print(namelist)
			allCarousellProduct.append(namelist)

		gadgetprice_span = page_soup.findAll("span",{"class":"ProductCard__cardPrice___1b7Lt"})
		for container in gadgetprice_span:
			pricelist = container["title"]
			#print(pricelist)
			allCarousellProduct.append(pricelist)

		return allCarousellProduct