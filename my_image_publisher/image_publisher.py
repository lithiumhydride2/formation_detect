#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def main():
    rospy.init_node('image_publisher', anonymous=True)
    image_pub = rospy.Publisher('image_topic', Image, queue_size=10)
    rate = rospy.Rate(10)  # 设置发布频率为10Hz

    bridge = CvBridge()

    while not rospy.is_shutdown():
        try:
            # 读取图像文件
            img = cv2.imread('/home/liuchen/catkin_ws/src/my_image_publisher/need4.jpg')
            # print(img)
            # 将OpenCV图像转换为ROS图像消息
            img_msg = bridge.cv2_to_imgmsg(img, encoding="bgr8")
            # 发布图像消息
            image_pub.publish(img_msg)
            rate.sleep()
        except Exception as e:
            rospy.logerr(e)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
