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

    def __init__(self, addr, bus: I2cAbstraction, enable=True):
        self.addr = addr
        self.bus = bus
        self.enable = enable
        self.set_enable(enable)

    def setfreq(self, freq):
        """
        The function sets the PWM frequency with the specified value. Default value is 200 Hertz
        :param freq: 24-1526 Hertz
        """
        if 24 <= freq <= 1526:
            prescalevel = round((25000000 / (4096 * freq))) - 1
            self.bus.i2c_writeto_mem(self.addr, 0xFE, prescalevel.to_bytes(1, 'big'))
        else:
            print("Frequency value not in range")

    def set_enable(self, enable):
        """
        The function is used to enable or disable the LED Cell at a particular address.
        """
        self.enable = enable
        if self.enable:
            self.bus.i2c_writeto_mem(self.addr, 0x06, (0).to_bytes(2, 'little'))
            self.bus.i2c_writeto_mem(self.addr, 0x08, (4095).to_bytes(2, 'little'))
        else:
            self.bus.i2c_writeto_mem(self.addr, 0x08, (0).to_bytes(2, 'little'))
            self.bus.i2c_writeto_mem(self.addr, 0x06, (4095).to_bytes(2, 'little'))


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
        self._setmain(register_address, 0)
        self._setmain(register_address + 0x02, value)
        # elif value+delay > 100:
        # self.setmain(register_address, delay)
        # self.setmain(register_address + 0x02, delay+value-100)

    def _get_register(self, pin):
        addr_dict = {0: 0x06, 1: 0x0A, 2: 0x0E, 3: 0x12, 4: 0x16, 5: 0x1A, 6: 0x1E,
                     7: 0x22, 8: 0x26, 9: 0x2A, 10: 0x2E, 11: 0x32, 12: 0x36}
        return addr_dict[pin]

    def set_red(self, value):
        """
        The function turns the Red LED on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the LED
        """
        # delay = 10
        if self.is_first_on_led_controller:
            pin = LedController.LedRed1
        else:
            pin = LedController.LedRed2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def set_blue(self, value):
        """
        The function turns the Blue LED on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the LED
        """
        # delay = 20
        if self.is_first_on_led_controller:
            pin = LedController.LedBlue1
        else:
            pin = LedController.LedBlue2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def set_green(self, value):
        """
        The function turns Green the LED on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the LED
        """
        # delay = 30
        if self.is_first_on_led_controller:
            pin = LedController.LedGreen1
        else:
            pin = LedController.LedGreen2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def set_white(self, value):
        """
        The function turns the White LED on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the LED
        """
        # delay = 40
        if self.is_first_on_led_controller:
            pin = LedController.LedWhite1
        else:
            pin = LedController.LedWhite2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def set_uv(self, value):
        """
        The function turns the Ultraviolet LED on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the LED
        """
        # delay = 50
        if self.is_first_on_led_controller:
            pin = LedController.LedUV1
        else:
            pin = LedController.LedUV2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)

    def set_ir(self, value):
        """
        The function turns the Infrared LED on with desired intensity(brightness) value
        :param value: 0-100 Intensity of the LED
        """
        # delay = 60
        if self.is_first_on_led_controller:
            pin = LedController.LedIR1
        else:
            pin = LedController.LedIR2
        register_address = self._get_register(pin)
        self._setpwm(register_address, value)
