from database_module import DatabaseModule
from helper import IO
import web
import sensor_DHT11

db = None

def main():
    db = DatabaseModule()



    web.run_server()
    #sensor_DHT11.blink()


if __name__ == '__main__':
    main()
