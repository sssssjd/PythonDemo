# -*- coding: utf-8 -*-
__author__ = 'sssssjd'
__date__ = '2018/10/30 15:31'

import requests
import os
import json


def getsrc(url):
    try:
        html = requests.get(url)  # get函数获取图片链接地址，requests发送访问请求
        return html
    except:
        html = requests.get('https://ws1.sinaimg.cn/large/9150e4e5ly1fdr0byflomj208c08caa3.jpg')
        return html


def getimg(keyword, page):

    folder_path = 'D://photo//'+keyword+'//'
    if not os.path.exists(folder_path):  # 判断文件夹是否已经存在
        os.makedirs(folder_path)  # 创建文件夹

    url = 'https://www.doutula.com/api/search?keyword='+keyword+'&mime=0&page='+str(page)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)  # 使用headers避免访问受限
    text = json.loads(response.text)
    items = text['data']['list']
    moreimg = text['data']['more']  # 判断是否还有下一页

    for index, item in enumerate(items, (page-1)*36):
        if item:
            html = getsrc(item['image_url'])  # get函数获取图片链接地址，requests发送访问请求
            img_format = str(item['image_url'])[-3:]
            img_name = folder_path + str(index + 1) + '.'+img_format
            with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
                file.write(html.content)
                file.flush()
            file.close()  # 关闭文件
            print('第%d张图片下载完成' % (index + 1))
            # time.sleep(1)  # 自定义延时
    return moreimg
    # print('抓取完成')


for i in range(1, 51):
    moreimg = int(getimg('葫芦娃', i))
    if moreimg == 0:
        break
print('抓取完成')
