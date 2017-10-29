from django.http import HttpResponse
from urllib.request import urlopen as uReq
from .models import PageCrawl, SearchItem
from bs4 import BeautifulSoup as soup
from django.template import loader
from django.shortcuts import render
from django.http import Http404
import requests


#search main page
def home(request):
    all_page = PageCrawl.objects.all()
    print(all_page)
    html = ''
    for pageCrawl in all_page:
        url = '/search/'+str(pageCrawl.page_id)+'/'
        html += '<a href ="' + url + '"> '+str(pageCrawl.info)+' </a> <br> '
    return HttpResponse(html)


#insert into PageCrawl
def insert(request):
    my_url = 'https://testwebsite.com/search/products/?query=iphone'
    page_instance = PageCrawl.objects.create(info="test",page_url=my_url)
    return HttpResponse("<h1> Meh </h1>")


#page for each website
def details(request,page_id):
    try:
        page = PageCrawl.objects.get(page_id=page_id)
    except PageCrawl.DoesNotExist:
        raise Http404('This page does not exists la, why you come here..pergi sana la ')
    return render(request,'page/detail.html',{'page': page,})


#homepage
def first(request):
    all_page = PageCrawl.objects.all()
    context = {'all_page' : all_page,}
    return render(request,'page/homepage.html',context)
    #return HttpResponse('<h1> The first page loh</h1>')


#insert data from scrap into model
def store(request):
    # userCategory = input('Enter category first :')
    userKeyword = 'iphone'
    # different things different it last code
    catergoryURL = 'Mobile-Phones-and-Gadgets-3020/'
    frontMudahURL = 'https://www.mudah.my/malaysia/'
    # middleMudahURL = userKeyword
    lastMudahURL = '-for-sale'
    fLastMudahURL = '?lst=0&fs=1&w=3&cg=3020&q='
    sLastMudahURL = '&so=1&st=s'
    concatURL = frontMudahURL + catergoryURL + userKeyword + lastMudahURL + fLastMudahURL + userKeyword + sLastMudahURL
    my_url = concatURL

    # opening up connection, grabbing the page
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")

    page1 = PageCrawl.objects.get(pk=1)
    item = SearchItem()
    item.page = page1

    containers = page_soup.findAll("div", {"class": "top_params_col1"})

    for container in containers:
        brandprice = container.findAll("div", {"class": "ads_price"})
        brandpricelist = brandprice[0].text.strip()
        brandname = container.h2.a["title"]

        item_instance = SearchItem.objects.create(price=brandpricelist, title=brandname,page=page1 )

    return HttpResponse("<h1> muahahahaha </h1>")


#template example
def template(request):
    all_page = PageCrawl.objects.all()
    template = loader.get_template('page/index.html')
    context = {
        'all_page':all_page,
    }
    return HttpResponse(template.render(context,request))


def renders(request):
    all_page = PageCrawl.objects.all()
    context = {
        'all_page': all_page,
    }
    return render(request,'page/index.html',context)



