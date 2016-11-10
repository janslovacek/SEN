import Adafruit_BMP.BMP085 as BMP085
import logging


class SensorBmp180:

    def get_temp_press_alt(self):
        try:
            sensor = BMP085.BMP085()
            temperature = sensor.read_temperature()
            pressure = sensor.read_pressure()
            altitude = sensor.read_altitude()
        except Exception as e:
            logging.info(str(e))
            temperature, pressure, altitude = None
        logging.info('Temp = {0:0.2f} *C'.format(temperature))
        logging.info('Pressure = {0:0.2f} Pa'.format(pressure))
        logging.info('Altitude = {0:0.2f} m'.format(altitude))
        return temperature, pressure, altitude
