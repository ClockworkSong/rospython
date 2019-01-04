#!/usr/bin/python
# -*- coding:utf-8 -*-

#================================================================
#   Copyright (C) 2018 Sangfor Ltd. All rights reserved.
#   
#   文件名称：xd_add2int_cli.py
#   创 建 者：Song_xd
#   邮    箱：244549970@qq.com
#   创建日期：2018年12月22日
#   描    述：
#
#================================================================

SRV_NAME = 'add_two_ints_server'
# imports the AddTwoInts service 
from rospy_tutorials.srv import *
import rospy

## add two numbers using the add_two_ints service
## @param x int: first number to add
## @param y int: second number to add
def add_two_ints_client(x, y):

    # NOTE: you don't have to call rospy.init_node() to make calls against
    # a service. This is because service clients do not have to be
    # nodes.

    # block until the add_two_ints service is available
    # you can optionally specify a timeout
    rospy.wait_for_service(SRV_NAME)
    
    try:
        # create a handle to the add_two_ints service
        add_two_ints = rospy.ServiceProxy(SRV_NAME, AddTwoInts)
        
        print "Requesting %s+%s"%(x, y)
        
        # simplified style
        resp1 = add_two_ints(x, y)

        # formal style
        resp2 = add_two_ints.call(AddTwoIntsRequest(x, y))

        if not resp1.sum == (x + y):
            raise Exception("test failure, returned sum was %s"%resp1.sum)
        if not resp2.sum == (x + y):
            raise Exception("test failure, returned sum was %s"%resp2.sum)
        return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    
    argv = rospy.myargv()
    if len(argv) == 1:
        import random
        x = random.randint(-50000, 50000)
        y = random.randint(-50000, 50000)
    elif len(argv) == 3:
        try:
            x = int(argv[1])
            y = int(argv[2])
        except:
            print usage()
            sys.exit(1)
    else:
        print usage()
        sys.exit(1)
    print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
