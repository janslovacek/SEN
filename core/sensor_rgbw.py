import logging
import smbus
import time


class SensorRgbw:
    RGBW_DEV_BUS = 1  # the RGBW sensor is connected to RPIs i2c bus no 1
    RGBW_DEV_ADDR = 0x10
    RGBW_CONF_REG_ADDR = 0x00
    RGBW_CONFIG_WORD = 0x0000
    RED_CMD = 0x08
    GREEN_CMD = 0x09
    BLUE_CMD = 0x0A
    WHITE_CMD = 0x0B

    def __init__(self):
        # init smbus
        self.bus = smbus.SMBus(self.RGBW_DEV_BUS)
        # configure rgbw sensor
        self.bus.write_word_data(self.RGBW_DEV_ADDR, self.RGBW_CONF_REG_ADDR, self.RGBW_CONFIG_WORD)

    def __read(self, cmd):
        return self.bus.read_word_data(self.RGBW_DEV_ADDR, cmd)

    # data byte low = LSB, data byte high = MSB
    def get_rgbw(self):
        red = self.__read(self.RED_CMD)
        green = self.__read(self.GREEN_CMD)
        blue = self.__read(self.BLUE_CMD)
        white = self.__read(self.WHITE_CMD)
        logging.info("-------------------------------------------------------------")
        logging.info("RED: {0}".format(red))
        logging.info("GREEN: {0}".format(green))
        logging.info("BLUE: {0}".format(blue))
        logging.info("WHITE: {0}".format(white))
        logging.info("-------------------------------------------------------------")

