# coding: utf-8

"""
    Mock Server API

    MockServer enables easy mocking of any system you integrate with via HTTP or HTTPS with clients written in Java, JavaScript and Ruby and a simple REST API (as shown below).  MockServer Proxy is a proxy that introspects all proxied traffic including encrypted SSL traffic and supports Port Forwarding, Web Proxying (i.e. HTTP proxy), HTTPS Tunneling Proxying (using HTTP CONNECT) and SOCKS Proxying (i.e. dynamic port forwarding).  Both MockServer and the MockServer Proxy record all received requests so that it is possible to verify exactly what requests have been sent by the system under test.  # noqa: E501

    OpenAPI spec version: 5.3.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class HttpTemplate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'template_type': 'str',
        'template': 'str',
        'delay': 'Delay'
    }

    attribute_map = {
        'template_type': 'templateType',
        'template': 'template',
        'delay': 'delay'
    }

    def __init__(self, template_type=None, template=None, delay=None):  # noqa: E501
        """HttpTemplate - a model defined in OpenAPI"""  # noqa: E501

        self._template_type = None
        self._template = None
        self._delay = None
        self.discriminator = None

        if template_type is not None:
            self.template_type = template_type
        if template is not None:
            self.template = template
        if delay is not None:
            self.delay = delay

    @property
    def template_type(self):
        """Gets the template_type of this HttpTemplate.  # noqa: E501


        :return: The template_type of this HttpTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this HttpTemplate.


        :param template_type: The template_type of this HttpTemplate.  # noqa: E501
        :type: str
        """
        allowed_values = ["JAVASCRIPT", "VELOCITY"]  # noqa: E501
        if template_type not in allowed_values:
            raise ValueError(
                "Invalid value for `template_type` ({0}), must be one of {1}"  # noqa: E501
                .format(template_type, allowed_values)
            )

        self._template_type = template_type

    @property
    def template(self):
        """Gets the template of this HttpTemplate.  # noqa: E501


        :return: The template of this HttpTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this HttpTemplate.


        :param template: The template of this HttpTemplate.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def delay(self):
        """Gets the delay of this HttpTemplate.  # noqa: E501


        :return: The delay of this HttpTemplate.  # noqa: E501
        :rtype: Delay
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this HttpTemplate.


        :param delay: The delay of this HttpTemplate.  # noqa: E501
        :type: Delay
        """

        self._delay = delay

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HttpTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
