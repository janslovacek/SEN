import RPi.GPIO as GPIO
import logging
import time
import Adafruit_DHT


class SensorDht11:
    """Only pin 4 (BMC) should be used for DHT11 data.
    Provides data from DHT11 sensor.
    """
    _DHT_PIN = 4
    _DHT_TYPE = 11
    _DELAY = 1
    _ATTEMPT_NO = 20

    def __init__(self):
        GPIO.setup(self._DHT_PIN, GPIO.IN)

    def get_temp_hum(self):
        """Returns:
                Two floating point values. First value represents humidity, second
                temperature. Values 'None' can be returned after 20 unsuccessful attempts
                to get value from sensor. This may indicate something is wrong with the
                hardware.
            """
        humidity = None
        temperature = None

        for x in range(self._ATTEMPT_NO):
            try:
                humidity, temperature = Adafruit_DHT.read(self._DHT_TYPE, self._DHT_PIN)
                if humidity is not None and temperature is not None:
                    break
            except Exception as e:
                logging.debug(str(e))
                humidity = None
                temperature = None
            logging.debug('None returned from dht11.')
            time.sleep(self._DELAY)

        logging.info('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
        return humidity, temperature
