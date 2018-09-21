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


class VolumeParameterConfigJson(object):
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
        'volume_parameter_type': 'str',
        'minimum_size': 'int',
        'maximum_size': 'int',
        'minimum_number': 'int',
        'maximum_number': 'int'
    }

    attribute_map = {
        'volume_parameter_type': 'volumeParameterType',
        'minimum_size': 'minimumSize',
        'maximum_size': 'maximumSize',
        'minimum_number': 'minimumNumber',
        'maximum_number': 'maximumNumber'
    }

    def __init__(self, volume_parameter_type=None, minimum_size=None, maximum_size=None, minimum_number=None, maximum_number=None):
        """
        VolumeParameterConfigJson - a model defined in Swagger
        """

        self._volume_parameter_type = None
        self._minimum_size = None
        self._maximum_size = None
        self._minimum_number = None
        self._maximum_number = None

        if volume_parameter_type is not None:
          self.volume_parameter_type = volume_parameter_type
        if minimum_size is not None:
          self.minimum_size = minimum_size
        if maximum_size is not None:
          self.maximum_size = maximum_size
        if minimum_number is not None:
          self.minimum_number = minimum_number
        if maximum_number is not None:
          self.maximum_number = maximum_number

    @property
    def volume_parameter_type(self):
        """
        Gets the volume_parameter_type of this VolumeParameterConfigJson.

        :return: The volume_parameter_type of this VolumeParameterConfigJson.
        :rtype: str
        """
        return self._volume_parameter_type

    @volume_parameter_type.setter
    def volume_parameter_type(self, volume_parameter_type):
        """
        Sets the volume_parameter_type of this VolumeParameterConfigJson.

        :param volume_parameter_type: The volume_parameter_type of this VolumeParameterConfigJson.
        :type: str
        """

        self._volume_parameter_type = volume_parameter_type

    @property
    def minimum_size(self):
        """
        Gets the minimum_size of this VolumeParameterConfigJson.

        :return: The minimum_size of this VolumeParameterConfigJson.
        :rtype: int
        """
        return self._minimum_size

    @minimum_size.setter
    def minimum_size(self, minimum_size):
        """
        Sets the minimum_size of this VolumeParameterConfigJson.

        :param minimum_size: The minimum_size of this VolumeParameterConfigJson.
        :type: int
        """

        self._minimum_size = minimum_size

    @property
    def maximum_size(self):
        """
        Gets the maximum_size of this VolumeParameterConfigJson.

        :return: The maximum_size of this VolumeParameterConfigJson.
        :rtype: int
        """
        return self._maximum_size

    @maximum_size.setter
    def maximum_size(self, maximum_size):
        """
        Sets the maximum_size of this VolumeParameterConfigJson.

        :param maximum_size: The maximum_size of this VolumeParameterConfigJson.
        :type: int
        """

        self._maximum_size = maximum_size

    @property
    def minimum_number(self):
        """
        Gets the minimum_number of this VolumeParameterConfigJson.

        :return: The minimum_number of this VolumeParameterConfigJson.
        :rtype: int
        """
        return self._minimum_number

    @minimum_number.setter
    def minimum_number(self, minimum_number):
        """
        Sets the minimum_number of this VolumeParameterConfigJson.

        :param minimum_number: The minimum_number of this VolumeParameterConfigJson.
        :type: int
        """

        self._minimum_number = minimum_number

    @property
    def maximum_number(self):
        """
        Gets the maximum_number of this VolumeParameterConfigJson.

        :return: The maximum_number of this VolumeParameterConfigJson.
        :rtype: int
        """
        return self._maximum_number

    @maximum_number.setter
    def maximum_number(self, maximum_number):
        """
        Sets the maximum_number of this VolumeParameterConfigJson.

        :param maximum_number: The maximum_number of this VolumeParameterConfigJson.
        :type: int
        """

        self._maximum_number = maximum_number

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
        if not isinstance(other, VolumeParameterConfigJson):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
