from dummyi2c import I2CDummy
from ledcontrol import LedController,LedCell

def test_1():
    i2c = I2CDummy()
    ledcontroller = LedController(5, i2c)
    led_red = LedCell(ledcontroller, True)
    led_red.setred(100)

