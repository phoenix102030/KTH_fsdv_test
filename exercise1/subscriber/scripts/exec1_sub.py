#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32, Float32

class exec1_sub:
    def __init__(self):
        rospy.init_node('exec1_sub', anonymous=True)
        self.publisher = rospy.Publisher('/kthfs/result', Float32, queue_size=10)
        rospy.Subscriber('/yang', Int32, self.callback)

    def callback(self, data):
        q = 0.15
        result = data.data / q
        rospy.loginfo('Result: %f', result)
        self.publisher.publish(result)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        node = exec1_sub()
        node.run()
    except rospy.ROSInterruptException:
        pass
