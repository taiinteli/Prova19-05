import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from collections import deque
import time
import math

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.move_turtle)
        self.twist_msg_ = Twist()

class Fila(list):
    def __init__(self, lista): 
        super().__init__(item for item in lista)

    def push(self, x):
        super().append(x)

    def pop(self):
        return super().pop(0)

    def __repr__(self):
        return super().__repr__()

def move_turtle():
    f = Fila([0.0, 0.5, 0.0, 0.5, 0.0, 1.0])
    print(f)
    f.push(f)
    print(f)
    f.pop(f)
    f.pop(f)
    print(f)

    f = Fila([0.5, 0.0, 0.5, 0.0, 1.0, 0.0])
    print(f)
    f.push(f)
    print(f)
    f.pop(f)
    f.pop(f)
    print(f)

def main(args=None):
    rclpy.init(args=args)
    tc = TurtleController(Pose(x=1.0, y=0.0))
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()