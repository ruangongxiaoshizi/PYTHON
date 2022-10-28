from PIL import Image #pillow处理图片的工具
import os #python内置函数，处理文件
im = Image.open('E:/pythonzhinan/CrawlOne/img_f/1.jpg')
w,h = im.size
img_row = 3
img_column = 10
names = os.listdir('E:/pythonzhinan/CrawlOne/img_f')

#建立新的画布
new_img = Image.new('RGB',(img_column*w,img_row*h))
for i in range(img_row):
    for j in range(img_column):
        o_img = Image.open('E:/pythonzhinan/CrawlOne/img_f/'+names[img_column*i+j])
        new_img.paste(o_img,(j*w,i*h))
new_img.save('wzxlp.jpg')