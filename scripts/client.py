#!/usr/bin/env python

from rospy_websocker_client import WebsocketROSClient as ros_ws
from std_msgs.msg import String 
from geometry_msgs.msg import  PoseStamped
import rospy

def listener():
  rospy.init_node('listener',anonymous=True)

  ws_client = ros_ws.ws_client('192.168.1.3', 3000) # ip, port, name of client
  ws_client.connect()

  # Subscribe
          # 1. The name of the topic server;
          # 2. The type of topic
          # 3. The name of the topic where to publish
          # 4. Frame rate: default = 0
          # 5. queue_length:  default = 0

  ws_client.subscribe('/listener', String(), '/listener')
  
  # Publish
  msg = Twist()
  msg.linear.x = 999
          # 1. the name of the topic on server where to publish; 
          # 2. the message
  ws_client.publish("/cmd_vel",msg)
  rospy.spin()

if __name__=="__main__":
  try:
    listener()
  except:
    print("Exception!");
    pass
