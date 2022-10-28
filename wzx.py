# 爬虫 获取 男神女神图片
import requests#发送请求
from lxml import etree#解析xpath工具
#获取数据
url = "https://movie.douban.com/celebrity/1166896/photos/"
res = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'})
res.encoding = 'utf-8' #显示中文，解决乱码
#print(res.text)#打印文本结果
#提取数据
xp = etree.HTML(res.text)
img_urls = xp.xpath('/html/body/div/div/div/div/ul/li/div/a/img/@src')
img_names = xp.xpath("/html/body/div/div/div/div/ul/li/div[@class='prop']")
t = 0
for u,n in zip(img_urls,img_names):
    print(f'正在下载的图片像素：{n},地址名：{u}')
    t += 1
    #图片响应
    img_res = requests.get(u,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'})
    with open("E:/pythonzhinan/CrawlOne/img_f/{0}.jpg".format(t),'wb') as f:
    #with open(f'E:\\pythonzhinan\\CrawlOne\\img_f\\{n}.jpg')as f:
        f.write(img_res.content)