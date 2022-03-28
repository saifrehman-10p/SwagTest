# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_auth_post(self):
        """Test case for auth_post

        
        """
        body = AuthBody()
        response = self.client.open(
            '//auth',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_item_apple_delete(self):
        """Test case for item_apple_delete

        
        """
        response = self.client.open(
            '//item/apple',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_item_get(self):
        """Test case for item_get

        
        """
        response = self.client.open(
            '/item/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_item_iphonex_get(self):
        """Test case for item_iphonex_get

        
        """
        response = self.client.open(
            '//item/Iphonex',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_item_iphonex_post(self):
        """Test case for item_iphonex_post

        
        """
        body = ItemIphonexBody1()
        response = self.client.open(
            '//item/Iphonex',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_item_iphonex_put(self):
        """Test case for item_iphonex_put

        
        """
        body = ItemIphonexBody()
        response = self.client.open(
            '//item/Iphonex',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_store1_delete(self):
        """Test case for store_store1_delete

        
        """
        response = self.client.open(
            '//store/store1',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_store4_get(self):
        """Test case for store_store4_get

        
        """
        response = self.client.open(
            '//store/store4',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_store4_post(self):
        """Test case for store_store4_post

        
        """
        response = self.client.open(
            '//store/store4',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_usersignup_post(self):
        """Test case for usersignup_post

        
        """
        body = UsersignupBody()
        response = self.client.open(
            '///usersignup',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
