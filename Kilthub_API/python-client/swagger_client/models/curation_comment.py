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


class CurationComment(object):
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
        'account_id': 'int',
        'type': 'str',
        'text': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'type': 'type',
        'text': 'text'
    }

    def __init__(self, id=None, account_id=None, type=None, text=None, _configuration=None):  # noqa: E501
        """CurationComment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._account_id = None
        self._type = None
        self._text = None
        self.discriminator = None

        self.id = id
        self.account_id = account_id
        self.type = type
        self.text = text

    @property
    def id(self):
        """Gets the id of this CurationComment.  # noqa: E501

        The ID of the comment.  # noqa: E501

        :return: The id of this CurationComment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurationComment.

        The ID of the comment.  # noqa: E501

        :param id: The id of this CurationComment.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this CurationComment.  # noqa: E501

        The ID of the account which generated this comment.  # noqa: E501

        :return: The account_id of this CurationComment.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CurationComment.

        The ID of the account which generated this comment.  # noqa: E501

        :param account_id: The account_id of this CurationComment.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def type(self):
        """Gets the type of this CurationComment.  # noqa: E501

        The ID of the account which generated this comment.  # noqa: E501

        :return: The type of this CurationComment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CurationComment.

        The ID of the account which generated this comment.  # noqa: E501

        :param type: The type of this CurationComment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["comment", "approved", "rejected", "closed"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def text(self):
        """Gets the text of this CurationComment.  # noqa: E501

        The value/content of the comment.  # noqa: E501

        :return: The text of this CurationComment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CurationComment.

        The value/content of the comment.  # noqa: E501

        :param text: The text of this CurationComment.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

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
        if issubclass(CurationComment, dict):
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
        if not isinstance(other, CurationComment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CurationComment):
            return True

        return self.to_dict() != other.to_dict()
