from ledcontrol import I2cAbstraction


class MachineI2c(I2cAbstraction):
    def __init__(self, i2c):
        self.i2c = i2c

    def scan(self):
        self.i2c.scan()

    def i2c_writeto(self, addr, buf):
        self.i2c.writeto(addr, buf)

    def i2c_readfrom(self, addr, nbytes):
        self.i2c.readfrom(addr, nbytes)

    def i2c_readfrom_mem(self, addr, memaddr, nbytes):
        self.i2c.readfrom_mem(addr, memaddr, nbytes)

    def i2c_writeto_mem(self, addr, memaddr, buf):
        self.i2c.writeto_mem(addr, memaddr, buf)

class PybI2c(I2cAbstraction):
    def __init__(self, i2c):
        self.i2c = i2c

    def scan(self):
        self.i2c.scan()

    def i2c_writeto(self, addr, buf):
        self.i2c.writeto(addr, buf)

    def i2c_readfrom(self, addr, nbytes):
        self.i2c.readfrom(addr, nbytes)

    def i2c_readfrom_mem(self, addr, memaddr, nbytes):
        self.i2c.mem_read(nbytes, addr, memaddr)

    def i2c_writeto_mem(self, addr, memaddr, buf):
        self.i2c.mem_write(buf, addr, memaddr)
