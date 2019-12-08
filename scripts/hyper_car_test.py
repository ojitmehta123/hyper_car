#! /usr/bin/env python
__author__='Ojit Mehta'
import rospy , time
from geometry_msgs.msg import Twist

rospy.init_node("speed_test", anonymous=True)

class Controller(object):
    def __init__(self):
        self.rate=rospy.Rate(10)
        self.pub=rospy.Publisher("/hyper_car/cmd_vel" , Twist , queue_size = 10)
        self.vel=Twist()
        self.vel_inc = 0.166

    def publish(self):
        """ increasing vel.linear.x for 3 sec and then decreasing for next 3 sec"""
        t0=time.time()
        while not rospy.is_shutdown():
            self.pub.publish(self.vel)
            rospy.loginfo("time:%r velocity:%r"%(time.time()-t0 , self.vel))
            self.vel.linear.x += self.vel_inc

            if time.time() - t0 >= 3:
                self.vel_inc = -0.166

            if time.time() - t0 >= 6:
                self.vel=Twist()
                self.pub.publish(self.vel)
                rospy.loginfo(self.vel)
                return
            time.sleep(0.1)    

if __name__=="__main__":
    rospy.wait_for_service("/gazebo/get_world_properties")
    time.sleep(2.0)
    o=Controller()
    o.publish()

