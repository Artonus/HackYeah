from simple_pid import PID
from Motor import Motor
import time

pid = PID(3, 0, 0, setpoint=5)

# assume we have a system we want to control in controlled_system
m = Motor(3.5)
v = m.update(0)

while True:
    # compute new ouput from the PID according to the systems current value
    control = pid.__call__(v)
    # feed the PID output to the system and get its current value
    v = m.update(control)
    print("control",control)
    print("position",m.getPosition())
    time.sleep(1)