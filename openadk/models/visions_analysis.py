# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VisionsAnalysis(object):
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
        'age': 'int',
        'group': 'str',
        'gender': 'str',
        'expression': 'str'
    }

    attribute_map = {
        'age': 'age',
        'group': 'group',
        'gender': 'gender',
        'expression': 'expression'
    }

    def __init__(self, age=None, group=None, gender=None, expression=None):  # noqa: E501
        """VisionsAnalysis - a model defined in Swagger"""  # noqa: E501

        self._age = None
        self._group = None
        self._gender = None
        self._expression = None
        self.discriminator = None

        if age is not None:
            self.age = age
        if group is not None:
            self.group = group
        if gender is not None:
            self.gender = gender
        if expression is not None:
            self.expression = expression

    @property
    def age(self):
        """Gets the age of this VisionsAnalysis.  # noqa: E501

        Age  # noqa: E501

        :return: The age of this VisionsAnalysis.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this VisionsAnalysis.

        Age  # noqa: E501

        :param age: The age of this VisionsAnalysis.  # noqa: E501
        :type: int
        """
        if age is not None and age < 0:  # noqa: E501
            raise ValueError("Invalid value for `age`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age = age

    @property
    def group(self):
        """Gets the group of this VisionsAnalysis.  # noqa: E501

         Age group, all possible values: - baby - children - juvenile - youth - middle_age - old_age - none   # noqa: E501

        :return: The group of this VisionsAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this VisionsAnalysis.

         Age group, all possible values: - baby - children - juvenile - youth - middle_age - old_age - none   # noqa: E501

        :param group: The group of this VisionsAnalysis.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def gender(self):
        """Gets the gender of this VisionsAnalysis.  # noqa: E501

         Gender, all possible values: - male - female - none \"none\" means there is no result.   # noqa: E501

        :return: The gender of this VisionsAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this VisionsAnalysis.

         Gender, all possible values: - male - female - none \"none\" means there is no result.   # noqa: E501

        :param gender: The gender of this VisionsAnalysis.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female", "none"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def expression(self):
        """Gets the expression of this VisionsAnalysis.  # noqa: E501

         Expression, all possible values: - anger - disgust - fear - happy - sad - surprised - normal - none   # noqa: E501

        :return: The expression of this VisionsAnalysis.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this VisionsAnalysis.

         Expression, all possible values: - anger - disgust - fear - happy - sad - surprised - normal - none   # noqa: E501

        :param expression: The expression of this VisionsAnalysis.  # noqa: E501
        :type: str
        """

        self._expression = expression

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
        if issubclass(VisionsAnalysis, dict):
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
        if not isinstance(other, VisionsAnalysis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
