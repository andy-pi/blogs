Date: 2016-03-05
Title: 网页抓取
Slug: web-scraping
Tags: python
Author: andy

## 网页抓取

昨天一位顾客请我帮他把一整网站的内容成为MSWORD的文件。我发现了这个网站有一百多的网页，难怪请去安迪牌帮他的忙！当然我不要手动复制网页内容然后在MSWORD粘贴，最后写小程序。

## 细节

虽然能用requests module但是我发现wget的软件更合适，所以我让wget把每一个网页下载了：

```
wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains example-website.org \
     --no-parent \
         example-website.org
```

终于有一个文件夹，里面有很多文件夹和.html文件。所以第一个部分就是要从每一个文件夹一步一步的选择文件 （但不要打印和atom网页）：

```
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
		if (file[-4:]=="html" and file[-9:]!="atom.html" and file[-8:]!="rss.html" and file[-10:]!="Print.html" ):
			# 如果file不是rss,print或atom把file做什么
```

在这个循环里要提取网页的内容。正好每一页有这样的html/css tag:

```
<
```

那么我们能使用BeautifulSoup module为了提取：

```
# 打开文件
workingfile = open(os.path.join(subdir, file))
# 把文件输入Beautiful Soup object
soup = bs4.BeautifulSoup(workingfile, from_encoding='utf-8')
# 选择article-body css tag存为body可变
body = soup.select('.article-body')
```

第一次我把body存在MSWORD，但出问题因为BeatifulSoup输出UTF8跟htmltags一起，MSWORD python module 需要简单text。 必须用encodinghtml2text换一下。
html2text

```
# 把body存为UTF8
unicodestr = unicode(str(body[0]), "utf-8")
# 把UTF8(unicodestr)删除htmltags
plaintextbody=html2text.html2text(unicodestr)
```

快结束了！

```
# 构成MSWORD文件
doc = docx.Document()
# 文件名
save_name=file[:-5] + ".docx"
# 在文件第一部分写文件名
doc.add_paragraph(save_name)
# 加text
doc.add_paragraph(plaintextbody)
# 存档
doc.save(os.path.join("word",save_name))
```

好了！那么下一循环将要做下一文件。


## 综合代码：

```
import bs4, os, docx, html2text, sys
rootdir = './'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if (file[-4:]=="html" and file[-9:]!="atom.html" and file[-8:]!="rss.html" and file[-10:]!="Print.html" ):
            workingfile = open(os.path.join(subdir, file))
            soup = bs4.BeautifulSoup(workingfile, from_encoding='utf-8')
            body = soup.select('.article-body')
            try: 
                unicodestr = unicode(str(body[0]), "utf-8")
                plaintextbody=html2text.html2text(unicodestr)
                doc = docx.Document()
                save_name=file[:-5] + ".docx"
                doc.add_paragraph(save_name)
                doc.add_paragraph(plaintextbody)
                doc.save(os.path.join("word",save_name))
            except:
                continue
```