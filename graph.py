#!/usr/bin/python
#-*- coding:utf-8 -*-
from time import sleep
import datetime
import time
import locale
import matplotlib as mplt
mplt.use("Agg")
import matplotlib.dates
import matplotlib.pyplot as plt

#ディレクトリ指定
logpath = '/home/pi/N1/logfile/'
graphfile = '/home/pi/N1/server/graph.png'
#**** グラフ生成関数 ****
def makeGraph(date):

	#ファイルからデータの読み出し
	f = open(logpath + date + ".log", 'r')
	dates = []
	temp = []
	humi = []
	pres = []
	moist = []
	#ファイルからデータ取り出し
    	for line in f:
		dates.append(datetime.strptime(line[0:13], "%Y%m%d%H%M%S"))
        	temp.append(float(line[25:29]))
        	humi.append(float(line[32:36]))
        	pres.append(float(line[16:22]))
		moist.append(float(line[40:43]))
    	#時刻データの数値への変換
    	x = mplt.dates.date2num(dates)       #数値へ変換
    	#グラフのインスタンス取得
    	fig, ax1 = plt.subplots(1,1, sharex=True, figsize=(12, 6))
    	plt.ylim([0, 80])           #ax1のY軸スケール指定
    	ax2 = ax1.twinx()
    	plt.ylim([960, 1030])       #ax2のY軸スケール指定
    	#X軸の時間軸フォーマット指定
    	timeFmt = mplt.dates.DateFormatter('%H:%M')   #日/時:分で表示
	start = mplt.dates.DateFormatter(datetime.strptime('00:00','%H:%M'))
	stop = mplt.dates.DateFormatter(datetime.strptime('23:59','%H:%M'))
	#ax1.set_xlim(['00:00','23:59'])
    	ax1.xaxis.set_major_formatter(timeFmt)
    	#グラフ描画 X軸を時間にする
    	ax1.plot_date(x, temp, 'g', xdate=True, label="Temparature")    #color=red Time
    	ax1.plot_date(x, humi, 'k', xdate=True, label="Humidity")       #color=green
    	ax1.plot_date(x, moist,'r', xdate=True, label="Plant Moisture")       #color=black
    	ax2.plot_date(x, pres, 'b', xdate=True, label="Pressure")       #color=blue

    	#横軸の追加
    	ax1.axhline(y=25, color='k', linestyle='--')
    	ax1.axhline(y=50, color='k', linestyle='--')
    	ax2.axhline(y=1013, color='m', linestyle='--')
    	ax1.legend(loc='lower left')                    #凡例表示位置指定
    	ax2.legend(loc='lower right')       
    	ax1.set_xlabel('time')
    	ax1.set_ylabel('temp(DegC)/humidity(%RH)/\nplanter moisture(%RH)', color='k') 
    	ax2.set_ylabel('air pressure(hPa)', color='b')
    	#日本語タイトル
    	ax1.set_title(time.strftime('%m/%d') + ' HIMAWARI.chan ', fontsize=25)
    	fig.savefig(graphfile)
#   fig.show()

if __name__=='__main__':

	datetime = datetime.datetime.today()
	datetime_formatted = datetime.strftime("%Y%m%d")
    	makeGraph(datetime_formatted)
