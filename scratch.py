from pyb import I2C
from main import I2cAbstraction

class PybI2c(I2cAbstraction):
    def __init__(self):
        super(). __init__(self, mode, baudrate)
    def read(self, data, addr, memaddr, addr_size, timeout=5000):
        I2C.mem_read(data, addr, memaddr, timeout=5000, addr_size=8)
    def write(self, data, addr, memaddr, addr_size, timeout=5000):
        I2C.mem_write(data, addr, memaddr, timeout=5000, addr_size=8)
    def recv(self, recv, addr=0x00, timeout=5000):
        I2C.recv(recv, addr=0x00, timeout=5000)
    def send(self, send, addr=0x00, timeout=5000):
        I2C.send(send, addr=0x00, timeout=5000)

