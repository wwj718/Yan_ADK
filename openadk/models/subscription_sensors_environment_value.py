# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_sensors_environment_info import SubscriptionSensorsEnvironmentInfo  # noqa: F401,E501
from openadk import util


class SubscriptionSensorsEnvironmentValue(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, environment=None):  # noqa: E501
        """SubscriptionSensorsEnvironmentValue - a model defined in Swagger

        :param environment: The environment of this SubscriptionSensorsEnvironmentValue.  # noqa: E501
        :type environment: List[SubscriptionSensorsEnvironmentInfo]
        """
        self.swagger_types = {
            'environment': List[SubscriptionSensorsEnvironmentInfo]
        }

        self.attribute_map = {
            'environment': 'environment'
        }

        self._environment = environment

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionSensorsEnvironmentValue of this SubscriptionSensorsEnvironmentValue.  # noqa: E501
        :rtype: SubscriptionSensorsEnvironmentValue
        """
        return util.deserialize_model(dikt, cls)

    @property
    def environment(self):
        """Gets the environment of this SubscriptionSensorsEnvironmentValue.


        :return: The environment of this SubscriptionSensorsEnvironmentValue.
        :rtype: List[SubscriptionSensorsEnvironmentInfo]
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this SubscriptionSensorsEnvironmentValue.


        :param environment: The environment of this SubscriptionSensorsEnvironmentValue.
        :type environment: List[SubscriptionSensorsEnvironmentInfo]
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment
