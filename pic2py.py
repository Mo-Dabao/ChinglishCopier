# coding: utf-8


import base64


def pic2py(picnames, pyname):
    """
    将图像文件转换为py文件
    """
    for picname in picnames:
        with open(picname, "rb") as pic:
            b64str = base64.b64encode(pic.read())
        # 注意这边b64str一定要加上.decode()
        with open(pyname + ".py", "a") as py:
            py.write(f"{picname[:-4]} = \"{b64str.decode()}\"\n")

if __name__ == '__main__':
    picnames = [".\pics\weixin_qr.png"]
    pyname = "ChinglishCopier_pic__"
    pic2py(picnames, pyname)
