import os
from lxml import etree
import urllib.request

import threading
import socket
from download.save_to_mysql import *
from download.upload import upload_image


start_url = "http://www.xgyw.cc"
socket.setdefaulttimeout(20)

headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
   'Referer': 'http://www.Bing.com/',
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
   'Accept-Encoding': 'none',
   'Accept-Language': 'en-US,en;q=0.8',
   'Connection': 'keep-alive'
}
COOKIES_ENABLED = False


def get_three_pic(url):
    print("get_three_pic " + "start")
    print(url)
    req = urllib.request.Request(url=url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("gb2312", 'ignore')
    except Exception as e:
        pass
    et = etree.HTML(html)
    image_urls = et.xpath("/html/body//table//p//img/@src") #是一个list（但是只有三张）
    th = [("t" + str(i)) for i in range(0, len(image_urls))]
    for i in range(0,len(image_urls)):
        url = start_url + image_urls[i]
        print(url)
        th[i] = threading.Thread(target=upload_image, args=(url,))
        th[i].start()


def get_all_page_url(url, big_item_id, little_item_num, little_item_page_index, little_item_index_in_every_page):
    print("get_all_page_url " + "start")
    print(url)
    req = urllib.request.Request(url=url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("gb2312", 'ignore')
    except Exception as e:
        pass
    et = etree.HTML(html)
    page_num = int(et.xpath("/html/body//table[4]//a/text()")[-2]) # 每一个little_item总共有多少页
    print(page_num)
    urls = []
    for i in range(1, page_num):
        urls.append(url[:-5] + "_" + str(i) + ".html")
    urls.insert(0, url) # 将第一页加进去
    for i in urls:
        print(i)
        # get_three_pic(i, path, big_item_id, little_item_num, title, little_item_page_index, little_item_index_in_every_page)
        get_three_pic(i)


def get_all_item_url(url, big_item_id, little_item_num, little_item_page_index):
    print("get_all_item_url " + "start")
    # url = http://www.xgyw.cc/Xgyw/
    """
    将每一页的item的url获取到
    :param url:
    :param path:
    :return:
    """
    print(url)
    # print(path)
    req = urllib.request.Request(url=url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("gb2312", 'ignore')
    except Exception as e:
        pass
    et = etree.HTML(html)
    item_urls = [start_url+i for i in et.xpath("/html/body//div[3]//table[3]/td[1]/div/a/@href")]  # 每一页标题对应的url
    for i in range(0, len(item_urls)):
        # get_all_page_url(item_urls[i], path, big_item_id, little_item_num, little_item_page_index, i + 1)  # 将little_item对应的url传过去
        get_all_page_url(item_urls[i], big_item_id, little_item_num, little_item_page_index, i + 1)  # 将little_item对应的url传过去




def get_every_page_in_big_item(url, big_title, big_item_id):
    """
    获取每个big_item总共有多少个little_item、总共多少页，每个页面的url是多少
    :param url:
    :param path:
    :param big_title:
    :param big_item_id:
    :return:
    """
    print("get_every_page_in_big_item " + "start")
    print(url)
    req = urllib.request.Request(url=url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("gb2312", 'ignore')
    except Exception as e:
        pass
    et = etree.HTML(html)
    little_item_num = int(et.xpath("/html/body/div[3]/table[3]//table[5]//span/strong/text()")[0])  # little_item个数
    print(big_title + "has " + str(little_item_num) + " items")
    if little_item_num%20 == 0:
        little_item_page = little_item_num // 20 # big_item总共有多少页
    else:
        little_item_page = (little_item_num // 20) + 1
    little_item_page_urls = []
    for i in range(2, little_item_page + 1):
        little_item_page_urls.append(url + "page_" + str(i) + ".html")
    little_item_page_urls.insert(0, url)
    print(little_item_page_urls)  # 每一页的url是多少
    for j in range(0, len(little_item_page_urls)):
        # get_all_item_url(little_item_page_urls[j], path, big_item_id, little_item_num, j)  # 传过去每一页的url
        get_all_item_url(little_item_page_urls[j], big_item_id, little_item_num, j)  # 传过去每一页的url


def get_big_item(url=start_url):
    print("get_big_item " + "start")
    req = urllib.request.Request(url=url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode("gb2312", 'ignore')
    except Exception as e:
        pass
    et = etree.HTML(html)
    big_title = et.xpath("/html/body//div[2]//a/text()")[1:13] + et.xpath("/html/body//div[3]//a/text()")[1:23]
    title_urls = et.xpath("/html/body//div[2]//a/@href")[1:13] + et.xpath("/html/body//div[3]//a/@href")[11:33]
    combine_insert_sql("big_item", [i for i in range(1, len(big_title) + 1)], big_title, title_urls) # 将big_item插入mysql中
    for i in range(0, len(big_title)):
        # get_every_page_in_big_item(title_urls[i], path_big_item, big_title[i], i + 1)
        get_every_page_in_big_item(title_urls[i], big_title[i], i + 1)

if __name__ == '__main__':
    get_big_item()