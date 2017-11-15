from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class mudahScrapEngine:

	def scrapIt(self, mconcatURL):
		allMudahProduct = []
		my_url = mconcatURL

		#opening up connection, grabbing the page
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()

		#html parsing
		page_soup = soup(page_html, "html.parser")

		containers = page_soup.findAll("div",{"class":"top_params_col1"})

		for container in containers:
			brandname = container.h2.a["title"]

			brandprice = container.findAll("div",{"class":"ads_price"})
			brandpricelist = brandprice[0].text.strip()
			allMudahProduct.append(brandname)
			allMudahProduct.append(brandpricelist)

		return allMudahProduct

