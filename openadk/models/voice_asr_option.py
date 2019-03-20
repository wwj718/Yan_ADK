# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VoiceAsrOption(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'continues': 'bool',
        'timestamp': 'int'
    }

    attribute_map = {
        'continues': 'continues',
        'timestamp': 'timestamp'
    }

    def __init__(self, continues=None, timestamp=None):  # noqa: E501
        """VoiceAsrOption - a model defined in Swagger"""  # noqa: E501

        self._continues = None
        self._timestamp = None
        self.discriminator = None

        self.continues = continues
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def continues(self):
        """Gets the continues of this VoiceAsrOption.  # noqa: E501

        是否进行连续语意识别, 布尔值, true 需要， false不需要, 默认为false  # noqa: E501

        :return: The continues of this VoiceAsrOption.  # noqa: E501
        :rtype: bool
        """
        return self._continues

    @continues.setter
    def continues(self, continues):
        """Sets the continues of this VoiceAsrOption.

        是否进行连续语意识别, 布尔值, true 需要， false不需要, 默认为false  # noqa: E501

        :param continues: The continues of this VoiceAsrOption.  # noqa: E501
        :type: bool
        """
        if continues is None:
            raise ValueError("Invalid value for `continues`, must not be `None`")  # noqa: E501

        self._continues = continues

    @property
    def timestamp(self):
        """Gets the timestamp of this VoiceAsrOption.  # noqa: E501

        时间戳, Unix标准时间  # noqa: E501

        :return: The timestamp of this VoiceAsrOption.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VoiceAsrOption.

        时间戳, Unix标准时间  # noqa: E501

        :param timestamp: The timestamp of this VoiceAsrOption.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VoiceAsrOption, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VoiceAsrOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
