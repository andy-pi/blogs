Date: 2016-01-29
Title: 树莓牌用中文
Slug: rpi-zhongwen
Tags: raspberrypi
Author: 安迪

# 在树莓派中安装中文输入方法  (在施工)

树莓派标准版本raspbian系统用英语。 这个instruction从起教怎么安装中文。 你需要win电脑设置SD卡。 看好：虽然在GUI可以用中文，但是命令行和python代码依然用英文！

第一： 从树莓派网站下载最新版的raspbian系统
第二： extractzip
第三： 下载win32diskimager ![win32diskimager]（http://www.onlinedown.net/soft/110173.htm）
第四： 把SD卡插进win电脑， 然后把*.img文件写到SD卡。
第五： 把SD卡插进树莓派就启动。
第六： 

sudo apt-get install ttf-wqy-zenhei
sudo apt-get install scim-pinyin
sudo raspi-config
然后选择change_locale，在Default locale for the system environment:中选择zh_CN.UTF-8。然后重启机器，就发现整个环境变成中文的了。

http://www.cnblogs.com/yondy/archive/2013/04/23/3033404.html
http://blogger.gtwang.org/2014/12/raspberry-pi-chinese-input-method.html
http://www.guokr.com/post/520901/