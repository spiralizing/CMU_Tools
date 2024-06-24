# coding: utf-8

"""
    Figshare API

    Figshare apiv2. Using Swagger 2.0  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class LocationWarningsUpdate(object):
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
        'location': 'str',
        'warnings': 'list[str]'
    }

    attribute_map = {
        'location': 'location',
        'warnings': 'warnings'
    }

    def __init__(self, location=None, warnings=None, _configuration=None):  # noqa: E501
        """LocationWarningsUpdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._location = None
        self._warnings = None
        self.discriminator = None

        self.location = location
        self.warnings = warnings

    @property
    def location(self):
        """Gets the location of this LocationWarningsUpdate.  # noqa: E501

        Url for entity  # noqa: E501

        :return: The location of this LocationWarningsUpdate.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this LocationWarningsUpdate.

        Url for entity  # noqa: E501

        :param location: The location of this LocationWarningsUpdate.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def warnings(self):
        """Gets the warnings of this LocationWarningsUpdate.  # noqa: E501

        Issues encountered during the operation  # noqa: E501

        :return: The warnings of this LocationWarningsUpdate.  # noqa: E501
        :rtype: list[str]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this LocationWarningsUpdate.

        Issues encountered during the operation  # noqa: E501

        :param warnings: The warnings of this LocationWarningsUpdate.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and warnings is None:
            raise ValueError("Invalid value for `warnings`, must not be `None`")  # noqa: E501

        self._warnings = warnings

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
        if issubclass(LocationWarningsUpdate, dict):
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
        if not isinstance(other, LocationWarningsUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocationWarningsUpdate):
            return True

        return self.to_dict() != other.to_dict()
