from dummyi2c import I2CDummy


def test_1():
    i2c = I2CDummy()
    ledcontroller = LedController(5)
    led_red = LedCell(ledcontroller)
    led_red.setred(1, True)
