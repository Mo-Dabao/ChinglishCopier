# coding: utf-8
"""
ChinglishCopier's GUI powered by tkinter
未实现：
- 监听剪贴板

@author: Mo Dabao
"""


import tkinter as tk
from organize import organize as organize_core
from ChinglishCopier_pic import weixin_qr


# 帮助文本
HELP = \
"""\n\n\n
清空：
    清空此文本框的内容。\n\n\n
整理：
    若文本框内有内容，则整理文本框内容；
    若文本框内无内容，则整理剪贴板内容。\n\n\n
剪切：
    将文本框内容剪切到剪贴板。

"""

# 关于文本
ABOUT = \
"""\n\n\n
此软件对查重结果概不负责！！！
\n\n\n
所有整理的文献内容归原作者所有
\n\n\n
==================================================\n\n
                                      作者：墨大宝\n
                                微信公众号：碎积云\n
                                         2019-2-22
"""


class MainWindow(tk.Tk):
    """
    主窗口
    """
    def __init__(self):
        super().__init__()
        # 禁止窗口缩放
        self.resizable(width=False, height=False)
        # 主窗口标题
        self.title("查重100%！")
        # 菜单栏
        self.menubar = tk.Menu(self)
        self.menubar.add_command(label="帮助", command=self.help)
        self.menubar.add_command(label="关于", command=self.about)
        self.config(menu=self.menubar)
        # 文本框
        self.text_disp = tk.Text(self, width=50, height=30)
        self.text_disp.insert(tk.INSERT, HELP)
        self.text_disp.grid(row=0, column=0, columnspan=3)
        # “清空”按钮
        self.button_clear = tk.Button(self, text="清空", command=self.clear)
        self.button_clear.grid(row=1, column=0, sticky=tk.W+tk.E)
        # “整理”按钮
        self.button_oganize = tk.Button(self, text="整理", command=self.organize)
        self.button_oganize.grid(row=1, column=1, sticky=tk.W+tk.E)
        # “剪切”按钮
        self.button_cut = tk.Button(self, text="剪切", command=self.cut)
        self.button_cut.grid(row=1, column=2, sticky=tk.W+tk.E)
        # 读取公众号二维码图片的base64编码
        self.weixin_qr = tk.PhotoImage(data=weixin_qr)
        # 事件循环
        self.mainloop()

    def clear(self):
        """
        清空text_disp文本框
        """
        self.text_disp.delete(0.0, tk.END)  # 清空text_disp文本框内容

    def organize(self):
        """
        获得text_disp文本框的内容并整理
        整理完覆盖掉text_disp文本框的内容
        """
        text_old = self.text_disp.get(0.0, tk.END)  # 获取text_disp文本框内容
        text_old = text_old if not text_old.isspace() else self.clipboard_get()
        self.clear()
        text_new = organize_core(text_old)
        self.text_disp.insert(tk.INSERT, text_new)

    def cut(self):
        """
        将文本框内的内容剪切到剪切板
        """
        text = self.text_disp.get(0.0, tk.END)
        self.clear()
        # 更新剪贴板内容为指定字符串
        self.clipboard_clear()  # 清除剪贴板内容
        self.clipboard_append(text)  # 向剪贴板追加内容

    def help(self):
        """
        菜单栏“帮助”
        """
        self.clear()
        self.text_disp.insert(tk.INSERT, HELP)

    def about(self):
        """
        菜单栏“关于”
        """
        self.clear()
        self.text_disp.insert(tk.INSERT, ABOUT)
        # 插入图片
        self.text_disp.image_create(tk.END , image=self.weixin_qr)


if __name__ == "__main__":
    root = MainWindow()

