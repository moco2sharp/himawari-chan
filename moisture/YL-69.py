# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import spidev

#GPIOのピン番号
pin = 22

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

#GPIOの指定したピン番号を出力端子に設定
GPIO.setup(pin, GPIO.OUT)

#出力用関数
def output_fromGPIO(pin, output):
    GPIO.output(pin, output)
    sleep(0.1)

def Read_spi(channel):
    """
    MCP3008経由でアナログセンサからのデータを受け取る。
    channelはMCP3008の入力チャンネルで、0から7の値
    """
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    print(adc)
    return data


if __name__ == '__main__':
    #SPI通信開始
    spi=spidev.SpiDev()
    spi.open(0, 0) # bus0, CE0
    spi.max_speed_hz = 100000 #追加　これがないと動かない

    #データ取得前にYL-69に電圧を印可
    output_fromGPIO(pin,True)
    getValue = Read_spi(0)
    print(getValue)
    #YL-69の印加電圧をとめる
    output_fromGPIO(pin,False)
    #SPI通信終了
    spi.close()

