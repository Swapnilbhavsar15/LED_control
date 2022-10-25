class I2cAbstraction:
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
    LedGreen1 = 2
    LedBlue1 = 3
    LedIR1 = 4
    LedUV1 = 5
    LedWhite1 = 6
    LedRed2 = 7
    LedGreen2 = 8
    LedBlue2 = 9
    LedIR2 = 10
    LedUV2 = 11
    LedWhite2 = 12
    LedOp1 = 13
    LedOp2 = 14

    def __init__(self, addr, bus: I2cAbstraction, enable=True):
        self.addr = addr
        self.bus = bus
        self.enable = enable
        self._set_mode()
        self.set_enable(enable)

    def _set_mode(self):
        self.bus.i2c_writeto_mem(self.addr, 0x00, b'\x01')
        self.bus.i2c_writeto_mem(self.addr, 0x01, b'\x14')

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
            self.bus.i2c_writeto_mem(self.addr, 0x08, b'\x00')
            self.bus.i2c_writeto_mem(self.addr, 0x09, b'\x00')
            self.bus.i2c_writeto_mem(self.addr, 0x07, b'\x00')
            self.bus.i2c_writeto_mem(self.addr, 0x06, b'\x00')

        else:
            self.bus.i2c_writeto_mem(self.addr, 0x06, b'\x00')
            self.bus.i2c_writeto_mem(self.addr, 0x07, b'\x10')
            self.bus.i2c_writeto_mem(self.addr, 0x09, b'\x00')
            self.bus.i2c_writeto_mem(self.addr, 0x08, b'\x00')


class LedCell:
    white = 0

    def __init__(self, ledcontroller: LedController, is_first_on_led_controller):
        self.ledcontroller = ledcontroller
        self.is_first_on_led_controller = is_first_on_led_controller

    def _setmain(self, register_address, value):
        i2c_address = self.ledcontroller.addr
        new_val = int(((value * 4096) / 100) - 1)
        if new_val < 0:
            new_val = 0
        if self.white:
            new_val = int(new_val)
        byte_val = new_val.to_bytes(2, 'little')
        self.ledcontroller.bus.i2c_writeto_mem(i2c_address, register_address, byte_val[0:1])
        self.ledcontroller.bus.i2c_writeto_mem(i2c_address, register_address + 0x01, byte_val[1:2])

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
        self.white = 1
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
