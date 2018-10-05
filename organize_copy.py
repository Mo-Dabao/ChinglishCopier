# coding: utf-8
"""
整理从文献中复制出来的全角数字、字母为半角
去除所有空格、换行

@author: Mo Dabao
"""

import tkinter as tk

# 要保留的中文全角标点
preserve = "，。：；？！“”‘’"

root = tk.Tk()  # 创建一个主窗口，用于容纳整个GUI程序
root.title("查重百分百！")  # 设置主窗口对象的标题栏
def set_clipboard(s):
    """
    设置剪切板内容为指定字符串
    """
    root.clipboard_clear()  # 清除剪贴板内容
    root.clipboard_append(s)  # 向剪贴板追加内容

text = tk.Text(root, width=100, height=30)
text.pack()  # pack()方法，用于自动调节组件自身的尺寸

def oganize():
    """
    获得text文本框的内容并整理
    整理完覆盖掉text文本框的内容
    """
    s = text.get(0.0, tk.END)
    text.delete(0.0, tk.END)
    ns = []
    for c in s:
        if c.isspace():
            continue
        else:
            unicode = ord(c)
            # 非中文全角字符转半角
            if 65281 <= unicode <= 65374 and c not in preserve:
                unicode -= 65248
                ns.append(chr(unicode))
            else:
                ns.append(c)
    ns = ''.join(ns)
    text.insert(tk.INSERT, ns)
button_oganize = tk.Button(root, text='整理', command=oganize)
button_oganize.pack()

def cut():
    """
    将文本框内的内容剪切到剪切板
    """
    s = text.get(0.0, tk.END)
    text.delete(0.0, tk.END)
    set_clipboard(s)
button_cut = tk.Button(root, text='剪切', command=cut)
button_cut.pack()

root.mainloop()  # 事件循环
