#!/usr/bin/env python

from rospy_websocker_client import WebsocketROSClient as ros_ws
from std_msgs.msg import String 
from geometry_msgs.msg import  PoseStamped
import rospy
from geometry_msgs.msg import Twist

def ws_subscribe(_ws_client, topic_name, topic_type, topic_name_published):
  if topic_type=='std_msgs/String':
    _ws_client.subscribe(topic_name,String(),topic_name_published)
  elif topic_type=='geometry_msgs/Twist':
    _ws_client.subscribe(topic_name,Twist(),topic_name_published)
  elif topic_type=='geometry_msgs/PoseStamped':
    _ws_client.subscribe(topic_name,PoseStamped(),topic_name_published)
  else:
    rospy.logerr("Unknwon topic type.")


def ws_sub_node():
  print "ws_sub_node"
  rospy.init_node('listener',anonymous=True)

  port = rospy.get_param('~port',3000)
  print "Flag1-1-1. port:",port
  address = rospy.get_param('~address','127.0.0.1')
  print "Flag1-1-2. address:",address
  subscribe_topics = rospy.get_param('~subscribe_topics','')[1:-1].split(',')

  # Websocket client
#  ws_client = ros_ws.ws_client('192.168.1.3', 3000) # ip, port, name of client
  ws_client = ros_ws.ws_client('147.47.91.124', 10) # ip, port, name of client
  
  # Server to client
  for topic in subscribe_topics:
    print "Flag1-1-3. subs_topic:",topic
    topic_name = topic.split(':')[0]
    topic_type = topic.split(':')[1]
    topic_name_published = topic.split(':')[2]
    ws_subscribe(ws_client, topic_name, topic_type, topic_name_published)
#    rospy.sleep(1)
#    ws_client.subscribe(topic_name, topic_type, topic_name_published)
#ws_client.subscribe('/listener', String(), '/listener')
  msg = Twist()
  rate = rospy.Rate(1);
  ws_client.connect()
#  rospy.spin()
#  print "Flag1-1-5"
  msg_index = 0
  while not rospy.is_shutdown():
    msg.linear.x = msg_index
    ws_client.publish("/cmd_vel",msg)
    msg_index = msg_index + 1.0
#rospy.sleep(1)
    rate.sleep()

#def ws_pub_node():
#  print "ws_pub_node"
#  ws_client = ros_ws.ws_client('147.47.91.124', 10) # ip, port, name of client
## Publish
#  rate = rospy.Rate(10)
#  msg = Twist()
#  msg_index = 0
#  ws_client.connect()


if __name__=="__main__":
  try:
    ws_sub_node()
#    ws_pub_node()
  except rospy.ROSInterruptException:
    print("Exception!")
    pass
