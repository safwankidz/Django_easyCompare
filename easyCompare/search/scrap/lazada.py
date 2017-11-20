from bs4 import BeautifulSoup as soup
import requests
from django.shortcuts import render,get_object_or_404
from search import models

class lazadaScrapEngine:
	
	def scrapIt(self, lconcatURL):
		#url of site to scrap
		my_url = lconcatURL
		#to act like human that browse from browser
		headers = {'User-Agent':'Mozilla/5.0'}
		#do requesting to act like human not bot
		page = requests.get(my_url)

		#html parsing
		page_soup = soup(page.text, "html.parser")

		#main container including header
		mainbigcontainer = page_soup.findAll("div",{"class":"catalog__main__content"})

		page = get_object_or_404(models.PageCrawl, pk=6)

		for container in mainbigcontainer:
			n = 0
			count = 0
			productdiv = container.findAll("div",{"class":"c-product-card__description"})
			pricediv = container.findAll("div",{"class":"c-product-card__price"})
			propicdiv = container.findAll("div",{"class":"c-product-card__img-placeholder"})
			limitloop = len(productdiv)
			while n!= limitloop:
				productnamelist = productdiv[n].a.text.strip()
				pricetaglist = pricediv[n].span.text.strip()
				piclist = propicdiv[n].a.span["data-js-component-params"]
				lcurlyr = piclist.replace("{","")
				rcurlyr = lcurlyr.replace("}","")
				srcr = rcurlyr.replace('"src"',"")
				twodotr = srcr.replace(': "',"")
				allr = twodotr.replace('"',"").strip()
				URLStrip = productnamelist.strip().replace(" ", "-")
				item_instance = models.SearchItem.objects.create(page=page,
																 price=pricetaglist,
																 title=productnamelist,
																 pic=allr,
																 rating=0,
																 detail=' ',
																 item_link=' ',
																 condition='',
																 location='',
																 URLstrip=URLStrip)
				n = n + 1
				count = count+1
				if count==5:
					break
		
		return