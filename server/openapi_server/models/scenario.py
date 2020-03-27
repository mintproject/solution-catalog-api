# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Scenario(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, text=None, region=None, subregion=None, time_period=None):  # noqa: E501
        """Scenario - a model defined in OpenAPI

        :param id: The id of this Scenario.  # noqa: E501
        :type id: str
        :param text: The text of this Scenario.  # noqa: E501
        :type text: str
        :param region: The region of this Scenario.  # noqa: E501
        :type region: str
        :param subregion: The subregion of this Scenario.  # noqa: E501
        :type subregion: str
        :param time_period: The time_period of this Scenario.  # noqa: E501
        :type time_period: object
        """
        self.openapi_types = {
            'id': str,
            'text': str,
            'region': str,
            'subregion': str,
            'time_period': object
        }

        self.attribute_map = {
            'id': 'id',
            'text': 'text',
            'region': 'region',
            'subregion': 'subregion',
            'time_period': 'time_period'
        }

        self._id = id
        self._text = text
        self._region = region
        self._subregion = subregion
        self._time_period = time_period

    @classmethod
    def from_dict(cls, dikt) -> 'Scenario':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The scenario of this Scenario.  # noqa: E501
        :rtype: Scenario
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Scenario.


        :return: The id of this Scenario.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scenario.


        :param id: The id of this Scenario.
        :type id: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this Scenario.


        :return: The text of this Scenario.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Scenario.


        :param text: The text of this Scenario.
        :type text: str
        """

        self._text = text

    @property
    def region(self):
        """Gets the region of this Scenario.


        :return: The region of this Scenario.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Scenario.


        :param region: The region of this Scenario.
        :type region: str
        """

        self._region = region

    @property
    def subregion(self):
        """Gets the subregion of this Scenario.


        :return: The subregion of this Scenario.
        :rtype: str
        """
        return self._subregion

    @subregion.setter
    def subregion(self, subregion):
        """Sets the subregion of this Scenario.


        :param subregion: The subregion of this Scenario.
        :type subregion: str
        """

        self._subregion = subregion

    @property
    def time_period(self):
        """Gets the time_period of this Scenario.


        :return: The time_period of this Scenario.
        :rtype: object
        """
        return self._time_period

    @time_period.setter
    def time_period(self, time_period):
        """Sets the time_period of this Scenario.


        :param time_period: The time_period of this Scenario.
        :type time_period: object
        """

        self._time_period = time_period
