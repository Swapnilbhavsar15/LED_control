from scratch import PybI2c


class I2cAbstraction:
    def __init__(self, mode, baudrate):
        pass

    def i2c_read(self, data, addr, memaddr, addr_size, timeout=5000):
        pass

    def i2c_write(self, data, addr, memaddr, addr_size, timeout=5000):
        pass

    def i2c_recv(self, recv, addr=0x00, timeout=5000):
        pass

    def i2c_send(self, send, addr=0x00, timeout=5000):
        pass


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

    def __init__(self, addr):
        self.addr = addr

    def read(self, data, memaddr, addr_size, timeout=5000):
        PybI2c.i2c_read(data, self.addr, memaddr, addr_size)

    def write(self, data, memaddr, addr_size, timeout=5000):
        PybI2c.i2c_write(data, self.addr, memaddr, addr_size)

    def recv(self, recv, timeout=5000):
        PybI2c.i2c_recv(recv, self.addr)

    def send(self, send, timeout=5000):
        PybI2c.i2c_send(send, self.addr)


class LedCell:
    def __init__(self, ledcontroller):
        self.ledcontroller = ledcontroller

    def setred(self, value, isTrue):
        if self.isTrue:
            Pin = LedController.LedRed1
        else:
            Pin = LedController.LedRed2

