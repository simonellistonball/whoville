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


class RecommendationResponse(object):
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
        'recommendations': 'dict(str, VmTypeJson)',
        'virtual_machines': 'list[VmTypeJson]',
        'disk_responses': 'list[DiskResponse]'
    }

    attribute_map = {
        'recommendations': 'recommendations',
        'virtual_machines': 'virtualMachines',
        'disk_responses': 'diskResponses'
    }

    def __init__(self, recommendations=None, virtual_machines=None, disk_responses=None):
        """
        RecommendationResponse - a model defined in Swagger
        """

        self._recommendations = None
        self._virtual_machines = None
        self._disk_responses = None

        if recommendations is not None:
          self.recommendations = recommendations
        if virtual_machines is not None:
          self.virtual_machines = virtual_machines
        if disk_responses is not None:
          self.disk_responses = disk_responses

    @property
    def recommendations(self):
        """
        Gets the recommendations of this RecommendationResponse.

        :return: The recommendations of this RecommendationResponse.
        :rtype: dict(str, VmTypeJson)
        """
        return self._recommendations

    @recommendations.setter
    def recommendations(self, recommendations):
        """
        Sets the recommendations of this RecommendationResponse.

        :param recommendations: The recommendations of this RecommendationResponse.
        :type: dict(str, VmTypeJson)
        """

        self._recommendations = recommendations

    @property
    def virtual_machines(self):
        """
        Gets the virtual_machines of this RecommendationResponse.

        :return: The virtual_machines of this RecommendationResponse.
        :rtype: list[VmTypeJson]
        """
        return self._virtual_machines

    @virtual_machines.setter
    def virtual_machines(self, virtual_machines):
        """
        Sets the virtual_machines of this RecommendationResponse.

        :param virtual_machines: The virtual_machines of this RecommendationResponse.
        :type: list[VmTypeJson]
        """

        self._virtual_machines = virtual_machines

    @property
    def disk_responses(self):
        """
        Gets the disk_responses of this RecommendationResponse.

        :return: The disk_responses of this RecommendationResponse.
        :rtype: list[DiskResponse]
        """
        return self._disk_responses

    @disk_responses.setter
    def disk_responses(self, disk_responses):
        """
        Sets the disk_responses of this RecommendationResponse.

        :param disk_responses: The disk_responses of this RecommendationResponse.
        :type: list[DiskResponse]
        """

        self._disk_responses = disk_responses

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
        if not isinstance(other, RecommendationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
