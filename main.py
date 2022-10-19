from ledcontrol import LedCell, LedController
from pyboard import PybI2c

from pyb import I2C
def test():
    led_controller.set_enable(True)
    led_cell.set_red(50)

i2c = I2C(1, I2C.CONTROLLER)

i2c_abstraction = PybI2c(i2c)

led_controller = LedController(65, i2c_abstraction, enable=True)

led_cell = LedCell(led_controller, is_first_on_led_controller=False)

