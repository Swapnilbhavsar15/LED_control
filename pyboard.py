from machine import I2C
from ledcontrol import I2cAbstraction


class PybI2c(I2cAbstraction):
    def __init__(self):
        super.__init__(self, scl, sda, freq)
        self.i2c = I2C(self.scl, self.sda, self.freq)

    def scan(self):
        I2C.scan()

    def i2c_writeto(self, addr, buf):
        I2C.writeto(addr, buf)

    def i2c_readfrom(self, addr, nbytes):
        I2C.readfrom(addr, nbytes)

    def i2c_readfrom_mem(self, addr, memaddr, nbytes):
        I2C.readfrom_mem(addr, memaddr, nbytes)

    def i2c_writeto_mem(self, addr, memaddr, buf):
        I2C.writeto_mem(addr, memaddr, buf)
