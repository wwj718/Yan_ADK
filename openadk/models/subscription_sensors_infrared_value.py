# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_sensors_infrared_info import SubscriptionSensorsInfraredInfo  # noqa: F401,E501
from openadk import util


class SubscriptionSensorsInfraredValue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, infrared=None):  # noqa: E501
        """SubscriptionSensorsInfraredValue - a model defined in Swagger

        :param infrared: The infrared of this SubscriptionSensorsInfraredValue.  # noqa: E501
        :type infrared: List[SubscriptionSensorsInfraredInfo]
        """
        self.swagger_types = {
            'infrared': List[SubscriptionSensorsInfraredInfo]
        }

        self.attribute_map = {
            'infrared': 'infrared'
        }

        self._infrared = infrared

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionSensorsInfraredValue of this SubscriptionSensorsInfraredValue.  # noqa: E501
        :rtype: SubscriptionSensorsInfraredValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def infrared(self):
        """Gets the infrared of this SubscriptionSensorsInfraredValue.


        :return: The infrared of this SubscriptionSensorsInfraredValue.
        :rtype: List[SubscriptionSensorsInfraredInfo]
        """
        return self._infrared

    @infrared.setter
    def infrared(self, infrared):
        """Sets the infrared of this SubscriptionSensorsInfraredValue.


        :param infrared: The infrared of this SubscriptionSensorsInfraredValue.
        :type infrared: List[SubscriptionSensorsInfraredInfo]
        """
        if infrared is None:
            raise ValueError("Invalid value for `infrared`, must not be `None`")  # noqa: E501

        self._infrared = infrared
