Date: 2015-11-26
Title: 树莓派量天气的计划
Slug: rpi-tianqi
Tags: raspberrypi
Author: andy

# 树莓派天气监控 (在施工)

## 介绍 - 树莓派量天气的计划

我们英国的朋友常常问我们，你们在中国那边的气候怎么样？为了告诉他们所以我创造一台树莓派天气监测系统。 先我选择了传感器。我上网研究以后找到了DHT22温度和湿度传感器。 这个又便宜又有adafruit python library (adafruit就是个美国电子产品的公司)。 另外选择了BMP085传感器，这个可以量气压和温度。用这个的话我也可以把两个传感器数据算平均得温度。除了温度湿度气压以外，我也要表示空气的质量，因为不一定全国的地方都有污染的问题。量空气的质量很难不过airpi.es 用特别便宜的传感器。虽然这样不太准确 但是能算定性的测量。

## 一：硬件

树莓派一代modelA
USB无线
电源
DHT22传感器
BMP085传感器
电线
来酸奶塑料桶用盒子

## 二：电路设计图
photo:
![setup](download.andypi.co.uk/weatherpi_setup.jpg)

## 三：构成软件的基本

因为这个计划比较小，最好的系统就是raspbian-jessie-lite（raspbian小）。 

1. 下载RaspbianJessieLite![download](https://www.raspberrypi.org/downloads/raspbian/)
2. 构成无线（输入用户和密码）
3. 下面的命令安装python啊，传感器需要的drivers啊等等.

```
sudo apt-get update
sudo apt-get install build-essential python-dev python-pip python-smbus
mkdir tianqiapp
cd tianqiapp
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd  Adafruit_Python_BMP
sudo python setup.py install
cd ..

wget abyz.co.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
sudo make install
sudo pigpiod
```

```
sudo raspi-config
(https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

sudo i2cdetect -y 1
scn shot
```

## 四： 
cd  Adafruit_Python_BMP
sudo python simpletest.py


## 五python代码
把下面的代码存在SD卡。文件名：app.py

```python 
# import libraries
import sys, httplib, urllib, time, Adafruit_BMP.BMP085, DHT22, pigpio, atexit
BMP085sensor=Adafruit_BMP.BMP085.BMP085()
from config import *

# Setup RPi GPIO pins
PIN_DHT22=8

# update thingspeak routine (max once every 15 seconds)
def update_thingspeak(data1, data2, data3):
	params = urllib.urlencode({"field1": data1, "field2": data2, "field3": data3,'key':THINGSPEAK_APIWRITE})
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")                
	try:
		conn.request("POST", "/update", params, headers)
		#response = conn.getresponse()
		#print response.status, response.reason
		#data = response.read()
		conn.close()
	except:
		pass
		# error handler if needed

# main loop
if __name__ == "__main__":

	pi = pigpio.pi()

	# Humidity and temp from DHT22
	s = DHT22.sensor(pi, PIN_DHT22, LED=None, power=8)   
	s.trigger()
	time.sleep(0.2)
	humidity=s.humidity()
	temp1=s.temperature()
	
	# temp and pressure from BMP085
	temp2=BMP085sensor.read_temperature()
	pressure = BMP085sensor.read_pressure()

	# calc average temp of 2 sensors
	temperature = 0
	temperature=(temp1+temp2)/2
	
	update_thingspeak(temperature, humidity ,pressure)#, airq)
	print "Temp: " + str(temperature)
	print "Humidity: " + str(humidity)
	print "Pressure: " + str(pressure)	
	pi.stop()
	sys.exit()
```

chmod +x app.py

http://docs.gadgetkeeper.com/pages/viewpage.action?pageId=7700673
http://www.instructables.com/id/Build-Your-First-IOT-with-a-Raspberry-Pi-DHT11-sen/?ALLSTEPS
http://www.australianrobotics.com.au/news/how-to-talk-to-thingspeak-with-python-a-memory-cpu-monitor
https://github.com/raddevon/pyspeak

## 六:
sudo crontab -e
0,15,30,45 /home/pi/tianqiapp/app.py &