import threading
import sys
import logging
from logging.handlers import RotatingFileHandler
from database_module import DatabaseModule
from database_module import Sort
from helper import IO
import web
import RPi.GPIO as GPIO
import meteo


logging.getLogger().setLevel(logging.INFO)
file_handler = RotatingFileHandler("sen.log", mode='a', maxBytes=10*1024*1024)
file_handler.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.ERROR)
logging.getLogger().addHandler(file_handler)
logging.getLogger().addHandler(stream_handler)


meteo_values_event = threading.Event()
INTERVAL = 900  # seconds = 15 minutes


def get_meteo_values(interval, event):
    db = DatabaseModule()
    station = meteo.MeteoStation()
    while not event.is_set():
        # Measure values and 'sleep'
        humidity, temperature = station.get_dht11_hum_temp()
        i1, pressure, i2 = station.get_bmp180_temp_press_alt()
        red, green, blue, white = station.get_rgbw()
        db.add_record(temperature, humidity, pressure, red, green, blue, white)
        print('Temp: {0:0.1f} C \nHumidity: {1:0.1f} \nPressure: {2:0.1f} Pa\n'
              'Red: {3} \nGreen: {4} \nBlue: {5} \nWhite: {6}'
              .format(temperature, humidity, pressure, red, green, blue, white))
        event.wait(interval)
        pass

    GPIO.cleanup()


def start():
    thread = threading.Thread(target=get_meteo_values, args=(INTERVAL, meteo_values_event))
    thread.daemon = True
    thread.start()


def main():
    print("Hello, SEN!\nFor exit type 'exit'")
    start()
    while True:
        if input() == 'exit':
            meteo_values_event.set()
            sys.exit()
        else:
            print('Invalid command')
    print("Bye")


if __name__ == '__main__':
    main()
