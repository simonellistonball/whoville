# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RecommendationRequestJson(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'credential_id': 'int',
        'credential_name': 'str',
        'region': 'str',
        'platform_variant': 'str',
        'filters': 'dict(str, str)',
        'availability_zone': 'str',
        'blueprint_name': 'str',
        'blueprint_id': 'int'
    }

    attribute_map = {
        'credential_id': 'credentialId',
        'credential_name': 'credentialName',
        'region': 'region',
        'platform_variant': 'platformVariant',
        'filters': 'filters',
        'availability_zone': 'availabilityZone',
        'blueprint_name': 'blueprintName',
        'blueprint_id': 'blueprintId'
    }

    def __init__(self, credential_id=None, credential_name=None, region=None, platform_variant=None, filters=None, availability_zone=None, blueprint_name=None, blueprint_id=None):
        """
        RecommendationRequestJson - a model defined in Swagger
        """

        self._credential_id = None
        self._credential_name = None
        self._region = None
        self._platform_variant = None
        self._filters = None
        self._availability_zone = None
        self._blueprint_name = None
        self._blueprint_id = None

        if credential_id is not None:
          self.credential_id = credential_id
        if credential_name is not None:
          self.credential_name = credential_name
        if region is not None:
          self.region = region
        if platform_variant is not None:
          self.platform_variant = platform_variant
        if filters is not None:
          self.filters = filters
        if availability_zone is not None:
          self.availability_zone = availability_zone
        if blueprint_name is not None:
          self.blueprint_name = blueprint_name
        if blueprint_id is not None:
          self.blueprint_id = blueprint_id

    @property
    def credential_id(self):
        """
        Gets the credential_id of this RecommendationRequestJson.
        credential resource id for the request

        :return: The credential_id of this RecommendationRequestJson.
        :rtype: int
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        """
        Sets the credential_id of this RecommendationRequestJson.
        credential resource id for the request

        :param credential_id: The credential_id of this RecommendationRequestJson.
        :type: int
        """

        self._credential_id = credential_id

    @property
    def credential_name(self):
        """
        Gets the credential_name of this RecommendationRequestJson.
        credential resource name for the request

        :return: The credential_name of this RecommendationRequestJson.
        :rtype: str
        """
        return self._credential_name

    @credential_name.setter
    def credential_name(self, credential_name):
        """
        Sets the credential_name of this RecommendationRequestJson.
        credential resource name for the request

        :param credential_name: The credential_name of this RecommendationRequestJson.
        :type: str
        """

        self._credential_name = credential_name

    @property
    def region(self):
        """
        Gets the region of this RecommendationRequestJson.
        Related region

        :return: The region of this RecommendationRequestJson.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this RecommendationRequestJson.
        Related region

        :param region: The region of this RecommendationRequestJson.
        :type: str
        """

        self._region = region

    @property
    def platform_variant(self):
        """
        Gets the platform_variant of this RecommendationRequestJson.
        cloud provider api variant

        :return: The platform_variant of this RecommendationRequestJson.
        :rtype: str
        """
        return self._platform_variant

    @platform_variant.setter
    def platform_variant(self, platform_variant):
        """
        Sets the platform_variant of this RecommendationRequestJson.
        cloud provider api variant

        :param platform_variant: The platform_variant of this RecommendationRequestJson.
        :type: str
        """

        self._platform_variant = platform_variant

    @property
    def filters(self):
        """
        Gets the filters of this RecommendationRequestJson.
        filter for resources

        :return: The filters of this RecommendationRequestJson.
        :rtype: dict(str, str)
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this RecommendationRequestJson.
        filter for resources

        :param filters: The filters of this RecommendationRequestJson.
        :type: dict(str, str)
        """

        self._filters = filters

    @property
    def availability_zone(self):
        """
        Gets the availability_zone of this RecommendationRequestJson.
        related availability zone

        :return: The availability_zone of this RecommendationRequestJson.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """
        Sets the availability_zone of this RecommendationRequestJson.
        related availability zone

        :param availability_zone: The availability_zone of this RecommendationRequestJson.
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def blueprint_name(self):
        """
        Gets the blueprint_name of this RecommendationRequestJson.
        name that could indentify an existing blueprint

        :return: The blueprint_name of this RecommendationRequestJson.
        :rtype: str
        """
        return self._blueprint_name

    @blueprint_name.setter
    def blueprint_name(self, blueprint_name):
        """
        Sets the blueprint_name of this RecommendationRequestJson.
        name that could indentify an existing blueprint

        :param blueprint_name: The blueprint_name of this RecommendationRequestJson.
        :type: str
        """

        self._blueprint_name = blueprint_name

    @property
    def blueprint_id(self):
        """
        Gets the blueprint_id of this RecommendationRequestJson.
        id that could indentify an existing blueprint

        :return: The blueprint_id of this RecommendationRequestJson.
        :rtype: int
        """
        return self._blueprint_id

    @blueprint_id.setter
    def blueprint_id(self, blueprint_id):
        """
        Sets the blueprint_id of this RecommendationRequestJson.
        id that could indentify an existing blueprint

        :param blueprint_id: The blueprint_id of this RecommendationRequestJson.
        :type: int
        """

        self._blueprint_id = blueprint_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, RecommendationRequestJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
