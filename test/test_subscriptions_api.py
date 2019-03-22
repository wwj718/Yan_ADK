# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import openadk
from openadk.api.subscriptions_api import SubscriptionsApi  # noqa: E501
from openadk.rest import ApiException


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = openadk.api.subscriptions_api.SubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_put_motions(self):
        """Test case for put_motions

        推送运动控制状态  # noqa: E501
        """
        pass

    def test_put_sensors_subscription(self):
        """Test case for put_sensors_subscription

        推送传感器消息  # noqa: E501
        """
        pass

    def test_put_sensors_subscription_sensors_environment(self):
        """Test case for put_sensors_subscription_sensors_environment

        推送传感器消息  # noqa: E501
        """
        pass

    def test_put_sensors_subscription_sensors_infrared(self):
        """Test case for put_sensors_subscription_sensors_infrared

        推送传感器消息  # noqa: E501
        """
        pass

    def test_put_sensors_subscription_sensors_pressure(self):
        """Test case for put_sensors_subscription_sensors_pressure

        推送传感器消息  # noqa: E501
        """
        pass

    def test_put_sensors_subscription_sensors_touch(self):
        """Test case for put_sensors_subscription_sensors_touch

        推送传感器消息  # noqa: E501
        """
        pass

    def test_put_sensors_subscription_sensors_ultrasonic(self):
        """Test case for put_sensors_subscription_sensors_ultrasonic

        推送传感器消息  # noqa: E501
        """
        pass

    def test_put_tts_subscriptions_voice_tts(self):
        """Test case for put_tts_subscriptions_voice_tts

        推送TTS状态消息  # noqa: E501
        """
        pass

    def test_put_vision_subscription_visions(self):
        """Test case for put_vision_subscription_visions

        推送指定视觉任务消息  # noqa: E501
        """
        pass

    def test_put_voice_asr_subscriptions_voice_asr(self):
        """Test case for put_voice_asr_subscriptions_voice_asr

        推送语义理解消息  # noqa: E501
        """
        pass

    def test_put_voice_iat_subscription_voice_iat(self):
        """Test case for put_voice_iat_subscription_voice_iat

        推送语音识别原始JSON信息  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
