# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.voice_offline_slot import VoiceOfflineSlot  # noqa: F401,E501
from openadk.models.voice_offline_syntax_rule import VoiceOfflineSyntaxRule  # noqa: F401,E501
from openadk import util


class VoicePostOfflineSyntax(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, grammar=None, slot=None, start=None, startinfo=None, rule=None):  # noqa: E501
        """VoicePostOfflineSyntax - a model defined in Swagger

        :param grammar: The grammar of this VoicePostOfflineSyntax.  # noqa: E501
        :type grammar: str
        :param slot: The slot of this VoicePostOfflineSyntax.  # noqa: E501
        :type slot: List[VoiceOfflineSlot]
        :param start: The start of this VoicePostOfflineSyntax.  # noqa: E501
        :type start: str
        :param startinfo: The startinfo of this VoicePostOfflineSyntax.  # noqa: E501
        :type startinfo: str
        :param rule: The rule of this VoicePostOfflineSyntax.  # noqa: E501
        :type rule: List[VoiceOfflineSyntaxRule]
        """
        self.swagger_types = {
            'grammar': str,
            'slot': List[VoiceOfflineSlot],
            'start': str,
            'startinfo': str,
            'rule': List[VoiceOfflineSyntaxRule]
        }

        self.attribute_map = {
            'grammar': 'grammar',
            'slot': 'slot',
            'start': 'start',
            'startinfo': 'startinfo',
            'rule': 'rule'
        }

        self._grammar = grammar
        self._slot = slot
        self._start = start
        self._startinfo = startinfo
        self._rule = rule

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VoicePostOfflineSyntax of this VoicePostOfflineSyntax.  # noqa: E501
        :rtype: VoicePostOfflineSyntax
        """
        return util.deserialize_model(dikt, cls)

    @property
    def grammar(self):
        """Gets the grammar of this VoicePostOfflineSyntax.

        定义语法名称, 请输入纯字母  # noqa: E501

        :return: The grammar of this VoicePostOfflineSyntax.
        :rtype: str
        """
        return self._grammar

    @grammar.setter
    def grammar(self, grammar):
        """Sets the grammar of this VoicePostOfflineSyntax.

        定义语法名称, 请输入纯字母  # noqa: E501

        :param grammar: The grammar of this VoicePostOfflineSyntax.
        :type grammar: str
        """
        if grammar is None:
            raise ValueError("Invalid value for `grammar`, must not be `None`")  # noqa: E501

        self._grammar = grammar

    @property
    def slot(self):
        """Gets the slot of this VoicePostOfflineSyntax.

        声明槽, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :return: The slot of this VoicePostOfflineSyntax.
        :rtype: List[VoiceOfflineSlot]
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this VoicePostOfflineSyntax.

        声明槽, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :param slot: The slot of this VoicePostOfflineSyntax.
        :type slot: List[VoiceOfflineSlot]
        """
        if slot is None:
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501

        self._slot = slot

    @property
    def start(self):
        """Gets the start of this VoicePostOfflineSyntax.

        定义开始规则, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :return: The start of this VoicePostOfflineSyntax.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this VoicePostOfflineSyntax.

        定义开始规则, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :param start: The start of this VoicePostOfflineSyntax.
        :type start: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def startinfo(self):
        """Gets the startinfo of this VoicePostOfflineSyntax.

        定义开始规则详细内容  # noqa: E501

        :return: The startinfo of this VoicePostOfflineSyntax.
        :rtype: str
        """
        return self._startinfo

    @startinfo.setter
    def startinfo(self, startinfo):
        """Sets the startinfo of this VoicePostOfflineSyntax.

        定义开始规则详细内容  # noqa: E501

        :param startinfo: The startinfo of this VoicePostOfflineSyntax.
        :type startinfo: str
        """
        if startinfo is None:
            raise ValueError("Invalid value for `startinfo`, must not be `None`")  # noqa: E501

        self._startinfo = startinfo

    @property
    def rule(self):
        """Gets the rule of this VoicePostOfflineSyntax.

        所有的离线语法规则  # noqa: E501

        :return: The rule of this VoicePostOfflineSyntax.
        :rtype: List[VoiceOfflineSyntaxRule]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this VoicePostOfflineSyntax.

        所有的离线语法规则  # noqa: E501

        :param rule: The rule of this VoicePostOfflineSyntax.
        :type rule: List[VoiceOfflineSyntaxRule]
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule
