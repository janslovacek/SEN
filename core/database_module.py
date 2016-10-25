import sqlite3
import os
import sys
import logging
import time

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


class DatabaseModule:
    _DATABASE_NAME = 'sen_database.db'

    # Record table definition
    # noinspection SqlNoDataSourceInspection,SqlDialectInspection
    _TABLE_RECORD = '''CREATE TABLE records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature real,
            humidity real,
            created real)'''

    def __init__(self):
        self.__init_sqlite_db()

    def __del__(self):
        self.conn.close()

    # Fill database with test data
    def __create_test_data(self):
        self.add_record(24, 15)
        self.add_record(34, 99)
        self.add_record(13, 78)
        self.add_record(42, 56)
        self.add_record(32, 48)
        self.add_record(31, 12)
        self.add_record(23, 18)
        self.add_record(44, 48)

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
            logging.debug("Adding test data...")
            self.__create_test_data()
            logging.debug("Test data successfully added")

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
    def add_record(self, temp, humidity):
        cursor = self.conn.cursor()

        current_millis = time.mktime(time.localtime())*1000
        values = (temp, humidity, current_millis)
        # noinspection SqlNoDataSourceInspection
        cursor.execute('''INSERT INTO records(temperature, humidity, created) VALUES (?,?,?)''', values)
        self.conn.commit()
        logging.info("New record successfully added")

    # Gets records with from specific time
    def get_records_since(self, millis, limit=-1, offset=0):
        cursor = self.conn.cursor()

        values = (millis, limit, offset)
        cursor.execute('SELECT * FROM records WHERE created >= ? LIMIT ? OFFSET ?', values)
        result = cursor.fetchall()
        # Print number of results
        logging.debug("Found " + str(len(result)) + " rows")

        return result

    # Gets records with specific limit and offset
    # For retrieving all records with specific offset, pass -1 as limit
    def get_records(self, limit=-1, offset=0):
        return self.get_records_since(0, limit, offset)
