#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

class exec1_pub:
    def __init__(self):
        self.pub = rospy.Publisher('/yang', Int32, queue_size=10)
        rospy.init_node('exec1_pub', anonymous=True)
        self.rate = rospy.Rate(20) # 20hz
        self.n = 4
        self.k = 0

    def run(self):
        while not rospy.is_shutdown():
            self.k = self.k + self.n
            rospy.loginfo("Publishing: %d", self.k)
            self.pub.publish(self.k)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        node = exec1_pub()
        node.run()
    except rospy.ROSInterruptException:
        pass
