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
            print("Unable to write data file\nDirectory exists?")
            sys.exit(1)

        json.dump(data, outfile, default=lambda o: o.__dict__)
        outfile.close()

    @staticmethod
    def get_cloud_value(red, green, blue, white):
        """Returns specific cloud type according to rgbw values
            0 - dark (less than 200)
            1 - cloudy (200 - 25k)
            2 - partly cloudy (25k - 40k)
            3 - clear ( more than 40k)
        """
        max_value = max(red, green, blue, white)
        if max_value < 200:
            return 0
        elif max_value < 25000:
            return 1
        elif max_value < 40000:
            return 2
        else:
            return 3

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
        return chart_json

    @staticmethod
    def rgbw_to_json(records):
        chart_json = {
            "red": [],
            "green": [],
            "blue": [],
            "white": []
        }
        for item in records:
            chart_json["red"].append([item[8], item[4]])
            chart_json["green"].append([item[8], item[5]])
            chart_json["blue"].append([item[8], item[6]])
            chart_json["white"].append([item[8], item[7]])
        return chart_json
