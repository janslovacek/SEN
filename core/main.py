from module.DatabaseModule import DatabaseModule
from module.Helper import IO
from module import web_server


def main():
    print ("Hello, SEN!")
    database = DatabaseModule()

    IO.print_to_json("data.json", database.get_records())

    web_server.run_server()

if __name__ == '__main__':
    main()
