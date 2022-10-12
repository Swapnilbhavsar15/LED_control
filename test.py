from dummyi2c import I2CDummy
from ledcontrol import LedController,LedCell

def test_1():
    i2c = I2CDummy()
    ledcontroller = LedController(5, i2c, False)
    ledcontroller.setfreq(200)
    ledcontroller.set_enable(True)
    led_IR = LedCell(ledcontroller, True)
    led_IR.set_ir(90)



    ledcontroller.set_enable(True) # 0 -> 6
    ledcontroller.set_enable(False) # 0 -> 8

    ledcontroller.set_enable(True)  # 0 -> 6