from django.shortcuts import render
from .models import Products
import requests
import time
from bs4 import BeautifulSoup


# Create your views here.
def products(request):
    prod = Products.objects.all()
    fetchData()
    return render(request, 'index.html', {'pro':prod})


def fetchData():
    # Make a request
    page = requests.get('https://slickdeals.net/newsearch.php?page="+str(page)+"&forumchoice[]=9&pp=20&sort=newest&rating=1&previousdays=1&filter[]=12029&forumid[]=9&hideexpired=1&r=1')
    soup = BeautifulSoup(page.content, 'html.parser')
    # Create all_products as empty list
    all_products = []
     # Find Elements by ID
    results = soup.find(id="searchResults")
    products = results.find_all("div", class_="resultRow")
    count =0 
    for product in products:
        count += 1
        dealTitle   = product.find("a", class_="dealTitle")
        dealInfo    = product.find("div", class_="dealInfo")
        price       = product.find("span", class_="price")
        store       = product.find("span", class_="store")
        ratingNum   = product.find("div", class_="ratingNum")
        activityCol = product.find("div", class_="activityCol")
        lastPostCol = product.find("div", class_="lastPostCol")
        dealImg     = product.find("img", class_="lazyimg")
        dealLink    = product.find("a", class_="dealTitle")
        dealPostLink= product.find("a", class_="username bp-p-dealLink bp-c-link")
        if dealImg != None:
            dealImg = dealImg.attrs['data-original'] 
        if dealLink != None:
            dealLink = f'https://slickdeals.net/{dealLink.attrs["href"]}'
        if dealPostLink != None:
            dealPostLink = f'https://slickdeals.net/{dealPostLink.attrs["href"]}'

        dealTitle   = dealTitle.text.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        dealInfo    =  dealInfo.text.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        price       = price.text.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        store       = store.text.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        ratingNum   = ratingNum.text.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        activityCol = activityCol.text.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        lastPostCol = lastPostCol.text.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        if dealImg != None:
            dealImg = dealImg.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        if dealLink != None:
            dealLink = dealLink.replace("\n", '').replace("\r", '').replace("\t", '').strip()
        if dealPostLink != None:
            dealPostLink = dealPostLink.replace("\n", '').replace("\r", '').replace("\t", '').strip()

        deals = ()
        deals += (dealTitle,)
        deals += (dealInfo,)
        deals += (price,)
        deals += (store,)
        deals += (ratingNum,)
        deals += (activityCol,)
        deals += (lastPostCol,)
        deals += (dealImg,)
        deals += (dealLink,)
        deals += (dealPostLink,)
        all_products.append(deals)

    
    # for i in range(len(all_products)):
    #     print('\n\n')
    #     print('=='*40)
    #     print(' '*40, i+1)
    #     print('=='*40)

    #     print(f'\ndealTitle\t:=:\t{str(all_products[i][0])}')
    #     print(f'\ndealInfo\t:=:\t{str(all_products[i][1])}')
    #     print(f'\nprice\t\t:=:\t{str(all_products[i][2])}')
    #     print(f'\nstore\t\t:=:\t{str(all_products[i][3])}')
    #     print(f'\nratingNum\t:=:\t{str(all_products[i][4])}')
    #     print(f'\nactivityCol\t:=:\t{str(all_products[i][5])}')
    #     print(f'\nlastPostCol\t:=:\t{str(all_products[i][6])}')
    #     print(f'\ndealImg\t:=:\t{str(all_products[i][7])}')
    #     print(f'\ndealLink\t:=:\t{str(all_products[i][8])}')
    #     print(f'\ndealPostLink\t:=:\t{str(all_products[i][9])}')

    for i in range(len(all_products)):
        reg = Products(id=(i+1),
        dealTitle=str(all_products[i][0]),
        dealInfo=str(all_products[i][1]),
        price=str(all_products[i][2]),
        store=str(all_products[i][3]),
        ratingNum=str(all_products[i][4]),
        activityCol=str(all_products[i][5]),
        lastPostCol=str(all_products[i][6]),
        dealImg=str(all_products[i][7]),
        dealLink=str(all_products[i][8]),
        dealPostLink=str(all_products[i][9]))
        reg.save()
    print('DB Table Inserted!!!')
        
