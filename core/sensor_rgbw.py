import logging
import smbus


class SensorRgbw:
    __RGBW_DEV_BUS = 1  # the RGBW sensor is connected to RPIs i2c bus no 1
    __RGBW_DEV_ADDR = 0x10
    __RGBW_CONF_REG_ADDR = 0x00
    __RGBW_CONFIG_WORD = 0x0000
    __RED_CMD = 0x08
    __GREEN_CMD = 0x09
    __BLUE_CMD = 0x0A
    __WHITE_CMD = 0x0B

    def __init__(self):
        # init smbus
        self.bus = smbus.SMBus(self.__RGBW_DEV_BUS)
        # configure rgbw sensor
        self.bus.write_word_data(self.__RGBW_DEV_ADDR, self.__RGBW_CONF_REG_ADDR, self.__RGBW_CONFIG_WORD)


    def __read(self, cmd):
        return self.bus.read_word_data(self.__RGBW_DEV_ADDR, cmd)

    # data byte low = LSB, data byte high = MSB
    def get_rgbw(self):
        try:
            red = ByteOperations.swap_1st_and_2nd_byte(self.__read(self.__RED_CMD))
            green = ByteOperations.swap_1st_and_2nd_byte(self.__read(self.__GREEN_CMD))
            blue = ByteOperations.swap_1st_and_2nd_byte(self.__read(self.__BLUE_CMD))
            white = ByteOperations.swap_1st_and_2nd_byte(self.__read(self.__WHITE_CMD))
        except Exception as e:
            logging.debug(str(e))
            red, green, blue, white = None
        logging.info("RED: {0}".format(red))
        logging.info("GREEN: {0}".format(green))
        logging.info("BLUE: {0}".format(blue))
        logging.info("WHITE: {0}".format(white))
        return red, green, blue, white


class ByteOperations:

    @staticmethod
    def swap_1st_and_2nd_byte(number):
        return ((number >> 8) & 0x000000FF) | ((number << 8) & 0x0000FF00)
