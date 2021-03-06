# coding: utf-8

"""
    VictorOps API

    This API allows you to interact with the VictorOps platform in various ways. Your account may be limited to a total number of API calls per month. Also, some of these API calls have rate limits.  NOTE: In this documentation when creating a sample curl request (clicking the TRY IT OUT! button), in some API viewing interfaces, the '@' in an email address may be encoded. Please note that the REST endpoints will not process the encoded version. Make sure that the encoded character '%40' is changed to its unencoded form before submitting the curl request. 

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AddUserPayload(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first_name=None, last_name=None, username=None, email=None, admin=None, expiration_hours=None):
        """
        AddUserPayload - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'last_name': 'str',
            'username': 'str',
            'email': 'str',
            'admin': 'bool',
            'expiration_hours': 'float'
        }

        self.attribute_map = {
            'first_name': 'firstName',
            'last_name': 'lastName',
            'username': 'username',
            'email': 'email',
            'admin': 'admin',
            'expiration_hours': 'expirationHours'
        }

        self._first_name = first_name
        self._last_name = last_name
        self._username = username
        self._email = email
        self._admin = admin
        self._expiration_hours = expiration_hours

    @property
    def first_name(self):
        """
        Gets the first_name of this AddUserPayload.

        :return: The first_name of this AddUserPayload.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this AddUserPayload.

        :param first_name: The first_name of this AddUserPayload.
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this AddUserPayload.

        :return: The last_name of this AddUserPayload.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this AddUserPayload.

        :param last_name: The last_name of this AddUserPayload.
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")

        self._last_name = last_name

    @property
    def username(self):
        """
        Gets the username of this AddUserPayload.

        :return: The username of this AddUserPayload.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this AddUserPayload.

        :param username: The username of this AddUserPayload.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def email(self):
        """
        Gets the email of this AddUserPayload.

        :return: The email of this AddUserPayload.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AddUserPayload.

        :param email: The email of this AddUserPayload.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def admin(self):
        """
        Gets the admin of this AddUserPayload.

        :return: The admin of this AddUserPayload.
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """
        Sets the admin of this AddUserPayload.

        :param admin: The admin of this AddUserPayload.
        :type: bool
        """

        self._admin = admin

    @property
    def expiration_hours(self):
        """
        Gets the expiration_hours of this AddUserPayload.
        The validity duration for the invitatation/set password link sent to the added user.

        :return: The expiration_hours of this AddUserPayload.
        :rtype: float
        """
        return self._expiration_hours

    @expiration_hours.setter
    def expiration_hours(self, expiration_hours):
        """
        Sets the expiration_hours of this AddUserPayload.
        The validity duration for the invitatation/set password link sent to the added user.

        :param expiration_hours: The expiration_hours of this AddUserPayload.
        :type: float
        """

        self._expiration_hours = expiration_hours

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
        if not isinstance(other, AddUserPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
