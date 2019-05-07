# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk import util


class SubscriptionName(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name=None):  # noqa: E501
        """SubscriptionName - a model defined in Swagger

        :param name: The name of this SubscriptionName.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionName of this SubscriptionName.  # noqa: E501
        :rtype: SubscriptionName
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this SubscriptionName.


        :return: The name of this SubscriptionName.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionName.


        :param name: The name of this SubscriptionName.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name
