# coding: utf-8
"""
整理从文献中复制出来的非中文全角字符为半角
去除不在特定符号后的空格、换行

@author: Mo Dabao
"""

import time
import tkinter as tk
from tkinter import messagebox

# 要保留的中文全角标点
CHINESE = "！？，。：；“”‘’"

# 英文结束字符
ENGLISH = set("abcdefghijklmnopqrstuvwxyz"
              "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
              "!\"'),./:;?]}")

# 开场白
PROLOGUE = \
"""

清空：
    清空此文本框的内容。\n
整理：
    若文本框内有内容，则整理文本框内容；
    若文本框内无内容，则整理剪贴板内容。\n
剪切：
    将文本框内容剪切到剪贴板。
\n\n\n\n\n
墨大宝
2018-10-26
"""

BYE = \
"""
\n\n\n
此软件对查重结果概不负责！！！
\n\n\n
所有整理的文献内容归原作者所有
"""


class MainWindow(tk.Tk):
    """
    主窗口
    """
    def __init__(self):
        super().__init__()  # 手动继承父类构造方法
        self.title("查重100%！")  # 设置主窗口对象的标题栏
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # 组件
        self.text_disp = tk.Text(self, width=50, height=30)
        self.text_disp.insert(tk.INSERT, PROLOGUE)
        self.text_disp.pack()
        self.button_clear = tk.Button(self, text="清空", command=self.clear)
        self.button_clear.pack(side="left", expand="yes", fill="x")
        self.button_oganize = tk.Button(self, text="整理", command=self.oganize)
        self.button_oganize.pack(side="left", expand="yes", fill="x")
        self.button_cut = tk.Button(self, text="剪切", command=self.cut)
        self.button_cut.pack(side="left", expand="yes", fill="x")
        self.mainloop()  # 事件循环

    def clear(self):
        """
        清空text_disp文本框
        """
        self.text_disp.delete(0.0, tk.END)  # 清空text_disp文本框内容

        
    def oganize(self):
        """
        获得text_disp文本框的内容并整理
        整理完覆盖掉text_disp文本框的内容
        """
        s_raw = self.text_disp.get(0.0, tk.END)  # 获取text_disp文本框内容
        s_raw = s_raw if not s_raw.isspace() else self.clipboard_get()
        self.clear()
        s_rightwidth = []
        for char in s_raw:
            # 非中文全角字符转半角
            char_unicode = ord(char)
            if 65281 <= char_unicode <= 65374 and char not in CHINESE:
                char_unicode -= 65248
                s_rightwidth.append(chr(char_unicode))
            elif char in "　\t":
                s_rightwidth.append(' ')
            else:
                s_rightwidth.append(char)
        s_new = []
        length = len(s_rightwidth)
        last_char = ' '
        for n, char in enumerate(s_rightwidth):
            if char == ' ':
                if last_char in ENGLISH:
                    s_new.append(char)
                else:
                    continue
            elif char == '\n':
                if last_char in ".。：；":
                    s_new.append(char)
                else:
                    continue
            else:
                s_new.append(char)
            last_char = char
        s_new = ''.join(s_new)
        self.text_disp.insert(tk.INSERT, s_new)

    def cut(self):
        """
        将文本框内的内容剪切到剪切板
        """
        s = self.text_disp.get(0.0, tk.END)
        self.clear()
        # 更新剪贴板内容为指定字符串
        self.clipboard_clear()  # 清除剪贴板内容
        self.clipboard_append(s)  # 向剪贴板追加内容

    def on_closing(self):
        self.clear()
        self.text_disp.insert(tk.INSERT, BYE)
        time.sleep(1)
        if messagebox.showinfo(title="广告位长期招租",
                               message="983248128\nmo_dabao"):
            self.destroy()

if __name__ == "__main__":
    root = MainWindow()

