# Copyright 2015 nToklo Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

try:
    # Try to load first the Python 3 version
    from urllib.parse import urlencode
except:
    # Fallback to Python 2
    from urllib import urlencode

from .ntokloapi import NtokloAPIBase
from .exceptions import RequestError
from .utils import DictList


class Blacklist(NtokloAPIBase):

    def _build_querystring(self, products):

        """Build the querystring for the request.

        This method will create the required querystring for the blacklist to
        work.

        Args:
            products (list): The product IDs as a python list.

        Returns:
            String: A querystring ready to be tied to a URL/URI.

        .. note:: This private method will strip out any querstrings that have
                  no value. Otherwise the request and the signature would not
                  match.

        .. versionadded:: 0.1
        """
        qs_dict = DictList()
        for product in products:
            qs_dict['productId'] = product
        querystring = urlencode(qs_dict, True)
        return querystring

    def add(self, productid=[]):

        """Add a product to the blacklist so it doesn't get shown.

        Args:
            productid (list): List of product Ids to blacklist. Example: ['123','456']

        Raises:
            RequestError: In case the request couldn't be made or failed.

        Returns:
            String: Status code of the request. `204 No Content` is the
                    expected response.

        .. versionadded:: 0.1
        """
        method = "POST"
        uri = "/product/blacklist"
        url = "{}{}".format(self.api_endpoint, uri)
        querystring = self._build_querystring(productid)
        auth_token = self.get_token(uri + "?" + querystring, method)
        self.headers['Authorization'] = auth_token

        try:
            r = self.session.post(url, params=querystring, headers=self.headers)
            return r.status_code
        except Exception as e:
            raise RequestError(e)

    def remove(self, productid=[]):

        """Remove a product from the blacklist.

        This will remove a product or a list of products from the blacklist,
        allowing them to appear again on the recommendations to the user.

        Args:
            productid (list): List of product Ids to remove from the blacklist.
                       Example: ['123','456']

        Raises:
            RequestError: In case the request couldn't be made or failed.

        Returns:
            String: Status code of the request. `204 No Content` is the
                    expected response.

        .. versionadded:: 0.1
        """
        method = "DELETE"
        uri = "/product/blacklist"
        url = "{}{}".format(self.api_endpoint, uri)
        querystring = self._build_querystring(productid)
        auth_token = self.get_token(uri + "?" + querystring, method)
        self.headers['Authorization'] = auth_token

        try:
            r = self.session.delete(url, params=querystring, headers=self.headers)
            return r.status_code
        except Exception as e:
            raise RequestError(e)

    def list(self):

        """List the blacklisted products on an application.

        This method will list all the blacklisted products on a specific
        application.

        Raises:
            RequestError: In case the request couldn't be made or failed.

        Returns:
            JSON Object: JSON Object with the lsit of blacklisted elements.

        .. versionadded:: 0.1
        """

        method = "GET"
        uri = "/products/blacklist"
        url = "{}{}".format(self.api_endpoint, uri)
        auth_token = self.get_token(uri, method)
        self.headers['Authorization'] = auth_token

        try:
            r = self.session.get(url, headers=self.headers)
            return json.loads(r.text)
        except Exception as e:
            raise RequestError(e)
