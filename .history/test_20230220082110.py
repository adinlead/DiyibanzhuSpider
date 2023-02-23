
"""解析链接测试"""
import re

class url_parser:
    def __init__(self, url:str):
        """"判空"""
        if len(url.strip()) == 0:
            raise ValueError("input params is empty")
        
        self.__url = url
        self.__parse()
    
    def __parse(self):
        """检验是否url链接"""
        pattern = re.compile(
            "/^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\*\+,;=.]+$/")
        result = pattern.search(self.__url)
        print(result)
        

parser = url_parser('nsalknasfo')
print(parser)


"""页面解析测试"""
# from bs4 import BeautifulSoup as bs

# def substring(inp:str, st:str, ed:str) -> str:
#     return inp[inp.index(st) + len(st) : inp.index(ed)]

# with open('[case]32-32880-754225_5.html', 'rt', encoding='utf-8') as f:
#         data = f.read()

# soup = bs(data, 'html.parser')

# scripts = soup.find_all('script')

# # need_sorted -> str(base64 arr)
# ns = None
# ns_prefix = "var ns='"

# # 确认该页内容是否乱序
# for script in scripts:
#     script_text = script.get_text()
#     if ns_prefix in script_text:
#         ns = script_text[script_text.index(ns_prefix) + len(ns_prefix) :-2]
#         break
    
# print(ns)
# chapter_text = soup.find('div', class_='neirong').get_text()
# print(chapter_text)

