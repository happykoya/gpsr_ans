#!/usr/bin/env python
#-*- coding: utf-8 -*-

import roslib
import rospy
from voice_common_pkg.srv import TTS, SpeechToText

from gpsr_answer.srv import GPSR, GPSRResponse
import lp_gpsr

tts_pub = rospy.ServiceProxy('/tts', TTS)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)

file_name = "Questions.xml"
#file_path = roslib.packages.get_pkg_dir("GPSRCmdGen") + "/CommonFiles/" + file_name
lp = lp_gpsr.Selector(file_name)


def speak(sentence):
    tts_pub(sentence)
    return

def speechRecog():
    return stt_pub()

def conversation(_dammy):
    ros_response = GPSRResponse()

    # recognition result
    sentence = speechRecog()
    print(sentence)
    result_list = lp.checker(sentence.result_str)

    if all(result_list):
        speak("Question is")
        speak(result_list[0])
        speak("Answer is")
        speak(result_list[1])
        ros_response.result = True
    else:
        speak("Sorry I couldn't be recognized")
        ros_response.result = False

    return ros_response

def rosConfig():
    rospy.init_node('gpsr_conversation_srvserver')
    rospy.Service('/gpsr_conversation_srvserver', GPSR, conversation)
    rospy.loginfo('Ready to  conversation_srvserver')
    rospy.spin()

if __name__ == '__main__':
    rosConfig()
