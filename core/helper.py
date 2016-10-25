import json
import sys


class IO:

    def __init__(self):
        pass

    @staticmethod
    def print_to_json(filename, data):
        try:
            outfile = open(filename, 'w')
        except IOError:
            print ("Unable to write data file\nDirectory exists?")
            sys.exit(1)

        json.dump(data, outfile, default=lambda o: o.__dict__)
        outfile.close()

