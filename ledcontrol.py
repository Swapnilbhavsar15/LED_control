import adafruit_pca9685
import busio

class I2cAbstraction:
    def __init__(self, scl, sda, freq):
        pass

    def scan(self):
        raise NotImplementedError

    def i2c_writeto(self, addr, buf):
        raise NotImplementedError

    def i2c_readfrom(self, addr, nbytes):
        raise NotImplementedError

    def i2c_readfrom_mem(self, addr, memaddr, nbytes):
        raise NotImplementedError

    def i2c_writeto_mem(self, addr, memaddr, buf):
        raise NotImplementedError


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

    def __init__(self, addr):
        self.addr = addr


class LedCell:
    def __init__(self, ledcontroller):
        self.ledcontroller = ledcontroller

    def setred(self, value, isTrue):
        if isTrue:
            Pin = LedController.LedRed1
        else:
            Pin = LedController.LedRed2
        i2c_bus = busio.I2C(LedController.Scl, LedController.Sda)
        pca = adafruit_pca9685.PCA9685(i2c_bus)
        pca.frequency = 60
        pca.channels[Pin].duty_cycle = 0xffff