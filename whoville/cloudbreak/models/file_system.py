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


class FileSystem(object):
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
        'name': 'str',
        'type': 'str',
        'default_fs': 'bool',
        'adls': 'AdlsCloudStorageParameters',
        'wasb': 'WasbCloudStorageParameters',
        'gcs': 'GcsCloudStorageParameters',
        's3': 'S3CloudStorageParameters',
        'locations': 'list[StorageLocationRequest]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'default_fs': 'defaultFs',
        'adls': 'adls',
        'wasb': 'wasb',
        'gcs': 'gcs',
        's3': 's3',
        'locations': 'locations'
    }

    def __init__(self, name=None, type=None, default_fs=False, adls=None, wasb=None, gcs=None, s3=None, locations=None):
        """
        FileSystem - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._default_fs = None
        self._adls = None
        self._wasb = None
        self._gcs = None
        self._s3 = None
        self._locations = None

        self.name = name
        self.type = type
        if default_fs is not None:
          self.default_fs = default_fs
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
    def name(self):
        """
        Gets the name of this FileSystem.
        name of the filesystem

        :return: The name of this FileSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FileSystem.
        name of the filesystem

        :param name: The name of this FileSystem.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this FileSystem.
        type of the filesystem

        :return: The type of this FileSystem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this FileSystem.
        type of the filesystem

        :param type: The type of this FileSystem.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def default_fs(self):
        """
        Gets the default_fs of this FileSystem.
        true if fs.defaultFS should point to this filesystem

        :return: The default_fs of this FileSystem.
        :rtype: bool
        """
        return self._default_fs

    @default_fs.setter
    def default_fs(self, default_fs):
        """
        Sets the default_fs of this FileSystem.
        true if fs.defaultFS should point to this filesystem

        :param default_fs: The default_fs of this FileSystem.
        :type: bool
        """

        self._default_fs = default_fs

    @property
    def adls(self):
        """
        Gets the adls of this FileSystem.

        :return: The adls of this FileSystem.
        :rtype: AdlsCloudStorageParameters
        """
        return self._adls

    @adls.setter
    def adls(self, adls):
        """
        Sets the adls of this FileSystem.

        :param adls: The adls of this FileSystem.
        :type: AdlsCloudStorageParameters
        """

        self._adls = adls

    @property
    def wasb(self):
        """
        Gets the wasb of this FileSystem.

        :return: The wasb of this FileSystem.
        :rtype: WasbCloudStorageParameters
        """
        return self._wasb

    @wasb.setter
    def wasb(self, wasb):
        """
        Sets the wasb of this FileSystem.

        :param wasb: The wasb of this FileSystem.
        :type: WasbCloudStorageParameters
        """

        self._wasb = wasb

    @property
    def gcs(self):
        """
        Gets the gcs of this FileSystem.

        :return: The gcs of this FileSystem.
        :rtype: GcsCloudStorageParameters
        """
        return self._gcs

    @gcs.setter
    def gcs(self, gcs):
        """
        Sets the gcs of this FileSystem.

        :param gcs: The gcs of this FileSystem.
        :type: GcsCloudStorageParameters
        """

        self._gcs = gcs

    @property
    def s3(self):
        """
        Gets the s3 of this FileSystem.

        :return: The s3 of this FileSystem.
        :rtype: S3CloudStorageParameters
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """
        Sets the s3 of this FileSystem.

        :param s3: The s3 of this FileSystem.
        :type: S3CloudStorageParameters
        """

        self._s3 = s3

    @property
    def locations(self):
        """
        Gets the locations of this FileSystem.
        configuration of the filesystem location

        :return: The locations of this FileSystem.
        :rtype: list[StorageLocationRequest]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """
        Sets the locations of this FileSystem.
        configuration of the filesystem location

        :param locations: The locations of this FileSystem.
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
        if not isinstance(other, FileSystem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
