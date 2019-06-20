#!/usr/bin/env python

from rospy_websocker_client import WebsocketROSClient as ros_ws
from std_msgs.msg import String 
from geometry_msgs.msg import  PoseStamped
import rospy
from geometry_msgs.msg import Twist

def listener():
  rospy.init_node('listener',anonymous=True)

  # Websocket client
#  ws_client = ros_ws.ws_client('192.168.1.3', 3000) # ip, port, name of client
  ws_client = ros_ws.ws_client('147.47.91.124', 10) # ip, port, name of client
  
  # Subscribe
  ws_client.subscribe('/listener', String(), '/listener')

  # Publish
  msg = Twist()
  msg.linear.x = 999
  ws_client.connect()
  ws_client.publish("/cmd_vel",msg)

  rospy.spin()

if __name__=="__main__":
  try:
    print("Try listener");
    listener()
  except:
    print("Exception!");
    pass
