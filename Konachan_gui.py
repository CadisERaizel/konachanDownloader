#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6

import requests
from bs4 import BeautifulSoup
import urllib.request
import shutil


class konachanDownload:
    filename =""

    def sitename(url,page,tag):
        if(tag != ""):
            tag="&tags="+tag
            site = url+str(page)+tag
        else:
            site = url+str(page)
        return site

    def download_konachan(fromPage, max_pg, Url, path,tag):
        pages = fromPage
        images_no = 0
        while max_pg != 0:
            url = konachanDownload.sitename(Url,pages,tag)
            print("Page: "+url)
            code = requests.get(url)
            plaincode = code.text
            soup = BeautifulSoup(plaincode, "html.parser")
            name_soup = soup.find_all('a', {'class': 'thumb'})
            name_id = 0
            for link in soup.findAll('a', {'class': 'directlink'}):
                name = name_soup[name_id].get('href').split('/')[-1]
                urldl = link.get('href')
                fullname = str(name) + ".png"
                flink = urldl
                print(flink)
                urllib.request.urlretrieve(flink, fullname)
                shutil.move("/Users/rohithraj/PycharmProjects/images/" + fullname, path + "/" + fullname)
                images_no += 1
                name_id += 1
            pages+=1
            max_pg -= 1
        konachanDownload.filename = "Done"
        print("Images Downloaded: " + str(images_no))
        print("Download Complete!")

    def explicit(self, exp, startPage, nPages, tag, path):
        url = 'http://konachan.net/post?page='
        if (exp == "1"):
            url = 'http://konachan.com/post?page='
        if(exp == "1"):
            konachanDownload.download_konachan(startPage, nPages, url, path,tag)
        else:
            konachanDownload.download_konachan(startPage, nPages, url, path,tag)

    def noOfImages(option,tag):
        url = 'http://konachan.net/post?page='
        specific = False
        if (option == "1"):
            url = 'http://konachan.com/post?page='
        if (tag != ""):
            tag = '&tags=' + tag
            specific = True
        if (specific == True):
            url = url +"1"+ tag
        else:
            url = url + "1"
        code = requests.get(url)
        plaincode = code.text
        soup = BeautifulSoup(plaincode, "html.parser")
        name_soup = soup.find('div', {'class': 'pagination'}).findChildren('a')
        no = name_soup[-2].text
        return no

