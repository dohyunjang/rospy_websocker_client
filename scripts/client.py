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

def string_cb(data, args):
  ws_client = args[0]
  give_topic_name = args[1]
  ws_client.publish(give_topic_name, data)

def ws_client_node():
  rospy.init_node('websocket_client',anonymous=True)

  # Parsing parameters
  port = rospy.get_param('~port',3000)
  print "Flag1-1-1. port:",port
  address = rospy.get_param('~address','127.0.0.1')
  print "Flag1-1-2. address:",address
  server_pub_topics = rospy.get_param('~server_pub_topics','')[1:-1].split(',')
  client_pub_topics = rospy.get_param('~client_pub_topics','')[1:-1].split(',')

# Websocket client
#  ws_client = ros_ws.ws_client('192.168.1.3', 3000) # ip, port, name of client
#  ws_client = ros_ws.ws_client('147.47.91.124', 10) # ip, port, name of client
  ws_client = ros_ws.ws_client(address, port) # ip, port, name of client
  
  # Server to client
  for topic in server_pub_topics:
    receive_topic_name = topic.split(':')[0]
    topic_type = topic.split(':')[1]
    give_topic_name = topic.split(':')[2]
    ws_subscribe(ws_client, receive_topic_name, topic_type, give_topic_name)

  ws_client.connect()

  # Client to server
  for topic in client_pub_topics:
    print "Flag1-1-3. subs_topic:",topic
    receive_topic_name = topic.split(':')[0]
    topic_type = topic.split(':')[1]
    give_topic_name = topic.split(':')[2]
    rospy.Subscriber(receive_topic_name,String,string_cb,(ws_client, give_topic_name))

  rospy.spin()


if __name__=="__main__":
  try:
    ws_client_node()
  except rospy.ROSInterruptException:
    print("Exception!")
    pass
