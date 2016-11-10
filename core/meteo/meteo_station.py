import logging
import RPi.GPIO as GPIO
from meteo import sensor_BMP180
from meteo import sensor_rgbw
from meteo import sensor_DHT11


class MeteoStation:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def get_dht11_hum_temp(self):
        """Returns:
                Tuple (humidity, temperature). One or more values might be None.
        """
        dht11 = sensor_DHT11.SensorDht11()
        return dht11.get_hum_temp()

    def get_rgbw(self):
        """Returns:
                Tuple (red, green, blue, white). One or more values might be None.
        """
        try:
            rgbw = sensor_rgbw.SensorRgbw()
        except Exception as e:
            logging.info(str(e))
            rgbw = None, None, None, None
        rgbw = rgbw.get_rgbw()
        return rgbw

    def get_bmp180_temp_press_alt(self):
        """Returns:
                Tuple (temperature, pressure, altitude). One or more values might be None.
        """
        bmp180 = sensor_BMP180.SensorBmp180()
        return bmp180.get_temp_press_alt()

