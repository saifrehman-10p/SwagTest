# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse401(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, status_code: int=None, description: str=None, error: str=None):  # noqa: E501
        """InlineResponse401 - a model defined in Swagger

        :param status_code: The status_code of this InlineResponse401.  # noqa: E501
        :type status_code: int
        :param description: The description of this InlineResponse401.  # noqa: E501
        :type description: str
        :param error: The error of this InlineResponse401.  # noqa: E501
        :type error: str
        """
        self.swagger_types = {
            'status_code': int,
            'description': str,
            'error': str
        }

        self.attribute_map = {
            'status_code': 'status_code',
            'description': 'description',
            'error': 'error'
        }
        self._status_code = status_code
        self._description = description
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse401':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_401 of this InlineResponse401.  # noqa: E501
        :rtype: InlineResponse401
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status_code(self) -> int:
        """Gets the status_code of this InlineResponse401.


        :return: The status_code of this InlineResponse401.
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: int):
        """Sets the status_code of this InlineResponse401.


        :param status_code: The status_code of this InlineResponse401.
        :type status_code: int
        """

        self._status_code = status_code

    @property
    def description(self) -> str:
        """Gets the description of this InlineResponse401.


        :return: The description of this InlineResponse401.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this InlineResponse401.


        :param description: The description of this InlineResponse401.
        :type description: str
        """

        self._description = description

    @property
    def error(self) -> str:
        """Gets the error of this InlineResponse401.


        :return: The error of this InlineResponse401.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error: str):
        """Sets the error of this InlineResponse401.


        :param error: The error of this InlineResponse401.
        :type error: str
        """

        self._error = error