import connexion
import six

from swagger_server.models.auth_body import AuthBody  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.inline_response201 import InlineResponse201  # noqa: E501
from swagger_server.models.inline_response2011 import InlineResponse2011  # noqa: E501
from swagger_server.models.inline_response401 import InlineResponse401  # noqa: E501
from swagger_server.models.item_iphonex_body import ItemIphonexBody  # noqa: E501
from swagger_server.models.item_iphonex_body1 import ItemIphonexBody1  # noqa: E501
from swagger_server.models.usersignup_body import UsersignupBody  # noqa: E501
from swagger_server import util


def auth_post(body=None):  # noqa: E501
    """auth_post

    Auto generated using Swagger Inspector # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2002
    """
    if connexion.request.is_json:
        body = AuthBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def item_apple_delete():  # noqa: E501
    """item_apple_delete

    Auto generated using Swagger Inspector # noqa: E501


    :rtype: InlineResponse201
    """
    return 'do some magic!'


def item_get():  # noqa: E501
    """item_get

    Auto generated using Swagger Inspector # noqa: E501


    :rtype: InlineResponse2011
    """
    return 'do some magic!'


def item_iphonex_get():  # noqa: E501
    """item_iphonex_get

    Auto generated using Swagger Inspector # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def item_iphonex_post(body=None):  # noqa: E501
    """item_iphonex_post

    Auto generated using Swagger Inspector # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = ItemIphonexBody1.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def item_iphonex_put(body=None):  # noqa: E501
    """item_iphonex_put

    Auto generated using Swagger Inspector # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = ItemIphonexBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def store_store1_delete():  # noqa: E501
    """store_store1_delete

    Auto generated using Swagger Inspector # noqa: E501


    :rtype: InlineResponse201
    """
    return 'do some magic!'


def store_store4_get():  # noqa: E501
    """store_store4_get

    Auto generated using Swagger Inspector # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def store_store4_post():  # noqa: E501
    """store_store4_post

    Auto generated using Swagger Inspector # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def usersignup_post(body=None):  # noqa: E501
    """usersignup_post

    Auto generated using Swagger Inspector # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse201
    """
    if connexion.request.is_json:
        body = UsersignupBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
