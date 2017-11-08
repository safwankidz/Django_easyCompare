from django.http import HttpResponse
from urllib.request import urlopen as uReq
from .models import PageCrawl, SearchItem
from bs4 import BeautifulSoup as soup
from django.shortcuts import render,get_object_or_404
from .scrap import lazada
from .scrap import lelong
from .scrap import mudah
from .scrap import elevenstreet
from django.http import Http404
from django.template import loader
import requests


#main homepage
def first(request):
    all_page = PageCrawl.objects.all()
    return render(request,'page/index.html',{'all_page' : all_page})


#search main page
def home(request):
    userkeyword = 'iphone7'

    # lazada
    lazadaMainURL = 'http://www.lazada.com.my/'
    lazadaLastURL = '/?itemperpage=60&sc=MS0F&searchredirect='
    lconcatURL = lazadaMainURL + userkeyword + lazadaLastURL + userkeyword

    # mudah
    mudahMainURL = 'https://www.mudah.my/malaysia/'
    mudahMiddleURL = '-for-sale'
    mudahfLastURL = '?lst=0&fs=1&w=3&cg=0&q='
    mudahsLastURL = '&so=1&st=s'
    mconcatURL = mudahMainURL + userkeyword + mudahMiddleURL + mudahfLastURL + userkeyword + mudahsLastURL

    # elevenstreet
    elevenstreetMainURL = 'http://www.11street.my/totalsearch/TotalSearchAction/searchTotal?kwd='
    esconcatURL = elevenstreetMainURL + userkeyword

    # lelong
    lelongMainURL = 'https://www.lelong.com.my/catalog/all/list?TheKeyword='
    llconcatURL = lelongMainURL + userkeyword

    # carousell
    # carousellMainURL = 'https://carousell.com/search/products/?query='
    # cconcatURL = carousellMainURL + userkeyword

    scrapMudahResult = mudah.mudahScrapEngine()
    displayMudahResult = scrapMudahResult.scrapIt(mconcatURL)

    scrapLazadaResult = lazada.lazadaScrapEngine()
    displayLazadaResult = scrapLazadaResult.scrapIt(lconcatURL)

    scrapLelongResult = lelong.lelongScrapEngine()
    displayLelongResult = scrapLelongResult.scrapIt(llconcatURL)

    scrapElevenstreetResult = elevenstreet.estreetScrapEngine()
    displayEstreetResult = scrapElevenstreetResult.scrapIt(esconcatURL)

    page = PageCrawl.objects.all()
    return render(request,'page/homepage.html',{'all_page':page})


#page for search result page
def details(request,page_id):
    webpage = get_object_or_404(PageCrawl,page_id=page_id)
    return render(request,'page/detail.html',{'webpage': webpage,})


#page for product specification and details
def specs(request,URLstrip):
    item = get_object_or_404(SearchItem,URLstrip=URLstrip)
    return render(request,'page/product.html', {'item':item,})


#insert data from scrap into model
#def store(request):
#    # userCategory = input('Enter category first :')
#    userKeyword = 'iphone7'
#    # different things different it last code
#    catergoryURL = 'Mobile-Phones-and-Gadgets-3020/'
#    frontMudahURL = 'https://www.mudah.my/malaysia/'
#    # middleMudahURL = userKeyword
#    lastMudahURL = '-for-sale'
#    fLastMudahURL = '?lst=0&fs=1&w=3&cg=3020&q='
#    sLastMudahURL = '&so=1&st=s'
#    concatURL = frontMudahURL + catergoryURL + userKeyword + lastMudahURL + fLastMudahURL + userKeyword + sLastMudahURL
#    my_url = concatURL
#
#     # opening up connection, grabbing the page
#     uClient = uReq(my_url)
#     page_html = uClient.read()
#     uClient.close()

    # html parsing
    # page_soup = soup(page_html, "html.parser")
    #
    # #page3 = PageCrawl.objects.get(pk=3)
    # page3 = get_object_or_404(PageCrawl,pk=7)
    #
    # containers = page_soup.findAll("div", {"class": "top_params_col1"})
    #
    # for container in containers:
    #     brandprice = container.findAll("div", {"class": "ads_price"})
    #     product_price = brandprice[0].text.strip()
    #     title = container.h2.a["title"]
    #     URLStrip = title.strip().replace(" ","-")
    #
    #     item_instance = SearchItem.objects.create(page=page3,
    #                                               price=product_price,
    #                                               title=title,
    #                                               pic='',
    #                                               rating=0,
    #                                               detail=' ',
    #                                               item_link=' ',
    #                                               condition='',
    #                                               location='',
    #                                               URLstrip=URLStrip)
    # return


#template example - replace with render
#def template(request):
#    all_page = PageCrawl.objects.all()
#    templates = loader.get_template('page/index.html')
#    return HttpResponse(templates.render({'all_page':all_page,},request))

#Http404 example - replace with getObjectOr404
    #try:
    #    webpage = PageCrawl.objects.get(page_id=page_id)
    #except PageCrawl.DoesNotExist:
    #    raise Http404('This page does not exists')

#dynamic page example - oreplace with template.render
# print(all_page)
#    html = ''
#    for pageCrawl in all_page:
#        url = '/search/'+str(pageCrawl.page_id)+'/'
#        html += '<a href ="' + url + '"> '+str(pageCrawl.info)+' </a> <br> '
#    return HttpResponse(html)


#insert page info into PageCrawl
#def insert(request):
#    my_url = 'https://testwebsite.com/search/products/?query=iphone'
#    page_instance = PageCrawl.objects.create(info="test",page_url=my_url)
#    return HttpResponse("<h1> Meh </h1>")


#example for render
#def renders(request):
#    all_page = PageCrawl.objects.all()
#    return render(request,'page/index.html',{'all_page': all_page})

