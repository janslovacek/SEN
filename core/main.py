from database_module import DatabaseModule
from helper import IO
import RPi.GPIO as GPIO
import meteo_station

def main():
    print ("Hello, SEN!")
    #database = DatabaseModule()
    #IO.print_to_json("data.json", database.get_records())
    #web_server.run_server()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
