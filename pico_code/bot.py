from motor import Motor

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
        self.left.reverse(speed)
        self.right.reverse(speed)
        
    def stop(self):
        self.left.stop()
        self.right.stop()

