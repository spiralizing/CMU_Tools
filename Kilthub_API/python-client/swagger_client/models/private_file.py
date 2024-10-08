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


class PrivateFile(object):
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
        'viewer_type': 'str',
        'preview_state': 'str',
        'upload_url': 'str',
        'upload_token': 'str',
        'is_attached_to_public_version': 'bool'
    }

    attribute_map = {
        'viewer_type': 'viewer_type',
        'preview_state': 'preview_state',
        'upload_url': 'upload_url',
        'upload_token': 'upload_token',
        'is_attached_to_public_version': 'is_attached_to_public_version'
    }

    def __init__(self, viewer_type=None, preview_state=None, upload_url=None, upload_token=None, is_attached_to_public_version=None, _configuration=None):  # noqa: E501
        """PrivateFile - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._viewer_type = None
        self._preview_state = None
        self._upload_url = None
        self._upload_token = None
        self._is_attached_to_public_version = None
        self.discriminator = None

        self.viewer_type = viewer_type
        self.preview_state = preview_state
        self.upload_url = upload_url
        self.upload_token = upload_token
        self.is_attached_to_public_version = is_attached_to_public_version

    @property
    def viewer_type(self):
        """Gets the viewer_type of this PrivateFile.  # noqa: E501

        File viewer type  # noqa: E501

        :return: The viewer_type of this PrivateFile.  # noqa: E501
        :rtype: str
        """
        return self._viewer_type

    @viewer_type.setter
    def viewer_type(self, viewer_type):
        """Sets the viewer_type of this PrivateFile.

        File viewer type  # noqa: E501

        :param viewer_type: The viewer_type of this PrivateFile.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and viewer_type is None:
            raise ValueError("Invalid value for `viewer_type`, must not be `None`")  # noqa: E501

        self._viewer_type = viewer_type

    @property
    def preview_state(self):
        """Gets the preview_state of this PrivateFile.  # noqa: E501

        File preview state  # noqa: E501

        :return: The preview_state of this PrivateFile.  # noqa: E501
        :rtype: str
        """
        return self._preview_state

    @preview_state.setter
    def preview_state(self, preview_state):
        """Sets the preview_state of this PrivateFile.

        File preview state  # noqa: E501

        :param preview_state: The preview_state of this PrivateFile.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and preview_state is None:
            raise ValueError("Invalid value for `preview_state`, must not be `None`")  # noqa: E501

        self._preview_state = preview_state

    @property
    def upload_url(self):
        """Gets the upload_url of this PrivateFile.  # noqa: E501

        Upload url for file  # noqa: E501

        :return: The upload_url of this PrivateFile.  # noqa: E501
        :rtype: str
        """
        return self._upload_url

    @upload_url.setter
    def upload_url(self, upload_url):
        """Sets the upload_url of this PrivateFile.

        Upload url for file  # noqa: E501

        :param upload_url: The upload_url of this PrivateFile.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and upload_url is None:
            raise ValueError("Invalid value for `upload_url`, must not be `None`")  # noqa: E501

        self._upload_url = upload_url

    @property
    def upload_token(self):
        """Gets the upload_token of this PrivateFile.  # noqa: E501

        Token for file upload  # noqa: E501

        :return: The upload_token of this PrivateFile.  # noqa: E501
        :rtype: str
        """
        return self._upload_token

    @upload_token.setter
    def upload_token(self, upload_token):
        """Sets the upload_token of this PrivateFile.

        Token for file upload  # noqa: E501

        :param upload_token: The upload_token of this PrivateFile.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and upload_token is None:
            raise ValueError("Invalid value for `upload_token`, must not be `None`")  # noqa: E501

        self._upload_token = upload_token

    @property
    def is_attached_to_public_version(self):
        """Gets the is_attached_to_public_version of this PrivateFile.  # noqa: E501

        True if the file is attached to a public item version  # noqa: E501

        :return: The is_attached_to_public_version of this PrivateFile.  # noqa: E501
        :rtype: bool
        """
        return self._is_attached_to_public_version

    @is_attached_to_public_version.setter
    def is_attached_to_public_version(self, is_attached_to_public_version):
        """Sets the is_attached_to_public_version of this PrivateFile.

        True if the file is attached to a public item version  # noqa: E501

        :param is_attached_to_public_version: The is_attached_to_public_version of this PrivateFile.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_attached_to_public_version is None:
            raise ValueError("Invalid value for `is_attached_to_public_version`, must not be `None`")  # noqa: E501

        self._is_attached_to_public_version = is_attached_to_public_version

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
        if issubclass(PrivateFile, dict):
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
        if not isinstance(other, PrivateFile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrivateFile):
            return True

        return self.to_dict() != other.to_dict()
