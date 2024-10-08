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


class AuthorComplete(object):
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
        'institution_id': 'int',
        'group_id': 'int',
        'first_name': 'str',
        'last_name': 'str',
        'is_public': 'int',
        'job_title': 'str'
    }

    attribute_map = {
        'institution_id': 'institution_id',
        'group_id': 'group_id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'is_public': 'is_public',
        'job_title': 'job_title'
    }

    def __init__(self, institution_id=None, group_id=None, first_name=None, last_name=None, is_public=None, job_title=None, _configuration=None):  # noqa: E501
        """AuthorComplete - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._institution_id = None
        self._group_id = None
        self._first_name = None
        self._last_name = None
        self._is_public = None
        self._job_title = None
        self.discriminator = None

        self.institution_id = institution_id
        self.group_id = group_id
        self.first_name = first_name
        self.last_name = last_name
        self.is_public = is_public
        self.job_title = job_title

    @property
    def institution_id(self):
        """Gets the institution_id of this AuthorComplete.  # noqa: E501

        Institution id  # noqa: E501

        :return: The institution_id of this AuthorComplete.  # noqa: E501
        :rtype: int
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this AuthorComplete.

        Institution id  # noqa: E501

        :param institution_id: The institution_id of this AuthorComplete.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and institution_id is None:
            raise ValueError("Invalid value for `institution_id`, must not be `None`")  # noqa: E501

        self._institution_id = institution_id

    @property
    def group_id(self):
        """Gets the group_id of this AuthorComplete.  # noqa: E501

        Group id  # noqa: E501

        :return: The group_id of this AuthorComplete.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this AuthorComplete.

        Group id  # noqa: E501

        :param group_id: The group_id of this AuthorComplete.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and group_id is None:
            raise ValueError("Invalid value for `group_id`, must not be `None`")  # noqa: E501

        self._group_id = group_id

    @property
    def first_name(self):
        """Gets the first_name of this AuthorComplete.  # noqa: E501

        First Name  # noqa: E501

        :return: The first_name of this AuthorComplete.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AuthorComplete.

        First Name  # noqa: E501

        :param first_name: The first_name of this AuthorComplete.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this AuthorComplete.  # noqa: E501

        Last Name  # noqa: E501

        :return: The last_name of this AuthorComplete.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AuthorComplete.

        Last Name  # noqa: E501

        :param last_name: The last_name of this AuthorComplete.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def is_public(self):
        """Gets the is_public of this AuthorComplete.  # noqa: E501

        if 1 then the author has published items  # noqa: E501

        :return: The is_public of this AuthorComplete.  # noqa: E501
        :rtype: int
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this AuthorComplete.

        if 1 then the author has published items  # noqa: E501

        :param is_public: The is_public of this AuthorComplete.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and is_public is None:
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def job_title(self):
        """Gets the job_title of this AuthorComplete.  # noqa: E501

        Job title  # noqa: E501

        :return: The job_title of this AuthorComplete.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this AuthorComplete.

        Job title  # noqa: E501

        :param job_title: The job_title of this AuthorComplete.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and job_title is None:
            raise ValueError("Invalid value for `job_title`, must not be `None`")  # noqa: E501

        self._job_title = job_title

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
        if issubclass(AuthorComplete, dict):
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
        if not isinstance(other, AuthorComplete):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthorComplete):
            return True

        return self.to_dict() != other.to_dict()
