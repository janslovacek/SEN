from database_module import DatabaseModule
from helper import IO
import RPi.GPIO as GPIO
import meteo_station

def main():
    print ("Hello, SEN!")
    #database = DatabaseModule()
    #IO.print_to_json("data.json", database.get_records())
    #web_server.run_server()

    station = meteo_station.MeteoStation()
    dht_h, dht_t = station.get_dht11_hum_temp()
    print('Temp: {0:0.1f} C \nHumidity: {1:0.1f} %'.format(dht_h, dht_t))
    bmp_t, bmp_p, bmp_a = station.get_bmp180_temp_press_alt()
    print('Temp: {0:0.1f} C \nPressure: {1:0.1f} Pa\nAltitude: {2:0.1f} m'.format(bmp_t, bmp_p, bmp_a))
    rgbw_r, rgbw_g, rgbw_b, rgbw_w = station.get_rgbw()
    print('Red: {0} \nGreen: {1} \nBlue: {2} \nWhite: {3} '.format(rgbw_r, rgbw_g, rgbw_b, rgbw_w))
    GPIO.cleanup()

if __name__ == '__main__':
    main()
