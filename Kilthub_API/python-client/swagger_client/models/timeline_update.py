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


class TimelineUpdate(object):
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
        'first_online': 'str',
        'publisher_publication': 'str',
        'publisher_acceptance': 'str'
    }

    attribute_map = {
        'first_online': 'firstOnline',
        'publisher_publication': 'publisherPublication',
        'publisher_acceptance': 'publisherAcceptance'
    }

    def __init__(self, first_online=None, publisher_publication=None, publisher_acceptance=None, _configuration=None):  # noqa: E501
        """TimelineUpdate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._first_online = None
        self._publisher_publication = None
        self._publisher_acceptance = None
        self.discriminator = None

        if first_online is not None:
            self.first_online = first_online
        if publisher_publication is not None:
            self.publisher_publication = publisher_publication
        if publisher_acceptance is not None:
            self.publisher_acceptance = publisher_acceptance

    @property
    def first_online(self):
        """Gets the first_online of this TimelineUpdate.  # noqa: E501

        Online posted date  # noqa: E501

        :return: The first_online of this TimelineUpdate.  # noqa: E501
        :rtype: str
        """
        return self._first_online

    @first_online.setter
    def first_online(self, first_online):
        """Sets the first_online of this TimelineUpdate.

        Online posted date  # noqa: E501

        :param first_online: The first_online of this TimelineUpdate.  # noqa: E501
        :type: str
        """

        self._first_online = first_online

    @property
    def publisher_publication(self):
        """Gets the publisher_publication of this TimelineUpdate.  # noqa: E501

        Publish date  # noqa: E501

        :return: The publisher_publication of this TimelineUpdate.  # noqa: E501
        :rtype: str
        """
        return self._publisher_publication

    @publisher_publication.setter
    def publisher_publication(self, publisher_publication):
        """Sets the publisher_publication of this TimelineUpdate.

        Publish date  # noqa: E501

        :param publisher_publication: The publisher_publication of this TimelineUpdate.  # noqa: E501
        :type: str
        """

        self._publisher_publication = publisher_publication

    @property
    def publisher_acceptance(self):
        """Gets the publisher_acceptance of this TimelineUpdate.  # noqa: E501

        Date when the item was accepted for publication  # noqa: E501

        :return: The publisher_acceptance of this TimelineUpdate.  # noqa: E501
        :rtype: str
        """
        return self._publisher_acceptance

    @publisher_acceptance.setter
    def publisher_acceptance(self, publisher_acceptance):
        """Sets the publisher_acceptance of this TimelineUpdate.

        Date when the item was accepted for publication  # noqa: E501

        :param publisher_acceptance: The publisher_acceptance of this TimelineUpdate.  # noqa: E501
        :type: str
        """

        self._publisher_acceptance = publisher_acceptance

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
        if issubclass(TimelineUpdate, dict):
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
        if not isinstance(other, TimelineUpdate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TimelineUpdate):
            return True

        return self.to_dict() != other.to_dict()
