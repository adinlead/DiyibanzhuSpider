"""
    暴露相关爬虫接口
"""
from model import *
from core.novel_spider import novel_spider

class diyibanzhu:

    def __init__(self):
        """
        初始化config配置
        """

    

    def get_novel(self, url:str) -> novel:
        """
        传入链接返回小说实体类
        """
        spider = novel_spider(url)
        _novel = spider.connect()
        return spider.parser_novel(_novel)
        
    
    def get_chpater(self, url:str) -> chapter:
        """
        传入链接返回章节实体类
        """
        spider = novel_spider(url)
        _novel = spider.connect()
        if _novel:
           """可访问目录，直接测试访问章节链接""" 
           return spider.parse_chapter()

    def save_file(self, model):
        """
        保存小说或章节, 这里注意可以扩展追加更新和单独保存文件等功能
        """
        if type(model) = 

        
    


