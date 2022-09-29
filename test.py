from dummyi2c import I2CDummy
from ledcontrol import LedController,LedCell

def test_1():
    i2c = I2CDummy()
    ledcontroller = LedController(5, i2c)
    led_red = LedCell(ledcontroller, True)
    led_red.setred(100)
    led_red.setblue(90)
    led_red.setgreen(80)
    led_red.setwhite(70)
    led_red.setUV(60)
    led_red.setIR(50)





