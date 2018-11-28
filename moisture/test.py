import spidev
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 100000
#spi.xfer2([0xff,0xff,0xff,0xff])

def ReadAdc(ch):
	adc = spi.xfer2([1,(8+ch)<<4,0x00])
	print(adc)
	data = ((adc[1]&3)<<8) + adc[2]
	return data

if __name__ == '__main__':
	a = ReadAdc(0)
	print("adc: {:8}".format(a))
