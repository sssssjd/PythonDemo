# -*- coding: UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import re
import urllib.parse
import tkinter as tk


# 查询天气
def get_weather():
    city = e1.get()
    url1 = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + city
    weather = requests.get(url1)
    weather.encoding = 'utf-8'
    try:
        soup = BeautifulSoup(weather.text, 'html.parser')
        wheater = soup.find_all('weather')
        text = (('天气:%s' % wheater[0].type.text), ('湿度:%s' % soup.shidu.text),
                ('风力:%s' % soup.fengli.text), wheater[0].high.text, wheater[0].low.text)
        e2['state'] = 'normal'
        e2.delete(1.0, tk.END)
        e2.insert(tk.END, text)
        e2['state'] = 'disabled'
    except:
        text = '查询不到，请确认你输入的地名是否正确'
        e2['state'] = 'normal'
        e2.delete(1.0, tk.END)
        e2.insert(tk.END, text)
        e2['state'] = 'disabled'


# 微博热搜
def get_hotsearch():
    url2 = 'http://s.weibo.com/top/summary?cate=realtimehot'
    hot_search = requests.get(url2)
    hot_search.encoding = 'utf-8'
    try:
        hotkey = re.compile(r'td class=\\"td_05\\"><a href=\\"\\/weibo\\/(.*?)&Refer=top\\"')
        hotkeylistbe = re.findall(hotkey, hot_search.text)
        dict1 = {}
        for title in hotkeylistbe:
            # 去除干扰数字
            title = title.replace('25', '')
            url = 'http://s.weibo.com/weibo/' + title
            title = urllib.parse.unquote(title)  # 转码
            dict1[title] = url

        e3['state'] = 'normal'
        e3.delete(1.0, tk.END)
        i = 1
        for x in dict1:
            i = str(i)
            e3.insert(tk.END, i+'.'+x+'-->'+dict1[x]+'\n')
            i = int(i)
            i = i+1
        e3['state'] = 'disabled'
    except:
        text = '获取失败！'
        e3['state'] = 'normal'
        e3.delete(1.0, tk.END)
        e3.insert(tk.END, text)
        e3['state'] = 'disabled'


# 查询火车票
def train_search():
    star_city = e4.get()
    arr_city = e5.get()
    date = e6.get()
    q_star_city = urllib.parse.quote(star_city)
    q_arr_city = urllib.parse.quote(arr_city)
    url3 = 'https://train.qunar.com/dict/open/s2s.do?dptStation=' + q_star_city + '&arrStation=' +\
           q_arr_city + '&date=' + date + '&type=normal&user=neibu&source=site&start=1&num=500&sort=3'
    train_result = requests.get(url3)
    a1 = train_result.text
    try:
        htm = json.loads(a1)
        lines = htm['data']['s2sBeanList']
        print('一共查询到:%s趟车' % len(lines))
        train_list = []
        for checi in lines:
            list1 = []
            list1.append(checi['trainNo'] + ' ' + checi['dptStationName'] + '->' + checi['arrStationName'] +
                         ' ' + checi['dptTime'] + '-' + checi['arrTime'])
            b = checi['seats']
            for key, value in b.items():
                list1.append(' %s,票价：%s,余票:%s张;' % (key, value['price'], value['count']))
            train_list.append(list)

        e7['state'] = 'normal'
        e7.delete(1.0, tk.END)
        i = 1
        for x in train_list:
            i = str(i)
            e7.insert(tk.END, i + '.' + str(x) + '\n')
            i = int(i)
            i = i + 1
        e7['state'] = 'disabled'
    except:
        text = '获取失败！'
        e7['state'] = 'normal'
        e7.delete(1.0, tk.END)
        e7.insert(tk.END, text)
        e7['state'] = 'disabled'


# GUI
root = tk.Tk()
root.geometry("950x1000")
# root.iconbitmap('123.ico')
root.resizable(width=True, height=False)
root.title('小工具V0.1版本')
if __name__ == '__main__':
    # 天气
    tk.Label(root, text="城市：").grid(row=0, column=0)
    tk.Label(root, text="天气：").grid(row=1, column=0)
    e1 = tk.Entry(root, width=100)
    e2 = tk.Text(root, width=100, height=3, state="disabled")

    e1.grid(row=0, column=1, padx=3, pady=2)
    e2.grid(row=2, column=1, padx=3, pady=2)
    tk.Button(root, text="开始查询", width=10, command=get_weather).grid(row=0, column=2, padx=70, pady=10)

    # 热搜
    e3 = tk.Text(root, width=100, height=20, state="disabled")

    e3.grid(row=5, column=1, padx=3, pady=2)
    tk.Button(root, text="获取微博热搜榜单", width=20, command=get_hotsearch).grid(row=4, column=1, padx=70, pady=10)

    # 火车票
    tk.Button(root, text="火车票查询", width=20).grid(row=14, column=1, padx=70, pady=10)
    tk.Label(root, text="出发地：").grid(row=15, column=0)
    tk.Label(root, text="目的地：").grid(row=16, column=0)
    tk.Label(root, text="时间：").grid(row=17, column=0)
    tk.Label(root, text="时间格式参考：2018-04-02").grid(row=17, column=2)
    e4 = tk.Entry(root, width=100)
    e4.grid(row=15, column=1, padx=3, pady=2)
    e5 = tk.Entry(root, width=100)
    e5.grid(row=16, column=1, padx=3, pady=2)
    e6 = tk.Entry(root, width=100)
    e6.grid(row=17, column=1, padx=3, pady=2)
    tk.Button(root, text="开始查询", width=10, command=train_search).grid(row=16, column=2, padx=70, pady=10)
    e7 = tk.Text(root, width=100, height=20, state="disabled")
    e7.grid(row=18, column=1, padx=3, pady=2)

    tk.mainloop()
