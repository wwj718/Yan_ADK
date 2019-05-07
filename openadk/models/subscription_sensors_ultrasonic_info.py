# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk import util


class SubscriptionSensorsUltrasonicInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id=None, slot=None, value=None):  # noqa: E501
        """SubscriptionSensorsUltrasonicInfo - a model defined in Swagger

        :param id: The id of this SubscriptionSensorsUltrasonicInfo.  # noqa: E501
        :type id: int
        :param slot: The slot of this SubscriptionSensorsUltrasonicInfo.  # noqa: E501
        :type slot: int
        :param value: The value of this SubscriptionSensorsUltrasonicInfo.  # noqa: E501
        :type value: int
        """
        self.swagger_types = {
            'id': int,
            'slot': int,
            'value': int
        }

        self.attribute_map = {
            'id': 'id',
            'slot': 'slot',
            'value': 'value'
        }

        self._id = id
        self._slot = slot
        self._value = value

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionSensorsUltrasonicInfo of this SubscriptionSensorsUltrasonicInfo.  # noqa: E501
        :rtype: SubscriptionSensorsUltrasonicInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SubscriptionSensorsUltrasonicInfo.

        传感器地址  # noqa: E501

        :return: The id of this SubscriptionSensorsUltrasonicInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionSensorsUltrasonicInfo.

        传感器地址  # noqa: E501

        :param id: The id of this SubscriptionSensorsUltrasonicInfo.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id > 127:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `127`")  # noqa: E501
        if id is not None and id < 1:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def slot(self):
        """Gets the slot of this SubscriptionSensorsUltrasonicInfo.

        传感器槽位号  # noqa: E501

        :return: The slot of this SubscriptionSensorsUltrasonicInfo.
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this SubscriptionSensorsUltrasonicInfo.

        传感器槽位号  # noqa: E501

        :param slot: The slot of this SubscriptionSensorsUltrasonicInfo.
        :type slot: int
        """
        if slot is not None and slot > 6:  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value less than or equal to `6`")  # noqa: E501
        if slot is not None and slot < 1:  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value greater than or equal to `1`")  # noqa: E501

        self._slot = slot

    @property
    def value(self):
        """Gets the value of this SubscriptionSensorsUltrasonicInfo.

        距离值，单位毫米  # noqa: E501

        :return: The value of this SubscriptionSensorsUltrasonicInfo.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SubscriptionSensorsUltrasonicInfo.

        距离值，单位毫米  # noqa: E501

        :param value: The value of this SubscriptionSensorsUltrasonicInfo.
        :type value: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
