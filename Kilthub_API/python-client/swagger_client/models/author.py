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


class Author(object):
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
        'id': 'int',
        'full_name': 'str',
        'is_active': 'bool',
        'url_name': 'str',
        'orcid_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'full_name': 'full_name',
        'is_active': 'is_active',
        'url_name': 'url_name',
        'orcid_id': 'orcid_id'
    }

    def __init__(self, id=None, full_name=None, is_active=None, url_name=None, orcid_id=None, _configuration=None):  # noqa: E501
        """Author - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._full_name = None
        self._is_active = None
        self._url_name = None
        self._orcid_id = None
        self.discriminator = None

        self.id = id
        self.full_name = full_name
        self.is_active = is_active
        self.url_name = url_name
        self.orcid_id = orcid_id

    @property
    def id(self):
        """Gets the id of this Author.  # noqa: E501

        Author id  # noqa: E501

        :return: The id of this Author.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Author.

        Author id  # noqa: E501

        :param id: The id of this Author.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def full_name(self):
        """Gets the full_name of this Author.  # noqa: E501

        Author full name  # noqa: E501

        :return: The full_name of this Author.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Author.

        Author full name  # noqa: E501

        :param full_name: The full_name of this Author.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def is_active(self):
        """Gets the is_active of this Author.  # noqa: E501

        True if author has published items  # noqa: E501

        :return: The is_active of this Author.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Author.

        True if author has published items  # noqa: E501

        :param is_active: The is_active of this Author.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def url_name(self):
        """Gets the url_name of this Author.  # noqa: E501

        Author url name  # noqa: E501

        :return: The url_name of this Author.  # noqa: E501
        :rtype: str
        """
        return self._url_name

    @url_name.setter
    def url_name(self, url_name):
        """Sets the url_name of this Author.

        Author url name  # noqa: E501

        :param url_name: The url_name of this Author.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and url_name is None:
            raise ValueError("Invalid value for `url_name`, must not be `None`")  # noqa: E501

        self._url_name = url_name

    @property
    def orcid_id(self):
        """Gets the orcid_id of this Author.  # noqa: E501

        Author Orcid  # noqa: E501

        :return: The orcid_id of this Author.  # noqa: E501
        :rtype: str
        """
        return self._orcid_id

    @orcid_id.setter
    def orcid_id(self, orcid_id):
        """Sets the orcid_id of this Author.

        Author Orcid  # noqa: E501

        :param orcid_id: The orcid_id of this Author.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and orcid_id is None:
            raise ValueError("Invalid value for `orcid_id`, must not be `None`")  # noqa: E501

        self._orcid_id = orcid_id

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
        if issubclass(Author, dict):
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
        if not isinstance(other, Author):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Author):
            return True

        return self.to_dict() != other.to_dict()
