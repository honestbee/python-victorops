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


class ActiveIncidentInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, incident_number=None, start_time=None, current_phase=None, alert_count=None, last_alert_time=None, last_alert_id=None, entity_id=None, host=None, service=None, paged_users=None, paged_teams=None, transitions=None):
        """
        ActiveIncidentInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'incident_number': 'str',
            'start_time': 'str',
            'current_phase': 'str',
            'alert_count': 'float',
            'last_alert_time': 'str',
            'last_alert_id': 'str',
            'entity_id': 'str',
            'host': 'str',
            'service': 'str',
            'paged_users': 'list[str]',
            'paged_teams': 'list[str]',
            'transitions': 'list[IncidentTransition]'
        }

        self.attribute_map = {
            'incident_number': 'incidentNumber',
            'start_time': 'startTime',
            'current_phase': 'currentPhase',
            'alert_count': 'alertCount',
            'last_alert_time': 'lastAlertTime',
            'last_alert_id': 'lastAlertId',
            'entity_id': 'entityId',
            'host': 'host',
            'service': 'service',
            'paged_users': 'pagedUsers',
            'paged_teams': 'pagedTeams',
            'transitions': 'transitions'
        }

        self._incident_number = incident_number
        self._start_time = start_time
        self._current_phase = current_phase
        self._alert_count = alert_count
        self._last_alert_time = last_alert_time
        self._last_alert_id = last_alert_id
        self._entity_id = entity_id
        self._host = host
        self._service = service
        self._paged_users = paged_users
        self._paged_teams = paged_teams
        self._transitions = transitions

    @property
    def incident_number(self):
        """
        Gets the incident_number of this ActiveIncidentInfo.
        The VictorOps incident number

        :return: The incident_number of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._incident_number

    @incident_number.setter
    def incident_number(self, incident_number):
        """
        Sets the incident_number of this ActiveIncidentInfo.
        The VictorOps incident number

        :param incident_number: The incident_number of this ActiveIncidentInfo.
        :type: str
        """

        self._incident_number = incident_number

    @property
    def start_time(self):
        """
        Gets the start_time of this ActiveIncidentInfo.
        The time the incident started

        :return: The start_time of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this ActiveIncidentInfo.
        The time the incident started

        :param start_time: The start_time of this ActiveIncidentInfo.
        :type: str
        """

        self._start_time = start_time

    @property
    def current_phase(self):
        """
        Gets the current_phase of this ActiveIncidentInfo.
        The current phase of the incident \"resolved\", \"triggered\" or \"acknowledged\".

        :return: The current_phase of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._current_phase

    @current_phase.setter
    def current_phase(self, current_phase):
        """
        Sets the current_phase of this ActiveIncidentInfo.
        The current phase of the incident \"resolved\", \"triggered\" or \"acknowledged\".

        :param current_phase: The current_phase of this ActiveIncidentInfo.
        :type: str
        """

        self._current_phase = current_phase

    @property
    def alert_count(self):
        """
        Gets the alert_count of this ActiveIncidentInfo.
        The number of alerts received for this incident

        :return: The alert_count of this ActiveIncidentInfo.
        :rtype: float
        """
        return self._alert_count

    @alert_count.setter
    def alert_count(self, alert_count):
        """
        Sets the alert_count of this ActiveIncidentInfo.
        The number of alerts received for this incident

        :param alert_count: The alert_count of this ActiveIncidentInfo.
        :type: float
        """

        self._alert_count = alert_count

    @property
    def last_alert_time(self):
        """
        Gets the last_alert_time of this ActiveIncidentInfo.
        The time of the last alert received for the incident

        :return: The last_alert_time of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._last_alert_time

    @last_alert_time.setter
    def last_alert_time(self, last_alert_time):
        """
        Sets the last_alert_time of this ActiveIncidentInfo.
        The time of the last alert received for the incident

        :param last_alert_time: The last_alert_time of this ActiveIncidentInfo.
        :type: str
        """

        self._last_alert_time = last_alert_time

    @property
    def last_alert_id(self):
        """
        Gets the last_alert_id of this ActiveIncidentInfo.
        The unique id of the last alert for the incident

        :return: The last_alert_id of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._last_alert_id

    @last_alert_id.setter
    def last_alert_id(self, last_alert_id):
        """
        Sets the last_alert_id of this ActiveIncidentInfo.
        The unique id of the last alert for the incident

        :param last_alert_id: The last_alert_id of this ActiveIncidentInfo.
        :type: str
        """

        self._last_alert_id = last_alert_id

    @property
    def entity_id(self):
        """
        Gets the entity_id of this ActiveIncidentInfo.
        The unique identification of the entity being monitored that caused the incident

        :return: The entity_id of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ActiveIncidentInfo.
        The unique identification of the entity being monitored that caused the incident

        :param entity_id: The entity_id of this ActiveIncidentInfo.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def host(self):
        """
        Gets the host of this ActiveIncidentInfo.
        The host on which the incident occurred

        :return: The host of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this ActiveIncidentInfo.
        The host on which the incident occurred

        :param host: The host of this ActiveIncidentInfo.
        :type: str
        """

        self._host = host

    @property
    def service(self):
        """
        Gets the service of this ActiveIncidentInfo.
        The service name causing the incident (if any)

        :return: The service of this ActiveIncidentInfo.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this ActiveIncidentInfo.
        The service name causing the incident (if any)

        :param service: The service of this ActiveIncidentInfo.
        :type: str
        """

        self._service = service

    @property
    def paged_users(self):
        """
        Gets the paged_users of this ActiveIncidentInfo.
        The users that were paged for the incident.

        :return: The paged_users of this ActiveIncidentInfo.
        :rtype: list[str]
        """
        return self._paged_users

    @paged_users.setter
    def paged_users(self, paged_users):
        """
        Sets the paged_users of this ActiveIncidentInfo.
        The users that were paged for the incident.

        :param paged_users: The paged_users of this ActiveIncidentInfo.
        :type: list[str]
        """

        self._paged_users = paged_users

    @property
    def paged_teams(self):
        """
        Gets the paged_teams of this ActiveIncidentInfo.
        The teams that were paged for the incident

        :return: The paged_teams of this ActiveIncidentInfo.
        :rtype: list[str]
        """
        return self._paged_teams

    @paged_teams.setter
    def paged_teams(self, paged_teams):
        """
        Sets the paged_teams of this ActiveIncidentInfo.
        The teams that were paged for the incident

        :param paged_teams: The paged_teams of this ActiveIncidentInfo.
        :type: list[str]
        """

        self._paged_teams = paged_teams

    @property
    def transitions(self):
        """
        Gets the transitions of this ActiveIncidentInfo.
        Transitions of the incident state over time

        :return: The transitions of this ActiveIncidentInfo.
        :rtype: list[IncidentTransition]
        """
        return self._transitions

    @transitions.setter
    def transitions(self, transitions):
        """
        Sets the transitions of this ActiveIncidentInfo.
        Transitions of the incident state over time

        :param transitions: The transitions of this ActiveIncidentInfo.
        :type: list[IncidentTransition]
        """

        self._transitions = transitions

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
        if not isinstance(other, ActiveIncidentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other