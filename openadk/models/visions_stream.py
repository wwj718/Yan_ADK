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


class VisionsStream(object):
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
        'resolution': 'str',
        'url': 'str'
    }

    attribute_map = {
        'resolution': 'resolution',
        'url': 'url'
    }

    def __init__(self, resolution=None, url=None):  # noqa: E501
        """VisionsStream - a model defined in Swagger"""  # noqa: E501

        self._resolution = None
        self._url = None
        self.discriminator = None

        if resolution is not None:
            self.resolution = resolution
        self.url = url

    @property
    def resolution(self):
        """Gets the resolution of this VisionsStream.  # noqa: E501

        视频分辨率。默认视频分辨率为1024x768，最大视频分辨率为1920x1080  # noqa: E501

        :return: The resolution of this VisionsStream.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this VisionsStream.

        视频分辨率。默认视频分辨率为1024x768，最大视频分辨率为1920x1080  # noqa: E501

        :param resolution: The resolution of this VisionsStream.  # noqa: E501
        :type: str
        """

        self._resolution = resolution

    @property
    def url(self):
        """Gets the url of this VisionsStream.  # noqa: E501

        推送地址。 url 合法形式 webrtc://(ip):(port) 或者 udp://(ip):(port)  # noqa: E501

        :return: The url of this VisionsStream.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this VisionsStream.

        推送地址。 url 合法形式 webrtc://(ip):(port) 或者 udp://(ip):(port)  # noqa: E501

        :param url: The url of this VisionsStream.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

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
        if issubclass(VisionsStream, dict):
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
        if not isinstance(other, VisionsStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other