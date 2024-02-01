import adafruit_bme680
import time
import board

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()   # uses board.SCL and board.SDA
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

starttime = time.time()

# change this to match the location's pressure (hPa) at sea level
bme680.sea_level_pressure = 1013.25

FinalPrint = [starttime]

timediff = 0

while timediff < 10:
	
    p1 = "\nTemperature: %0.1f C" % bme680.temperature
    FinalPrint.append(p1)
    p2 = "Gas: %d ohm" % bme680.gas
    FinalPrint.append(p2)
    p3 = "Humidity: %0.1f %%" % bme680.relative_humidity
    FinalPrint.append(p3)
    p4 = "Pressure: %0.3f hPa" % bme680.pressure
    FinalPrint.append(p4)
    p5 = "Altitude = %0.2f meters" % bme680.altitude
    FinalPrint.append(p5)
    timediff = time.time() - starttime
    p6 = "Time Passed: %0.1f seconds" % timediff
    FinalPrint.append(p6)
	
    time.sleep(2)
    
print(FinalPrint)
