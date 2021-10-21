#!/usr/bin/env python
#-*- coding: utf-8 -*-

import roslib
import rospy
from voice_common_pkg.srv import *
from gpsr_answer.srv import GPSR

tts_pub = rospy.ServiceProxy('/tts', TTS)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)


def main():
    cnt = 0
    gpsr = rospy.ServiceProxy('/gpsr_conversation_srvserver',GPSR)
    print "Are you ready?"
    tts_pub('Are you ready?')
    for i in range(10):
        tts_pub('Talk to me.')
        result = gpsr().result
        if result == True:
            cnt += 1

    print cnt

if __name__ == '__main__':
    rospy.init_node('voice_sample_last')
    main()
