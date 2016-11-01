from database_module import DatabaseModule
from helper import IO
import RPi.GPIO as GPIO
import sensor_rgbw
import sensor_DHT11
import sensor_BMP180

def main():
    print ("Hello, SEN!")
    #database = DatabaseModule()
    #IO.print_to_json("data.json", database.get_records())
    #web_server.run_server()

    GPIO.setmode(GPIO.BCM)
    dht11 = sensor_DHT11.SensorDht11()
    dht11.get_temp_hum()
    rgbw = sensor_rgbw.SensorRgbw()
    rgbw.get_rgbw()
    bmp180 = sensor_BMP180.SensorBmp180()
    bmp180.get_temp_press()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
