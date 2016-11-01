from database_module import DatabaseModule
from database_module import Sort
from helper import IO
import web
import sensor_DHT11


def main():
    print ("Hello, SEN!")
    web.run_server()
    # print(database.get_records(5, 0, Sort.DESC))
    # IO.print_to_json("data.json", database.get_records())
    #sensor_DHT11.blink()

if __name__ == '__main__':
    main()
