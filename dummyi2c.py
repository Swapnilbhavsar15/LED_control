from ledcontrol import I2cAbstraction


class I2CDummy(I2cAbstraction):
    def __init__(self):
        pass

    def i2c_read(self, data, addr, memaddr, addr_size, timeout=5000):
        print(data, addr, memaddr, addr_size)

    def i2c_write(self, data, addr, memaddr, addr_size, timeout=5000):
        print

    def i2c_recv(self, recv, addr=0x00, timeout=5000):
        pass

    def i2c_send(self, send, addr=0x00, timeout=5000):
        pass
