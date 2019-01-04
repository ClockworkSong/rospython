#!/usr/bin/python
# -*- coding:utf-8 -*-


#================================================================
#   Copyright (C) 2018 Sangfor Ltd. All rights reserved.
#   
#   文件名称：xd_add2int.py
#   创 建 者：Song_xd
#   邮    箱：244549970@qq.com
#   创建日期：2018年12月22日
#   描    述：
#
#================================================================

NODE_NAME = 'add_two_ints_node'
SRV_NAME = 'add_two_ints_server'

import rospy
from beginner_tutorials.srv import *

def callback(req):
    # rospy.loginfo("Returning [%ld + %ld = %ld]" % (req.a, req.b, (req.a + req.b)))
    print("Returning [%s + %s = %s]" % (req.a, req.b, (req.a + req.b)))
    sum = int(req.a + req.b)

    return AddTwoIntsResponse(sum)

def add_two_ints_server():
    rospy.init_node(NODE_NAME)
    rospy.Service(SRV_NAME, AddTwoInts, callback)
    
    # spin() keeps Python from exiting until node is shutdown
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()


