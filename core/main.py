from database_module import DatabaseModule
from helper import IO
import web_server
import sensor_DHT11


def main():
    print ("Hello, SEN!")
    database = DatabaseModule()
    #IO.print_to_json("data.json", database.get_records())

    #web_server.run_server()
    sensor_DHT11.blink()


if __name__ == '__main__':
    main()
