import json
import sys
from datetime import datetime

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

    @staticmethod
    def records_to_chart_json(records):
        chart_json = {
            "xData": [],
            "datasets": [
                {
                    "name": "Temperature",
                    "data": [],
                    "unit": "°C",
                    "type": "line",
                    "valueDecimals": 0,
                    "min": None,
                    "max": None,
                },
                {
                    "name": "Humidity",
                    "data": [],
                    "unit": "%",
                    "type": "line",
                    "valueDecimals": 0,
                    "min": 0,
                    "max": 100,
                },
                {
                    "name": "Air pressure",
                    "data": [],
                    "unit": "hPa",
                    "type": "line",
                    "valueDecimals": 1,
                    "min": None,
                    "max": None,
                },
                # {
                #     "name": "Sky status",
                #     "data": [],
                #     "unit": "",
                #     "type": "line",
                #     "valueDecimals": 0,
                #     "min": 0,
                #     "max": 65536,
                # },
            ],
        }
        for item in records:
            chart_json["xData"].append(item[8])
            chart_json["datasets"][0]["data"].append(item[1])
            chart_json["datasets"][1]["data"].append(item[2])
            chart_json["datasets"][2]["data"].append(item[3] / 100)
            #chart_json["datasets"][3]["data"].append(item[4])

        return chart_json

