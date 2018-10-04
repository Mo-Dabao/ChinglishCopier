# coding: utf-8
"""
整理从文献中复制出来的全角数字、字母为半角
去除所有空格、换行

@author: Mo Dabao
"""

import tkinter as tk

# 新建了一个隐藏的窗口，纯粹是为了操作剪切板
# 应该有更简洁的方法，待改进
r=tk.Tk()
r.withdraw()  # 隐藏窗口
def set_clipboard(s):
    r.clipboard_clear()  # 清除剪贴板内容
    r.clipboard_append(s)  # 向剪贴板追加内容


root = tk.Tk()  # 创建一个主窗口，用于容纳整个GUI程序
root.title("查重百分百！")  # 设置主窗口对象的标题栏
text = tk.Text(root, width=100, height=30)
text.pack()  # pack()方法，用于自动调节组件自身的尺寸
def oganize():
    s = text.get(0.0, tk.END)
    text.delete(0.0, tk.END)
    ns = []
    for c in s:
        if c.isspace():
            continue
        else:
            unicode = ord(c)
            # 非中文全角字符转半角
            if 65281 <= unicode <= 65374 and c not in "，。：；？！“”‘’":
                unicode -= 65248
                ns.append(chr(unicode))
            else:
                ns.append(c)
    ns = ''.join(ns)
    text.insert(tk.INSERT, ns)
button_oganize = tk.Button(root, text='整理', command=oganize)
button_oganize.pack()
def cut():
    s = text.get(0.0, tk.END)
    text.delete(0.0, tk.END)
    set_clipboard(s)
button_cut = tk.Button(root, text='剪切', command=cut)
button_cut.pack()
root.mainloop()  # 事件循环
