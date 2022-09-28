from dummyi2c import I2CDummy


def test_1():
    i2c = I2CDummy()
    i2c.scan()
    i2c.i2c_writeto(12, b'123')
    i2c.i2c_readfrom(13, 3)
    i2c.i2c_writeto_mem(12, 3, b'\x10')
    i2c.i2c_readfrom_mem(13, 4, 3)