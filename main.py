from find_circles import run
from simple_pid import PID
from Motor import Motor
from time import sleep
import ConectionManager
import math

target = 15
connection = ConectionManager.Connection()

pid = PID(0.1, 0, 0, setpoint=target)
# motor = Motor(init_state)

# def controller(angle):
    # print(angle)
    #TODO: IMPLEMENT PID
    #TEST 1
# pwm(0.5, 0.07, "clkWise")
    #TEST 2
    #print(angle)
    #TEST 3
    # control = pid(angle)
    # if control > 0:
    #     pwm(0.2, control/(2*math.pi), "clkWise")
    # else if control < 0:
    #     pwm(0.2,control/(2*math.pi), "ctrClkWise")
    # else 
    #     connection.sendCommand("stop", 0)

def pwm(period, value, rotation):
    if rotation == "clkWise":
        connection.sendCommand("move", "rigth")
        connection.sendCommand("freq", "1")
        connection.disconnect()
    else:
        connection.sendCommand("move", "left")
        connection.sendCommand("freq", "1")
        connection.disconnect()

    sleep(period*value)
    connection.sendCommand("move", "stop")
    sleep(period - period*value)   

while True:
    pwm(1,0.07,"clWise")
# run(controller, display=True)
# connection.sendCommand("move", "left")
# connection.sendCommand("freq", "15")
# connection.disconnect()