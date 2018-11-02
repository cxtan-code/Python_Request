# coding:utf-8
import re
import requests
import os
from lxml import etree
from time import sleep
HEAD = 'https://tieba.baidu.com'
BZB = "https://tieba.baidu.com/f?kw=%E5%A3%81%E7%BA%B8&ie=utf-8"
MMB = "https://tieba.baidu.com/f?kw=%C3%C8%C3%C3&fr=ala0&tpl=5"
tieba = r'href="(\/\w\/\d+?)" title='


def get_html(url):
    response = requests.get(url)
    # page = urllib.urlopen(url)
    # htmlcode = page.read()
    return response.text


def get_img(html, path):
    i = 0
    html_code = html
    reg = r'class="BDE_Image" src="(.+?\.jpg)" size='
    # reg = r'src="(.+?\.jpg)" size='
    regimg = re.compile(reg)
    imglist = regimg.findall(html_code)
    for img in imglist:
        print img
        i = i + 1
        # urllib.urlretrieve(a, str(i)+".jpg")
        with open(path+str(i)+".jpg", "wb") as file:
            file.write(requests.get(img).content)


def get_url():
    '''
    tiebare = requests.get(MMB)
    regimg = re.compile(tieba)
    tiebalist = regimg.findall(tiebare.text)
    '''
    # 用xpath获取
    tiebare = requests.get(BZB)
    selector = etree.HTML(tiebare.text)
    tiebalist = selector.xpath(
        '//div[@class="threadlist_lz clearfix"]/div/a/@href')
    for body in tiebalist:
        html_code = get_html(HEAD+body)
        print HEAD+body
        try:
            os.mkdir('download_'+body[3:])
            get_img(html_code, 'download_'+body[3:]+'/')
        except OSError:
            get_img(html_code, 'download_'+body[3:]+'/')
