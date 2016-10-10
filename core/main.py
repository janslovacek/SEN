from module.DatabaseModule import DatabaseModule
from module.Helper import IO


def main():
    print ("Hello, SEN!")
    database = DatabaseModule()

    IO.print_to_json("data.json", database.get_records())

if __name__ == '__main__':
    main()
