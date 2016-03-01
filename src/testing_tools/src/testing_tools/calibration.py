from blender import *
import rospy
import os
from pau2motors.msg import pau
from topic_tools.srv import MuxSelect
import random

#<node pkg="topic_tools" type="mux" name="neck_pau" args="neck_pau cmd_neck_pau /blender_api/get_pau mux:=neck_pau_mux"/>
#<node pkg="topic_tools" type="mux" name="head_pau" args="head_pau no_pau /blender_api/get_pau mux:=head_pau_mux"/>
#<node pkg="topic_tools" type="mux" name="lips_pau" args="lips_pau head_pau lipsync_pau mux:=lips_pau_mux"/>
#<node pkg="topic_tools" type="mux" name="eyes_pau" args="eyes_pau head_pau eyes_tracking_pau mux:=eyes_pau_mux"/>
eye_pau_select = rospy.ServiceProxy("/sophia_body/eyes_pau_mux/select", MuxSelect)
head_pau_select = rospy.ServiceProxy("/sophia_body/head_pau_mux/select", MuxSelect)
head_pau_select.call("/blender_api/get_pau")
eye_pau_select.call("eyes_tracking_pau")

pub = rospy.Publisher('/blender_api/get_pau', pau, queue_size=1)

def send(pitch, yaw, delta):
    if delta > 0.2 or delta < -0.2:
        return
    msg = pau()
    msg.m_eyeGazeLeftPitch = pitch
    msg.m_eyeGazeLeftYaw = yaw
    msg.m_eyeGazeRightPitch = pitch
    msg.m_eyeGazeRightYaw = yaw
    msg.m_eyeGazeLeftPitch += delta
    msg.m_eyeGazeRightPitch += delta
    msg.m_eyeGazeLeftYaw += delta
    msg.m_eyeGazeRightYaw += delta

    pub.publish(msg)
    print "pub {}".format(msg)

if __name__ == '__main__':
    set_alive(False)
    set_blink_randomly(False)
    set_saccade(False)
    rospy.init_node('calibration')
    r = rospy.Rate(1)

    os.system('rosrun dynamic_reconfigure dynparam set /sophia_body/eye_tracking tracking True')

    delta = 0
    while not rospy.is_shutdown():
        r.sleep()
        send(pitch=0.2, yaw=0, delta=delta)
        delta = -1*delta

    #os.system('rosrun dynamic_reconfigure dynparam set /sophia_body/eye_tracking tracking False')
