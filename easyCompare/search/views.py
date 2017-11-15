from django.http import HttpResponse
from .models import PageCrawl, SearchItem
from django.shortcuts import render,get_object_or_404
from .scrap import lazada
from .scrap import lelong
from .scrap import mudah
from .scrap import elevenstreet
from django.http import Http404
<<<<<<< HEAD
import logging
import requests
=======
>>>>>>> 301f5070833eb2adc7b4fd2768c268026a505990


#main homepage
def home(request):
    page = PageCrawl.objects.all()
    return render(request,'page/index.html',{'page':page,})

<<<<<<< HEAD
#insert data from scrap into model
def store(request):
    userkeyword = request.POST.get('userkeyword')
    # userCategory = input('Enter category first :')
    # userKeyword = input('Enter keyword to search : ')
    # different things different it last code
    # frontMudahURL = 'https://www.mudah.my/malaysia/'
    # lastMudahURL = '-for-sale'
    # fLastMudahURL = '?lst=0&fs=1&w=3&cg=0&q='
    # sLastMudahURL = '&so=1&st=s'
    # concatURL = frontMudahURL + userKeyword + lastMudahURL + fLastMudahURL + userKeyword + sLastMudahURL
    # my_url = concatURL

    # # opening up connection, grabbing the page
    # uClient = uReq(my_url)
    # page_html = uClient.read()
    # uClient.close()

    # # html parsing
    # page_soup = soup(page_html, "html.parser")

    # #page3 = PageCrawl.objects.get(pk=3)
    # page3 = get_object_or_404(PageCrawl,pk=3)

    # containers = page_soup.findAll("div", {"class": "top_params_col1"})

    # for container in containers:
    #     brandprice = container.findAll("div", {"class": "ads_price"})
    #     brandpricelist = brandprice[0].text.strip()
    #     brandname = container.h2.a["title"]

    #     item_instance = SearchItem.objects.create(price=brandpricelist, title=brandname,page=page3 )
    print(userkeyword)
    return HttpResponse("<h1> muahahahaha </h1>")
=======

#search main page
def result(request):
    search_input = request.POST.get('userkeyword', None)
    SearchItem.objects.all().delete()
    userkeyword = search_input

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

    #scraping from each website
    scrapMudahResult = mudah.mudahScrapEngine()
    scrapMudahResult.scrapIt(mconcatURL)
    scrapLazadaResult = lazada.lazadaScrapEngine()
    scrapLazadaResult.scrapIt(lconcatURL)
    scrapLelongResult = lelong.lelongScrapEngine()
    scrapLelongResult.scrapIt(llconcatURL)
    scrapElevenstreetResult = elevenstreet.estreetScrapEngine()
    scrapElevenstreetResult.scrapIt(esconcatURL)

    page = PageCrawl.objects.all()
    return render(request, 'page/homepage.html', {'all_page': page})
>>>>>>> 301f5070833eb2adc7b4fd2768c268026a505990


#page for product specification and details
def specs(request,URLstrip):
    item = get_object_or_404(SearchItem,URLstrip=URLstrip)
    return render(request, 'page/product.html', {'item':item,})


# page for search result page
def details(request):
    item = request.POST.get('items',None)
    webpage = get_object_or_404(PageCrawl,page_id=item)
    return render(request, 'page/detail.html', {'webpage': webpage})

#Http404 example - replace with getObjectOr404
    #try:
    #    webpage = PageCrawl.objects.get(page_id=page_id)
    #except PageCrawl.DoesNotExist:
    #    raise Http404('This page does not exists')

#dynamic page example - replace with template.render
# print(all_page)
#    html = ''
#    for pageCrawl in all_page:
#        url = '/search/'+str(pageCrawl.page_id)+'/'
#        html += '<a href ="' + url + '"> '+str(pageCrawl.info)+' </a> <br> '
#    return HttpResponse(html)
