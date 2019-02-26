# coding: utf-8
"""
为了解决从pdf等格式的中文文献中复制粘贴常会出现的一些问题：
- 数字、字母等非中文字符变成全角字符
- 产生多余的空格、换行
- 中、英文标点（全、半角）混乱
- 英文上下文中的标点后缺空格
未解决：
- 括号等依赖上下文判断全、半角的标点未识别
- 仅支持中英文文献

@author: Mo Dabao
"""


# 可能出现在换行符前的字符
ENDSIGN = set(".:;!?。：；！？")

# 半角标点（除了.）
HALFPUNCTUATION = set(",:;!?")

# 可能出现在半角空格前的字符
SPACESIGN = set("abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                ",.:;!?\"')]}")

# 可能出现在半角标点前的字符
HALFPUNCTUATIONSIGN = set("abcdefghijklmnopqrstuvwxyz"
                          "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                          "0123456789\"')]}")

# unicode65281～65374中可能要保留的全角标点
FULLPUNCTUATION = set("，。：；！？")

# 数字
NUMBER = set("0123456789")


def organize(text_old):
    """整理从文献中复制出来的文本。

    - 删除多余的空白符（换行、空格、制表等）
    - 英文、数字、部分标点符号的全角字符换成半角字符
    - 修正误判为中文标点（，；：！？）的英文标点字符
    - 英文标点后确保一个空格
    注意：所有括号都处理为半角

    Args:
        text_old: 从文献中复制出来的文本。

    Returns:
        text_new: 整理之后的文本。
    """
    text_new = []
    for char in text_old:
        char_unicode = ord(char)
        # 处理换行符
        if char == '\n':
            # 若上一个字符为可能出现在换行符前的字符则保留
            if text_new and text_new[-1] in ENDSIGN:
                text_new.append(char)
            # 若上一个字符为可能出现在半角空格前的字符则换成半角空格
            elif text_new and text_new[-1] in SPACESIGN:
                text_new.append(' ')
        # 处理非换行符的空白字符
        elif char.isspace():
            # 若上一个字符为可能出现在半角空格前的字符则换成半角空格
            if text_new and text_new[-1] in SPACESIGN:
                text_new.append(' ')
        # 处理unicode65281～65374全角字符
        elif 65281 <= char_unicode <= 65374:
            # 确定要保留的全角字符串
            if char == "～":
                text_new.append(char)
            # 若为中文全角标点
            elif char in FULLPUNCTUATION:
                # 若上一个字符为可能出现在半角标点前的字符则换成半角并加空格
                if text_new and text_new[-1] in HALFPUNCTUATIONSIGN:
                    text_new.append(chr(char_unicode - 65248))
                    text_new.append(' ')
                # 否则保留
                else:
                    text_new.append(char)
            # 否则换成半角
            else:
                text_new.append(chr(char_unicode - 65248))
        # 正常英文字符
        elif char in HALFPUNCTUATIONSIGN:
            text_new.append(char)
        # 半角标点
        elif char in HALFPUNCTUATION:
            if text_new and text_new[-1] not in HALFPUNCTUATIONSIGN:
                text_new.append(chr(char_unicode + 65248))
            else:
                text_new.append(char)
                text_new.append(' ')
        # 处理剩余字符
        else:
            # 若上一个字符是半角空格则删去空格
            if text_new and text_new[-1] == ' ':
                del text_new[-1]
                # 若上一个字符是半角标点则换成全角
                if text_new[-1] in HALFPUNCTUATION:
                    text_new[-1] = chr(ord(text_new[-1]) + 65248)
            text_new.append(char)
    text_new = ''.join(text_new)
    return text_new
