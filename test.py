from dummyi2c import I2CDummy
from ledcontrol import LedCell, LedController


def test_1():
    i2c = I2CDummy()
    ledcontroller = LedController(5)
    led_red = LedCell(ledcontroller)
    led_red.setred(1, True)
