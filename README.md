# LED Controller using PCA9685
The project contains libraries to control different LEDs using the PCA9685 which is 16-channel LED controller

### Docs:
- [PCA9685 Datasheet](https://www.nxp.com/docs/en/data-sheet/PCA9685.pdf)
- [Pyboard Libraries](https://docs.micropython.org/en/latest/pyboard/quickref.html)
- [Raspberry Pi Pico Libraries](https://docs.micropython.org/en/latest/rp2/quickref.html)

### Example:
The following example will set the red LED to maximum intensity.
```python
from ledcontrol import LedCell, LedController
from pyboard import PybI2c
from pyb import I2C

i2c = I2C(1, I2C.CONTROLLER)
i2c_abstraction = PybI2c(i2c)
led_controller = LedController(65, i2c_abstraction, enable=True)
led_cell = LedCell(led_controller, is_first_on_led_controller=False)
led_cell.set_red(100)
```