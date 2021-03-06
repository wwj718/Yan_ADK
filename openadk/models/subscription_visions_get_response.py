# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_visions_results import SubscriptionVisionsResults  # noqa: F401,E501
from openadk import util


class SubscriptionVisionsGetResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code=None, type=None, data=None, timestamp=None, status=None, msg=None):  # noqa: E501
        """SubscriptionVisionsGetResponse - a model defined in Swagger

        :param code: The code of this SubscriptionVisionsGetResponse.  # noqa: E501
        :type code: int
        :param type: The type of this SubscriptionVisionsGetResponse.  # noqa: E501
        :type type: str
        :param data: The data of this SubscriptionVisionsGetResponse.  # noqa: E501
        :type data: SubscriptionVisionsResults
        :param timestamp: The timestamp of this SubscriptionVisionsGetResponse.  # noqa: E501
        :type timestamp: int
        :param status: The status of this SubscriptionVisionsGetResponse.  # noqa: E501
        :type status: str
        :param msg: The msg of this SubscriptionVisionsGetResponse.  # noqa: E501
        :type msg: str
        """
        self.swagger_types = {
            'code': int,
            'type': str,
            'data': SubscriptionVisionsResults,
            'timestamp': int,
            'status': str,
            'msg': str
        }

        self.attribute_map = {
            'code': 'code',
            'type': 'type',
            'data': 'data',
            'timestamp': 'timestamp',
            'status': 'status',
            'msg': 'msg'
        }

        self._code = code
        self._type = type
        self._data = data
        self._timestamp = timestamp
        self._status = status
        self._msg = msg

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionVisionsGetResponse of this SubscriptionVisionsGetResponse.  # noqa: E501
        :rtype: SubscriptionVisionsGetResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this SubscriptionVisionsGetResponse.

        Return code. 0 means success.  # noqa: E501

        :return: The code of this SubscriptionVisionsGetResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this SubscriptionVisionsGetResponse.

        Return code. 0 means success.  # noqa: E501

        :param code: The code of this SubscriptionVisionsGetResponse.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def type(self):
        """Gets the type of this SubscriptionVisionsGetResponse.

         The compute vision's result. The possible \"type\" values: - recognition - tracking - gender - age_group - quantity - color_detect   # noqa: E501

        :return: The type of this SubscriptionVisionsGetResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionVisionsGetResponse.

         The compute vision's result. The possible \"type\" values: - recognition - tracking - gender - age_group - quantity - color_detect   # noqa: E501

        :param type: The type of this SubscriptionVisionsGetResponse.
        :type type: str
        """
        allowed_values = ["recognition", "tracking", "gender", "age_group", "quantity", "color_detect"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def data(self):
        """Gets the data of this SubscriptionVisionsGetResponse.


        :return: The data of this SubscriptionVisionsGetResponse.
        :rtype: SubscriptionVisionsResults
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SubscriptionVisionsGetResponse.


        :param data: The data of this SubscriptionVisionsGetResponse.
        :type data: SubscriptionVisionsResults
        """

        self._data = data

    @property
    def timestamp(self):
        """Gets the timestamp of this SubscriptionVisionsGetResponse.

        Timestamp, Unix standard time.  # noqa: E501

        :return: The timestamp of this SubscriptionVisionsGetResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this SubscriptionVisionsGetResponse.

        Timestamp, Unix standard time.  # noqa: E501

        :param timestamp: The timestamp of this SubscriptionVisionsGetResponse.
        :type timestamp: int
        """

        self._timestamp = timestamp

    @property
    def status(self):
        """Gets the status of this SubscriptionVisionsGetResponse.

        Compute vision's status  # noqa: E501

        :return: The status of this SubscriptionVisionsGetResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubscriptionVisionsGetResponse.

        Compute vision's status  # noqa: E501

        :param status: The status of this SubscriptionVisionsGetResponse.
        :type status: str
        """

        self._status = status

    @property
    def msg(self):
        """Gets the msg of this SubscriptionVisionsGetResponse.

        Return code details.  # noqa: E501

        :return: The msg of this SubscriptionVisionsGetResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this SubscriptionVisionsGetResponse.

        Return code details.  # noqa: E501

        :param msg: The msg of this SubscriptionVisionsGetResponse.
        :type msg: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg
