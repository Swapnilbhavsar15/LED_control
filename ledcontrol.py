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
    addr_dict = { "LED1_ON_L" : 0x0A,
                  "LED1_ON_H" : 0x0B,
                  "LED1_OFF_L" : 0x0C,
                  "LED1_OFF_H" : 0x0D,
                  "LED2_ON_L" : 0x0E,
                  "LED2_ON_H" : 0x0F,
                  "LED2_OFF_L" : 0X10,
                  "LED2_OFF_H" : 0x11,
                  "LED3_ON_L" : 0x12,
                  "LED3_ON_H" : 0x13,
                  "LED3_OFF_L" : 0x14,
                  "LED3_OFF_H" : 0x15,
                  "LED4_ON_L" : 0x16,
                  "LED4_ON_H" : 0x17,
                  "LED4_OFF_L" : 0x18,
                  "LED4_OFF_H" : 0x19,
                  "LED5_ON_L" : 0x1A,
                  "LED5_ON_H" : 0x1B,
                  "LED5_OFF_L" : 0x1C,
                  "LED5_OFF_H" : 0x1D,
                  "LED6_ON_L" : 0x1E,
                  "LED6_ON_H" : 0x1F,
                  "LED6_OFF_L" : 0x20,
                  "LED6_OFF_H" : 0x21,
                  "LED7_ON_L" : 0x22,
                  "LED7_ON_H" : 0x23,
                  "LED7_OFF_L" : 0x24,
                  "LED7_OFF_H" : 0x25,
                  "LED8_ON_L" : 0x26,
                  "LED8_ON_H" : 0x27,
                  "LED8_OFF_L" : 0x28,
                  "LED8_OFF_H" : 0x29,
                  "LED9_ON_L" : 0x2A,
                  "LED9_ON_H" : 0x2B,
                  "LED9_OFF_L" : 0x2C,
                  "LED9_OFF_H" : 0x2D,
                  "LED10_ON_L" : 0x2E,
                  "LED10_ON_H" : 0x2F,
                  "LED10_OFF_L" : 0x30,
                  "LED10_OFF_H" : 0x31,
                  "LED11_ON_L" : 0x32,
                  "LED11_ON_H" : 0x33,
                  "LED11_OFF_L" : 0x34,
                  "LED11_OFF_H" : 0x35,
                  "LED12_ON_L" : 0x36,
                  "LED12_ON_H" : 0x37,
                  "LED12_OFF_L" : 0x38,
                  "LED12_OFF_H" : 0x39}

    def __init__(self, ledcontroller: LedController, is_first_on_led_controller):
        self.ledcontroller = ledcontroller
        self.is_first_on_led_controller = is_first_on_led_controller


    def setmain(self, register_address, value):
        i2c_address = self.ledcontroller.addr
        new_val = int((value*4096)/100)
        self.ledcontroller.bus.i2c_writeto_mem(i2c_address, register_address, new_val.to_bytes(2, byteorder='little'))

    def setPWM(self, register_address, value, delay):
        if value+delay <= 100:
            self.setmain(register_address, delay)
            self.setmain(register_address, delay+value)
        elif value+delay > 100:
            self.setmain(register_address, delay)
            self.setmain(register_address, delay+value-100)


    def setred(self, value):
        # value: 0-100
        delay = 10
        if self.is_first_on_led_controller:
            pin = LedController.LedRed1
        else:
            pin = LedController.LedRed2

        if pin == 1:
            self.setPWM(self.addr_dict["LED1_ON_L"], value, delay)
        else:
            self.setPWM(self.addr_dict["LED7_ON_L"], value, delay)


    def setblue(self, value):
        # value: 0-100
        delay = 20
        if self.is_first_on_led_controller:
            pin = LedController.LedBlue1
        else:
            pin = LedController.LedBlue2

        if pin == 2:
            self.setPWM(self.addr_dict["LED2_ON_L"], value, delay)
        else:
            self.setPWM(self.addr_dict["LED8_ON_L"], value, delay)

    def setgreen(self, value):
        # value: 0-100
        delay = 30
        if self.is_first_on_led_controller:
            pin = LedController.LedGreen1
        else:
            pin = LedController.LedGreen2

        if pin == 3:
            self.setPWM(self.addr_dict["LED3_ON_L"], value, delay)
        else:
            self.setPWM(self.addr_dict["LED9_ON_L"], value, delay)

    def setwhite(self, value):
        # value: 0-100
        delay = 40
        if self.is_first_on_led_controller:
            pin = LedController.LedWhite1
        else:
            pin = LedController.LedWhite2

        if pin == 4:
            self.setPWM(self.addr_dict["LED4_ON_L"], value, delay)
        else:
            self.setPWM(self.addr_dict["LED10_ON_L"], value, delay)

    def setUV(self, value):
        # value: 0-100
        delay = 50
        if self.is_first_on_led_controller:
            pin = LedController.LedUV1
        else:
            pin = LedController.LedUV2

        if pin == 5:
            self.setPWM(self.addr_dict["LED5_ON_L"], value, delay)
        else:
            self.setPWM(self.addr_dict["LED11_ON_L"], value, delay)

    def setIR(self, value):
        # value: 0-100
        delay = 60
        if self.is_first_on_led_controller:
            pin = LedController.LedIR1
        else:
            pin = LedController.LedIR2

        if pin == 6:
            self.setPWM(self.addr_dict["LED6_ON_L"], value, delay)
        else:
            self.setPWM(self.addr_dict["LED12_ON_L"], value, delay)