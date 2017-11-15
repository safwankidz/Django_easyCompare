from bs4 import BeautifulSoup as soup
from django.shortcuts import render,get_object_or_404
from search import models
import requests


class estreetScrapEngine:

	def scrapIt(self, esconcatURL):
		#url of site to scrap
		my_url = esconcatURL
		#to act like human that browse from browser
		headers = {'User-Agent':'Mozilla/5.0'}
		#do requesting to act like human not bot
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")

		maincontainer = page_soup.findAll("div",{"class":"wrap_category"})

		page = get_object_or_404(models.PageCrawl, pk=8)

		for container in maincontainer:
			n = 0
			productdiv = container.findAll("h3",{"class":"product-name tit_info"})
			pricediv = container.findAll("span",{"class":"rm_price old_price"})
			limitloop = len(productdiv)
			count = 0
			while n != limitloop:

				productnamelist = productdiv[n].a.text.strip()
				pricetaglist = pricediv[n].text.strip()
				URLStrip = productnamelist.strip().replace(" ", "-")
				item_instance = models.SearchItem.objects.create(page=page,
														  price=pricetaglist,
														  title=productnamelist,
														  pic='',
														  rating=0,
														  detail=' ',
														  item_link=' ',
														  condition='',
														  location='',
														  URLstrip=URLStrip)
				n = n + 1
				count = count+1
				if count==10:
					break


		return