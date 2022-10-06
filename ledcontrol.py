class I2cAbstraction:
    def __init__(self, scl, sda, freq):
        pass

    def scan(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
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


    def __init__(self, addr, bus: I2cAbstraction, enable):
        self.addr = addr
        self.bus = bus
        self.enable = enable

    def setfreq(self, freq):
        if 24 <= freq <= 1526:
            prescalevel = round((25000000 / (4096 * freq))) - 1
            self.bus.i2c_writeto_mem(self.addr, 0xFE, prescalevel.to_bytes(1, 'big'))
        else:
            print("Frequency value not in range")

    def setoutputenable(self):
        if self.enable:
            self.bus.enable()
        else:
            self.bus.disable()

class LedCell:

    def __init__(self, ledcontroller: LedController, is_first_on_led_controller):
        self.ledcontroller = ledcontroller
        self.is_first_on_led_controller = is_first_on_led_controller

    def _setmain(self, register_address, value):
        i2c_address = self.ledcontroller.addr
        new_val = int((value * 4096) / 100)
        self.ledcontroller.bus.i2c_writeto_mem(i2c_address, register_address, new_val.to_bytes(2, byteorder='little'))

    # Add delay parameter if need to be used
    def _setpwm(self, register_address, value):
        # if value+delay <= 100:
        self._setmain(register_address, 0x00)
        self._setmain(register_address + 0x02, value)
        # elif value+delay > 100:
        # self.setmain(register_address, delay)
        # self.setmain(register_address + 0x02, delay+value-100)

    def _get_register(self, pin):
        addr_dict = {1: 0x0A, 2: 0x0E, 3: 0x12, 4: 0x16, 5: 0x1A, 6: 0x1E,
                     7: 0x22, 8: 0x26, 9: 0x2A, 10: 0x2E, 11: 0x32, 12: 0x36}
        return addr_dict[pin]

    def setred(self, value):
        """
        The function turns Red Led on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the Led
        """
        # delay = 10
        if self.is_first_on_led_controller:
            pin = LedController.LedRed1
        else:
            pin = LedController.LedRed2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def setblue(self, value):
        """
        The function turns Blue Led on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the Led
        """
        # delay = 20
        if self.is_first_on_led_controller:
            pin = LedController.LedBlue1
        else:
            pin = LedController.LedBlue2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def setgreen(self, value):
        """
        The function turns Green Led on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the Led
        """
        # delay = 30
        if self.is_first_on_led_controller:
            pin = LedController.LedGreen1
        else:
            pin = LedController.LedGreen2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def setwhite(self, value):
        """
        The function turns White Led on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the Led
        """
        # delay = 40
        if self.is_first_on_led_controller:
            pin = LedController.LedWhite1
        else:
            pin = LedController.LedWhite2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def setuv(self, value):
        """
        The function turns Ultraviolet Led on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the Led
        """
        # delay = 50
        if self.is_first_on_led_controller:
            pin = LedController.LedUV1
        else:
            pin = LedController.LedUV2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def setir(self, value):
        """
        The function turns Infrared Led on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the Led
        """
        # delay = 60
        if self.is_first_on_led_controller:
            pin = LedController.LedIR1
        else:
            pin = LedController.LedIR2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)
