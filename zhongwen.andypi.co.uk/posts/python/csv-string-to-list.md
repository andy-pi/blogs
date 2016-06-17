Date: 2016-01-02
Title: CSV to list
Slug: csv-to-list
Tags: python
Author: 安迪


# 把逗号分隔值的字符串转变python的单子

有一个字符串的里面有词，用逗号来分开，像：

```python
>>>string1 = "bill, ben, jack, james"
```
我要把这件数据成为python的单子可是python单子要求每一个词应该被引用号围绕。 既然有两百词所以我就不要手动得做，最快写代码让python做！ 真巧可以用string.split 的办法:

```python
>>>list1 = string1.split(',')
>>>print list1
>>>["bill", "ben", "jack", "james"]
```
