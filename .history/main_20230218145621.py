import cloudscraper

target = 'http://www.2diyibanzhu.cc/32/32880/754225_2.html'
scraper = cloudscraper.create_scraper()
resp = scraper.get(target)
print(resp.text)
if resp.status_code == 403:
    print('你可能使用了代理服务导致无法访问')
# 输出文档
with open('tmp.txt', 'wt') as f:
    f.write(resp.text)

# 检查获取结果
if __name__ == '__main__':
    pass
