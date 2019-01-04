#!/usr/bin/python
# -*- coding:utf-8 -*-

#================================================================
#   Copyright (C) 2018 Sangfor Ltd. All rights reserved.
#   
#   文件名称：xd_listener.py
#   创 建 者：Song_xd
#   邮    箱：244549970@qq.com
#   创建日期：2018年12月21日
#   描    述：
#
#================================================================

import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Num

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    rospy.loginfo(rospy.get_caller_id() + 'I heard %ld', data.num)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    # rospy.Subscriber('chatter_topic', String, callback)
    rospy.Subscriber('chatter_topic', Num, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
