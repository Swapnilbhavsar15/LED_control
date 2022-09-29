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
    def i2c_writeto_mem(self, addr, memaddr, buf: bytes):
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
    def __init__(self, addr, bus: I2cAbstraction):
        self.addr = addr
        self.bus = bus


class LedCell:
    def __init__(self, ledcontroller: LedController, is_first_on_led_controller):
        self.ledcontroller = ledcontroller
        self.is_first_on_led_controller = is_first_on_led_controller

    def setmain(self, register_address, value):
        i2c_address = self.ledcontroller.addr
        new_value = int((value*4095)/100)
        self.ledcontroller.bus.i2c_writeto_mem(i2c_address, register_address, new_value.to_bytes(2, byteorder='big'))

    def setred(self, value):
        # value: 0-100
        if self.is_first_on_led_controller:
            pin = LedController.LedRed1
        else:
            pin = LedController.LedRed2

        if pin == 1:
            register_address = 0x0A
        else:
            register_address = 0x22
        LedCell.setmain(self,register_address,value)