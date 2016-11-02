import RPi.GPIO as GPIO
import logging
import time
import Adafruit_DHT


class SensorDht11:
    """Provides data from DHT11 sensor.
        Only pin 4 (BMC) should be used for DHT11 data.
    """
    __DHT_PIN = 4
    __DHT_TYPE = 11
    __DELAY = 2
    __ATTEMPT_NO = 20

    def __init__(self):
        GPIO.setup(self.__DHT_PIN, GPIO.IN)

    def get_hum_temp(self):
        """Returns:
                Two floating point values. First value represents humidity, second
                temperature. Values 'None' can be returned after 20 unsuccessful attempts
                to get value from sensor. This may indicate something is wrong with the
                hardware.
        """
        humidity = None
        temperature = None

        for x in range(self.__ATTEMPT_NO):
            try:
                humidity, temperature = Adafruit_DHT.read(self.__DHT_TYPE, self.__DHT_PIN)
                if humidity is not None and temperature is not None:
                    break
            except Exception as e:
                logging.info(str(e))
                humidity = None
                temperature = None
            logging.debug('None returned from dht11.')
            time.sleep(self.__DELAY)

        logging.info('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
        return humidity, temperature
