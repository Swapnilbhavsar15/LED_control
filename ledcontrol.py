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

    def setfreq(self, freq):
        if (24 <= freq <= 1526):
            prescaleval = round((25000000/(4096*freq))) - 1
        else:
            print("Frequency value not in range")
        self.bus.i2c_writeto_mem(self.addr, 0xFE, prescaleval.to_bytes(1, 'big'))

class LedCell:
    def __init__(self, ledcontroller: LedController, is_first_on_led_controller):
        self.ledcontroller = ledcontroller
        self.is_first_on_led_controller = is_first_on_led_controller

    def setmain(self, register_address, value):
        i2c_address = self.ledcontroller.addr
        new_value = int((value * 4095) / 100)
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
        self.setmain(register_address, value)

    def setblue(self, value):
        # value: 0-100
        if self.is_first_on_led_controller:
            pin = LedController.LedBlue1
        else:
            pin = LedController.LedBlue2

        if pin == 2:
            register_address = 0x0E
        else:
            register_address = 0x26
        self.setmain(register_address, value)

    def setgreen(self, value):
        # value: 0-100
        if self.is_first_on_led_controller:
            pin = LedController.LedGreen1
        else:
            pin = LedController.LedGreen2

        if pin == 3:
            register_address = 0x12
        else:
            register_address = 0x2A
        self.setmain(register_address, value)

    def setwhite(self, value):
        # value: 0-100
        if self.is_first_on_led_controller:
            pin = LedController.LedWhite1
        else:
            pin = LedController.LedWhite2

        if pin == 4:
            register_address = 0x16
        else:
            register_address = 0x2E
        self.setmain(register_address, value)

    def setUV(self, value):
        # value: 0-100
        if self.is_first_on_led_controller:
            pin = LedController.LedUV1
        else:
            pin = LedController.LedUV2

        if pin == 5:
            register_address = 0x1A
        else:
            register_address = 0x32
        self.setmain(register_address, value)

    def setIR(self, value):
        # value: 0-100
        if self.is_first_on_led_controller:
            pin = LedController.LedIR1
        else:
            pin = LedController.LedIR2

        if pin == 6:
            register_address = 0x1E
        else:
            register_address = 0x36
        self.setmain(register_address, value)
