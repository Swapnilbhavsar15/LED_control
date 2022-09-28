from ledcontrol import I2cAbstraction


class I2CDummy(I2cAbstraction):
    def __init__(self):
        pass

    def scan(self):
        print("scanned")

    def i2c_writeto(self, addr, buf):
        print(addr, buf)

    def i2c_readfrom(self, addr, nbytes):
        print(addr, nbytes)

    def i2c_readfrom_mem(self, addr, memaddr, nbytes):
        print(addr, memaddr, nbytes)

    def i2c_writeto_mem(self, addr, memaddr, buf):
        print(addr, memaddr, buf)
