# micropython script that outputs temperature and humidity readings from a DHT11 sensor.
import time
import dht
import machine

# create sensor object
sensor = dht.DHT11(machine.Pin(5))
# sensor = dht.DHT22(machine.Pin(5))

print("* DHT11 Temperature & Humidity *")
print("Temperature | Humidity ")

try:
    while True:
        # trigger measurement
        sensor.measure()

        temp = sensor.temperature()
        hum = sensor.humidity()

        # print value to console.
        # {} is used in conjunction with format() for substitution.
        # .2f       - format to 2 decimal places.
        # end='\r'  - curser will go to the start of the current line instead of making a new line.
        print("{0:>10.1f}C | {1:>7.1f}%".format(temp, hum), end='\r')

        time.sleep(2)

except KeyboardInterrupt:
    print('script stopped by user')
finally:
    print('Goodbye!')