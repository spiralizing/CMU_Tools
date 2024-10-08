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


class ArticleSearch(object):
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
        'resource_doi': 'str',
        'item_type': 'int',
        'doi': 'str',
        'handle': 'str',
        'project_id': 'int',
        'order': 'str'
    }

    attribute_map = {
        'resource_doi': 'resource_doi',
        'item_type': 'item_type',
        'doi': 'doi',
        'handle': 'handle',
        'project_id': 'project_id',
        'order': 'order'
    }

    def __init__(self, resource_doi=None, item_type=None, doi=None, handle=None, project_id=None, order='created_date', _configuration=None):  # noqa: E501
        """ArticleSearch - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resource_doi = None
        self._item_type = None
        self._doi = None
        self._handle = None
        self._project_id = None
        self._order = None
        self.discriminator = None

        if resource_doi is not None:
            self.resource_doi = resource_doi
        if item_type is not None:
            self.item_type = item_type
        if doi is not None:
            self.doi = doi
        if handle is not None:
            self.handle = handle
        if project_id is not None:
            self.project_id = project_id
        if order is not None:
            self.order = order

    @property
    def resource_doi(self):
        """Gets the resource_doi of this ArticleSearch.  # noqa: E501

        Only return articles with this resource_doi  # noqa: E501

        :return: The resource_doi of this ArticleSearch.  # noqa: E501
        :rtype: str
        """
        return self._resource_doi

    @resource_doi.setter
    def resource_doi(self, resource_doi):
        """Sets the resource_doi of this ArticleSearch.

        Only return articles with this resource_doi  # noqa: E501

        :param resource_doi: The resource_doi of this ArticleSearch.  # noqa: E501
        :type: str
        """

        self._resource_doi = resource_doi

    @property
    def item_type(self):
        """Gets the item_type of this ArticleSearch.  # noqa: E501

        Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model  # noqa: E501

        :return: The item_type of this ArticleSearch.  # noqa: E501
        :rtype: int
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this ArticleSearch.

        Only return articles with the respective type. Mapping for item_type is: 1 - Figure, 2 - Media, 3 - Dataset, 5 - Poster, 6 - Journal contribution, 7 - Presentation, 8 - Thesis, 9 - Software, 11 - Online resource, 12 - Preprint, 13 - Book, 14 - Conference contribution, 15 - Chapter, 16 - Peer review, 17 - Educational resource, 18 - Report, 19 - Standard, 20 - Composition, 21 - Funding, 22 - Physical object, 23 - Data management plan, 24 - Workflow, 25 - Monograph, 26 - Performance, 27 - Event, 28 - Service, 29 - Model  # noqa: E501

        :param item_type: The item_type of this ArticleSearch.  # noqa: E501
        :type: int
        """

        self._item_type = item_type

    @property
    def doi(self):
        """Gets the doi of this ArticleSearch.  # noqa: E501

        Only return articles with this doi  # noqa: E501

        :return: The doi of this ArticleSearch.  # noqa: E501
        :rtype: str
        """
        return self._doi

    @doi.setter
    def doi(self, doi):
        """Sets the doi of this ArticleSearch.

        Only return articles with this doi  # noqa: E501

        :param doi: The doi of this ArticleSearch.  # noqa: E501
        :type: str
        """

        self._doi = doi

    @property
    def handle(self):
        """Gets the handle of this ArticleSearch.  # noqa: E501

        Only return articles with this handle  # noqa: E501

        :return: The handle of this ArticleSearch.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this ArticleSearch.

        Only return articles with this handle  # noqa: E501

        :param handle: The handle of this ArticleSearch.  # noqa: E501
        :type: str
        """

        self._handle = handle

    @property
    def project_id(self):
        """Gets the project_id of this ArticleSearch.  # noqa: E501

        Only return articles in this project  # noqa: E501

        :return: The project_id of this ArticleSearch.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ArticleSearch.

        Only return articles in this project  # noqa: E501

        :param project_id: The project_id of this ArticleSearch.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def order(self):
        """Gets the order of this ArticleSearch.  # noqa: E501

        The field by which to order  # noqa: E501

        :return: The order of this ArticleSearch.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ArticleSearch.

        The field by which to order  # noqa: E501

        :param order: The order of this ArticleSearch.  # noqa: E501
        :type: str
        """
        allowed_values = ["created_date", "published_date", "modified_date", "views", "shares", "downloads", "cites"]  # noqa: E501
        if (self._configuration.client_side_validation and
                order not in allowed_values):
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"  # noqa: E501
                .format(order, allowed_values)
            )

        self._order = order

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
        if issubclass(ArticleSearch, dict):
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
        if not isinstance(other, ArticleSearch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArticleSearch):
            return True

        return self.to_dict() != other.to_dict()
