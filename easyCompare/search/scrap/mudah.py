from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from django.shortcuts import render,get_object_or_404
from search import models

class mudahScrapEngine:

	def scrapIt(self, mconcatURL):
		my_url = mconcatURL

		#opening up connection, grabbing the page
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()

		#html parsing
		page_soup = soup(page_html, "html.parser")

		containers = page_soup.findAll("div",{"class":"top_params_col1"})

		page = get_object_or_404(models.PageCrawl, pk=7)

		for container in containers:
			brandname = container.h2.a["title"]

			brandprice = container.findAll("div",{"class":"ads_price"})
			brandpricelist = brandprice[0].text.strip()

			URLStrip = brandname.strip().replace(" ", "-")
			item_instance = models.SearchItem.objects.create(page=page,
															 price=brandprice,
															 title=brandname,
															 pic='',
															 rating=0,
															 detail=' ',
															 item_link=' ',
															 condition='',
															 location='',
															 URLstrip=URLStrip)

		return
