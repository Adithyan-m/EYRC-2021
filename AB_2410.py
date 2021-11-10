#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from rospy.core import loginfo
from turtlesim.msg import Pose
 
ypose = 0.0
xpose = 0.0
roundy = 0.0
yinit = 0.0
xinit = 0.0
y = 0
x = 0
z = 0
tinit = 0
def callback(position):
   global ypose
   global roundy
   global x
   global y
   global yinit
   global xinit
   global xpose
   xpose = position.x
   ypose = position.y
   roundy = round(ypose,2)
   while x == 0:
       xinit = position.x
       yinit = position.y
       x = 1
 
def infinity():
  
   global ypose
   global roundy
   global x
   global y
   global z
   global yinit
   global xinit
   global xpose 
   global tinit
   rospy.init_node('turtle_revolve', anonymous=False)
   pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
   rospy.Subscriber('/turtle1/pose',Pose,callback)
 
   velocity = Twist()
   position = Pose()
   rate = rospy.Rate(10) #10Hz
   rate2 = rospy.Rate(1)
   rospy.loginfo("Moving the bot")
   radius = 1
 
   while not rospy.is_shutdown():
       seconds = rospy.get_time()
       while y == 0:
           tinit = rospy.get_time()
           y = 1

       if z == 0:
           velocity.linear.x = 1
           velocity.angular.z = -1/radius
           pub.publish(velocity)
           rospy.loginfo("moving bot circle 1")

           if (yinit-ypose<0.001 and seconds-tinit>6):
               z = 1
       elif z==1:
           velocity.linear.x = 1
           velocity.angular.z = 1/radius
           pub.publish(velocity)
           rospy.loginfo("moving bot circle 2")
           if (ypose-yinit<0.532 and seconds-tinit>11):
               z = 2
       else:
           rospy.loginfo("current y = %f",roundy)
           loginfo("task complete")
           break
    
       rate.sleep()
 
 
if __name__=='__main__':
   try:
       infinity()
   except rospy.ROSInterruptException:
       pass
