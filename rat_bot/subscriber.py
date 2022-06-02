#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


right_turn =  rospy.Publisher('/rat_bot/front_right_axle_revolute_controller/command', Float64, queue_size=10)
left_turn = rospy.Publisher('/rat_bot/front_left_axle_revolute_controller/command', Float64, queue_size=10)
rear_wheel = rospy.Publisher('/rat_bot/rear_axle_continuous_controller/command', Float64, queue_size=10)
twist = Float64()


def straight_push(data):
    rospy.loginfo(rospy.get_caller_id() + "data received %f", data.data)
    rear_wheel.publish(data.data)

def turn_push(data):
    rospy.loginfo(rospy.get_caller_id() + "data received %f", data.data)
    right_turn.publish(data.data)
    left_turn.publish(0)
    


def listener():
 
    rospy.init_node('motor_controller', anonymous=True)

    rospy.Subscriber("straight_motion", Float64, straight_push)
    rospy.Subscriber("turn", Float64, turn_push)

    rospy.spin()
 
if __name__ == '__main__':
    listener()