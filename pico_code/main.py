#motor.py
from machine import Pin, PWM
import time

class Motor:
    def __init__(self, pwm_pin, in1_pin, in2_pin):
        self.pwm = PWM(Pin(pwm_pin), freq=50, duty_u16=8192)
        self.pwm.duty_u16(0) # 0%
        self.dir_pins = (Pin(in1_pin, Pin.OUT), Pin(in2_pin, Pin.OUT))
        
    def forward(self, speed=None):
        self.dir_pins[0].value(0)
        self.dir_pins[1].value(1)
        if speed: self.speed(speed)
        
    def reverse(self, speed=None):
        self.dir_pins[1].value(0)
        self.dir_pins[0].value(1)
        if speed: self.speed(speed)
        
    def stop(self):
        self.dir_pins[0].value(0)
        self.dir_pins[1].value(0)
    
    def speed(self, percent):
        self.pwm.duty_u16(int((percent/100) * 65535)) # 0%
        
#bot.py
class SimpleBot:
    def __init__(self, left_motor, right_motor):
        self.left = left_motor
        self.right = right_motor
        
    def forward(self, speed=50):
        self.left.forward(speed)
        self.right.forward(speed)
        
    def cw(self, speed=50):
        self.left.forward(speed)
        self.right.reverse(speed)
        
    def ccw(self, speed=50):
        self.left.reverse(speed)
        self.right.forward(speed)
        
    def reverse(self, speed=50):
        self.left.forward(speed)
        self.right.forward(speed)
        
    def stop(self):
        self.left.stop()
        self.right.stop()
        

l, r = Pin(11, Pin.PULL_DOWN), Pin(9, Pin.PULL_DOWN)
values = [0, 0]

SPEED=50

#line following test
m = Motor(12, 10, 7)
n = Motor(3, 4, 6)

def say(_l, _r):
    if _r and _l:
        print("reverse (blocked)")
    elif _l:
        print("ccw (steer right)")
    elif _r:
        print("cw (steer left)")
    else:
        print("forward (on the line)")

bot = SimpleBot(m, n)
_l, _r = 0, 0
while True:
    _l = l.value()
    if _l != values[0]:
        print("9 (left) became", _l)
        values[0] = _l
        say(_l, _r)

    _r = r.value()
    if _r != values[1]:
        print("11 (right) became", _r)
        values[1] = _r
        say(_l, _r)
    
    if _r and _l:
        bot.reverse(SPEED)
    elif _l:
        bot.ccw(SPEED)
    elif _r:
        bot.cw(SPEED)
    else:
        bot.forward(SPEED)
    time.sleep(0.025)
