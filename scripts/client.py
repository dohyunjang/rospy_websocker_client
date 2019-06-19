#!/usr/bin/env python

from rospy_websocker_client import WebsocketROSClient as ros_ws
from std_msgs.msg import String 
from geometry_msgs.msg import  PoseStamped
import rospy

def listener():
  rospy.init_node('listener',anonymous=True)

  ws_client = ros_ws.ws_client('192.168.1.3', 3000) # ip, port, name of client
  ws_client.connect()

          # 1. The name of the topic server;
          # 2. The type of topic
          # 3. The name of the topic where to publish
          # 4. Frame rate: default = 0
          # 5. queue_length:  default = 0

  ws_client.subscribe('/server/hello', String(), '/erver/hello')
  rospy.spin()

if __name__=="__main__":
  try:
    listener()
  except:
    pass
