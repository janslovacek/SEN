import sqlite3
import os
import logging
import time
from enum import Enum


class Sort(Enum):
    ASC = 1
    DESC = 2


class DatabaseModule:
    """Records are returned as:
            Tuple (id, temp, humidity, pressure, red, green, blue, white, created[as millis]).
    """
    _DATABASE_NAME = 'sen_database.db'

    # Record table definition
    # noinspection SqlNoDataSourceInspection,SqlDialectInspection
    _TABLE_RECORD = 'CREATE TABLE records (' \
                    'id INTEGER PRIMARY KEY AUTOINCREMENT,' \
                    'temperature real, ' \
                    'humidity real, ' \
                    'pressure real, ' \
                    'red int, ' \
                    'green int, ' \
                    'blue int, ' \
                    'white int, ' \
                    'created real)'

    def __init__(self):
        self.__init_sqlite_db()

    def __del__(self):
        self.conn.close()

    # Fill database with test data
    def __create_test_data(self):
        self.add_record(24, 15, 34, 56, 43, 23, 52)
        self.add_record(34, 99, 75, 32, 15, 34, 56)
        self.add_record(13, 78, 32, 11, 48, 84, 43)
        self.add_record(42, 56, 24, 34, 18, 11, 13)
        self.add_record(32, 48, 84, 43, 99, 75, 32)
        self.add_record(31, 12, 35, 21, 56, 24, 34)
        self.add_record(23, 18, 11, 13, 44, 48, 25)
        self.add_record(44, 48, 21, 65, 56, 24, 34)

    # Initialize sqlite database
    def __init_sqlite_db(self):
        logging.info("Initializing SQLite database")
        # First check whether database exists
        exist = os.path.isfile(DatabaseModule._DATABASE_NAME)

        self.conn = sqlite3.connect(DatabaseModule._DATABASE_NAME)

        if not exist:
            logging.debug("Database is not created. Creating new one...")
            self.__create_database(self.conn)
            logging.debug("Database successfully created")
            # logging.debug("Adding test data...")
            # self.__create_test_data()
            # logging.debug("Test data successfully added")

        logging.info("Initialization of database successfully finished")

    # Creates necessary tables for proper working with database
    # noinspection SqlNoDataSourceInspection,PyMethodMayBeStatic
    def __create_database(self, connection):
        cursor = connection.cursor()
        # Create table
        cursor.execute(self._TABLE_RECORD)
        # Save (commit) the changes
        connection.commit()
        pass

    # Adds new record into database
    def add_record(self, temp, humidity, pressure, red, green, blue, white):
        cursor = self.conn.cursor()

        current_millis = time.mktime(time.localtime()) * 1000
        values = (temp, humidity, pressure, red, green, blue, white, current_millis)
        # noinspection SqlNoDataSourceInspection
        cursor.execute('INSERT INTO records'
                       '(temperature, humidity, pressure, red, green, blue, white, created) '
                       'VALUES (?,?,?,?,?,?,?,?)',
                       values)
        self.conn.commit()
        logging.info("New record successfully added")

    # Gets records with from specific time
    def get_records_since(self, millis, limit=-1, offset=0, sort=Sort.ASC):
        cursor = self.conn.cursor()

        values = (millis, limit, offset)
        cursor.execute('SELECT * FROM records'
                       ' WHERE created >= ?'
                       ' ORDER BY created ' + ('ASC' if sort == Sort.ASC else 'DESC') +
                       ' LIMIT ? OFFSET ?', values)
        result = cursor.fetchall()
        # Print number of results
        logging.debug("Found " + str(len(result)) + " rows")

        return result

    # Gets records with specific limit and offset
    # For retrieving all records with specific offset, pass -1 as limit
    def get_records(self, limit=-1, offset=0, sort=Sort.ASC):
        return self.get_records_since(0, limit, offset, sort)

    # Gets last record from database
    def get_last_record(self):
        return self.get_records(1, 0, Sort.DESC)

    # Returns average values of all records
    def get_average_values(self):
        cursor = self.conn.cursor()

        cursor.execute('SELECT '
                       'AVG(temperature), '
                       'AVG(humidity), '
                       'AVG(pressure), '
                       'AVG(red), '
                       'AVG(green), '
                       'AVG(blue), '
                       'AVG(white)'
                       'FROM records')
        return cursor.fetchall()
