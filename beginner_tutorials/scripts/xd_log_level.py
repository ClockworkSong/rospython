#!/usr/bin/python
# -*- coding:utf-8 -*-

#================================================================
#   Copyright (C) 2019 Sangfor Ltd. All rights reserved.
#   
#   文件名称：xd_log_level.py
#   创 建 者：Song_xd
#   邮    箱：244549970@qq.com
#   创建日期：2019年01月03日
#   描    述：
#
#================================================================

import rospy
from  std_msgs.msg import String

def log_level():

    debug ="Received a message on topic X from caller Y"
    rospy.logdebug("it is debug: %s", debug)

    info = "Node initialized"
    rospy.loginfo("it is info: %s", info)

    warn = "Could not load configuration file from <path>. Using defaults"
    rospy.logwarn("it is warn: %s", warn)

    error = "Received unexpected NaN value in transform X. Skipping..."
    rospy.logerr("it is error:%s", error)

    fatal = "Motors have caught fire!"
    rospy.logfatal("it is fatal: %s", fatal)


if __name__ == '__main__':

    try:
        rospy.init_node('log_level', anonymous=False, log_level=rospy.DEBUG)
        log_level()
    except rospy.ROSInterruptException :
        pass
