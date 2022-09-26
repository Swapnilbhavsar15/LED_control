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
    def __init__(self, addr):
        self.addr = addr
        self.LedEn = 0
        self.LedRed1 = 1
        self.LedBlue1 = 2
        self.LedGreen1 = 3
        self.LedWhite1 = 4
        self.LedUV1 = 5
        self.LedIR1 = 6
        self.LedRed2 = 7
        self.LedBlue2 = 8
        self.LedGreen2 = 9
        self.LedWhite2 = 10
        self.LedUV2 = 11
        self.LedIR2 = 12
        self.LedOp1 = 13
        self.LedOp2 = 14


    def read(self, data, memaddr, addr_size, timeout=5000):
        I2cAbstraction.i2c_read(data, self.addr, memaddr, addr_size)

    def write(self, data, memaddr, addr_size, timeout=5000):
        I2cAbstraction.i2c_write(data, self.addr, memaddr, addr_size)

    def recv(self, recv, timeout=5000):
        I2cAbstraction.i2c_recv(recv, self.addr)

    def send(self, send, timeout=5000):
        I2cAbstraction.i2c_send(send, self.addr)

class LedCell(LedController):
    def __init__(self, addr):
        super(). __init__(addr)
