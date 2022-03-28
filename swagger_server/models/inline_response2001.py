# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, price: float=None, name: str=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param price: The price of this InlineResponse2001.  # noqa: E501
        :type price: float
        :param name: The name of this InlineResponse2001.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'price': float,
            'name': str
        }

        self.attribute_map = {
            'price': 'price',
            'name': 'name'
        }
        self._price = price
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def price(self) -> float:
        """Gets the price of this InlineResponse2001.


        :return: The price of this InlineResponse2001.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price: float):
        """Sets the price of this InlineResponse2001.


        :param price: The price of this InlineResponse2001.
        :type price: float
        """

        self._price = price

    @property
    def name(self) -> str:
        """Gets the name of this InlineResponse2001.


        :return: The name of this InlineResponse2001.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InlineResponse2001.


        :param name: The name of this InlineResponse2001.
        :type name: str
        """

        self._name = name