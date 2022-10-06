from machine import I2C
from ledcontrol import I2cAbstraction

p_out = Pin('X1', Pin.OUT_PP)
class PybI2c(I2cAbstraction):
    def __init__(self):
        super.__init__(self, scl, sda, freq)
        self.i2c = I2C(self.scl, self.sda, self.freq)

    def scan(self):
        self.i2c.scan()

    def enable(self):
        p_out.high()

    def disable(self):
        p_out.low()

    def i2c_writeto(self, addr, buf):
        self.i2c.writeto(addr, buf)

    def i2c_readfrom(self, addr, nbytes):
        self.i2c.readfrom(addr, nbytes)

    def i2c_readfrom_mem(self, addr, memaddr, nbytes):
        self.i2c.readfrom_mem(addr, memaddr, nbytes)

    def i2c_writeto_mem(self, addr, memaddr, buf):
        self.i2c.writeto_mem(addr, memaddr, buf)
