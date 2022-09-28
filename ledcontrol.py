import adafruit_pca9685
import busio

class LedController:
    LedEn = 0
    LedRed1 = 1
    LedBlue1 = 2
    LedGreen1 = 3
    LedWhite1 = 4
    LedUV1 = 5
    LedIR1 = 6
    LedRed2 = 7
    LedBlue2 = 8
    LedGreen2 = 9
    LedWhite2 = 10
    LedUV2 = 11
    LedIR2 = 12
    LedOp1 = 13
    LedOp2 = 14
    Scl = 15
    Sda = 16
    def __init__(self, addr, bus: I2cAbstraction):
        self.addr = addr
        self.bus = bus


class LedCell:
    def __init__(self, ledcontroller: LedController, is_first_on_led_controller):
        self.ledcontroller = ledcontroller
        self.is_first_on_led_controller = is_first_on_led_controller

    def setred(self, value):
        # value: 0-100
        # value: 0-4095
        if self.is_first_on_led_controller:
            pin = LedController.LedRed1
        else:
            pin = LedController.LedRed2

        if pin == 1:
            register_address = 0x0A
        else:
            raise NotImplementedError
        i2c_address = self.ledcontroller.addr

        self.ledcontroller.bus.i2c_writeto_mem(i2c_address, register_address, bytes([1, 2]))