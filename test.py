from dummyi2c import I2CDummy
from ledcontrol import LedController,LedCell

def test_1():
    i2c = I2CDummy()
    ledcontroller = LedController(5, i2c, True)
    ledcontroller.setfreq(200)
    led_IR = LedCell(ledcontroller, True)
    led_IR.setir(90)






