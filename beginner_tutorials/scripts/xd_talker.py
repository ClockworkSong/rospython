#!/usr/bin/python
# -*- coding:utf-8 -*-

#================================================================
#   Copyright (C) 2018 Sangfor Ltd. All rights reserved.
#   
#   文件名称：xd_talker.py
#   创 建 者：Song_xd
#   邮    箱：244549970@qq.com
#   创建日期：2018年12月21日
#   描    述：
#
#===============================================================

import rospy
from std_msgs.msg import String
from beginner_tutorials.msg import Num

def talker():
    # pub = rospy.Publisher('chatter_topic', String, queue_size = 10)
    pub = rospy.Publisher('chatter_topic', Num, queue_size = 10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        hello_str = 10086
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
