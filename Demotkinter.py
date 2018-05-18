#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox


def zz(a):
    value = re.compile(r'^[0-9]+\.?[0-9]+$')
    rs = value.match(a)
    return rs


def bmi(high, weigh):
    if zz(high) and zz(weigh):
        high = float(high)
        weigh = float(weigh)
    else:
        return '输入错误，请重新输入！'

    b = weigh / high / high * 10000

    if b < 18.5:
        return "BMI=%.2f, 低于18.5，属于：过轻。" % b
    elif 18.5 <= b < 25:
        return "BMI=%.2f, 位于18.5-25，属于：正常。" % b
    elif 25 <= b < 28:
        return "BMI=%.2f, 位于25-28，属于：过重。" % b
    elif 28 <= b < 32:
        return "BMI=%.2f, 位于28-32，属于：肥胖。" % b
    elif b >= 28:
        return "BMI=%.2f, 高于32，属于：严重肥胖。" % b


class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        self.label1 = Label(self, text = '请输入您的身高:')
        self.label1.pack()
        self.nameInput1 = Entry(self)
        self.nameInput1.pack()
        self.label2 = Label(self, text = '请输入您的体重:')
        self.label2.pack()
        self.nameInput2 = Entry(self)
        self.nameInput2.pack()
        self.alertButton1 = Button(self, text='点击显示结果', command = self.result)
        self.alertButton1.pack()
        self.alertButton2 = Button(self, text='退出', command=self.quit)
        self.alertButton2.pack()

    def result(self):
        bmi_result = bmi(self.nameInput1.get(), self.nameInput2.get()) or '请输入您的参数'
        messagebox.showinfo("BMI转换结果", '%s' % bmi_result)


app = Application()
app.master.title("BMI转换器")
app.mainloop()
