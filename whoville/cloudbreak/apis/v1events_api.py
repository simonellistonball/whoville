# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class V1eventsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_events(self, **kwargs):
        """
        retrieve events by timestamp (long)
        Events are used to track stack creation initiated by cloudbreak users. Events are generated by the backend when resources requested by the user become available or unavailable
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_events(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int since:
        :return: list[CloudbreakEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_events_with_http_info(**kwargs)
        else:
            (data) = self.get_events_with_http_info(**kwargs)
            return data

    def get_events_with_http_info(self, **kwargs):
        """
        retrieve events by timestamp (long)
        Events are used to track stack creation initiated by cloudbreak users. Events are generated by the backend when resources requested by the user become available or unavailable
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_events_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int since:
        :return: list[CloudbreakEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'since' in params:
            query_params.append(('since', params['since']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v1/events', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CloudbreakEvent]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_events_by_s_tack_id(self, stack_id, **kwargs):
        """
        retrieve events by stackid (long)
        Events are used to track stack creation initiated by cloudbreak users. Events are generated by the backend when resources requested by the user become available or unavailable
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_events_by_s_tack_id(stack_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int stack_id: (required)
        :return: list[CloudbreakEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_events_by_s_tack_id_with_http_info(stack_id, **kwargs)
        else:
            (data) = self.get_events_by_s_tack_id_with_http_info(stack_id, **kwargs)
            return data

    def get_events_by_s_tack_id_with_http_info(self, stack_id, **kwargs):
        """
        retrieve events by stackid (long)
        Events are used to track stack creation initiated by cloudbreak users. Events are generated by the backend when resources requested by the user become available or unavailable
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_events_by_s_tack_id_with_http_info(stack_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int stack_id: (required)
        :return: list[CloudbreakEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stack_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events_by_s_tack_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stack_id' is set
        if ('stack_id' not in params) or (params['stack_id'] is None):
            raise ValueError("Missing the required parameter `stack_id` when calling `get_events_by_s_tack_id`")


        collection_formats = {}

        path_params = {}
        if 'stack_id' in params:
            path_params['stackId'] = params['stack_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v1/events/{stackId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[CloudbreakEvent]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_structured_events(self, stack_id, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_structured_events(stack_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int stack_id: (required)
        :return: list[StructuredEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_structured_events_with_http_info(stack_id, **kwargs)
        else:
            (data) = self.get_structured_events_with_http_info(stack_id, **kwargs)
            return data

    def get_structured_events_with_http_info(self, stack_id, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_structured_events_with_http_info(stack_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int stack_id: (required)
        :return: list[StructuredEvent]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stack_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_structured_events" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stack_id' is set
        if ('stack_id' not in params) or (params['stack_id'] is None):
            raise ValueError("Missing the required parameter `stack_id` when calling `get_structured_events`")


        collection_formats = {}

        path_params = {}
        if 'stack_id' in params:
            path_params['stackId'] = params['stack_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v1/events/struct/{stackId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[StructuredEvent]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_structured_events_zip(self, stack_id, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_structured_events_zip(stack_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int stack_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_structured_events_zip_with_http_info(stack_id, **kwargs)
        else:
            (data) = self.get_structured_events_zip_with_http_info(stack_id, **kwargs)
            return data

    def get_structured_events_zip_with_http_info(self, stack_id, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_structured_events_zip_with_http_info(stack_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int stack_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stack_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_structured_events_zip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stack_id' is set
        if ('stack_id' not in params) or (params['stack_id'] is None):
            raise ValueError("Missing the required parameter `stack_id` when calling `get_structured_events_zip`")


        collection_formats = {}

        path_params = {}
        if 'stack_id' in params:
            path_params['stackId'] = params['stack_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['tokenAuth']

        return self.api_client.call_api('/v1/events/struct/zip/{stackId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
