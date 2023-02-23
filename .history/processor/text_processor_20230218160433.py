import re
from processor.word_bank import words

"""
    处理文本的 图片标签, 广告文本
"""

__all__ = ['text_processor']
DEBUG = True

class text_processor :

    def __init__(self, solve_text = '') -> None:
        self.__solve_text = solve_text

    # 替换正则匹配内容
    def img_process(self, exps = '', replacement : dict = None) -> str:
        pattern = re.compile('\\w*?\\.png')
        self.__solve_text = '乐' + self.__solve_text
        return self.__solve_text

