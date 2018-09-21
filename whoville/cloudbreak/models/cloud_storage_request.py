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


class CloudStorageRequest(object):
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
        'adls': 'AdlsCloudStorageParameters',
        'wasb': 'WasbCloudStorageParameters',
        'gcs': 'GcsCloudStorageParameters',
        's3': 'S3CloudStorageParameters',
        'locations': 'list[StorageLocationRequest]'
    }

    attribute_map = {
        'adls': 'adls',
        'wasb': 'wasb',
        'gcs': 'gcs',
        's3': 's3',
        'locations': 'locations'
    }

    def __init__(self, adls=None, wasb=None, gcs=None, s3=None, locations=None):
        """
        CloudStorageRequest - a model defined in Swagger
        """

        self._adls = None
        self._wasb = None
        self._gcs = None
        self._s3 = None
        self._locations = None

        if adls is not None:
          self.adls = adls
        if wasb is not None:
          self.wasb = wasb
        if gcs is not None:
          self.gcs = gcs
        if s3 is not None:
          self.s3 = s3
        if locations is not None:
          self.locations = locations

    @property
    def adls(self):
        """
        Gets the adls of this CloudStorageRequest.

        :return: The adls of this CloudStorageRequest.
        :rtype: AdlsCloudStorageParameters
        """
        return self._adls

    @adls.setter
    def adls(self, adls):
        """
        Sets the adls of this CloudStorageRequest.

        :param adls: The adls of this CloudStorageRequest.
        :type: AdlsCloudStorageParameters
        """

        self._adls = adls

    @property
    def wasb(self):
        """
        Gets the wasb of this CloudStorageRequest.

        :return: The wasb of this CloudStorageRequest.
        :rtype: WasbCloudStorageParameters
        """
        return self._wasb

    @wasb.setter
    def wasb(self, wasb):
        """
        Sets the wasb of this CloudStorageRequest.

        :param wasb: The wasb of this CloudStorageRequest.
        :type: WasbCloudStorageParameters
        """

        self._wasb = wasb

    @property
    def gcs(self):
        """
        Gets the gcs of this CloudStorageRequest.

        :return: The gcs of this CloudStorageRequest.
        :rtype: GcsCloudStorageParameters
        """
        return self._gcs

    @gcs.setter
    def gcs(self, gcs):
        """
        Sets the gcs of this CloudStorageRequest.

        :param gcs: The gcs of this CloudStorageRequest.
        :type: GcsCloudStorageParameters
        """

        self._gcs = gcs

    @property
    def s3(self):
        """
        Gets the s3 of this CloudStorageRequest.

        :return: The s3 of this CloudStorageRequest.
        :rtype: S3CloudStorageParameters
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """
        Sets the s3 of this CloudStorageRequest.

        :param s3: The s3 of this CloudStorageRequest.
        :type: S3CloudStorageParameters
        """

        self._s3 = s3

    @property
    def locations(self):
        """
        Gets the locations of this CloudStorageRequest.
        cloud storage locations

        :return: The locations of this CloudStorageRequest.
        :rtype: list[StorageLocationRequest]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this CloudStorageRequest.
        cloud storage locations

        :param locations: The locations of this CloudStorageRequest.
        :type: list[StorageLocationRequest]
        """

        self._locations = locations

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
        if not isinstance(other, CloudStorageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
