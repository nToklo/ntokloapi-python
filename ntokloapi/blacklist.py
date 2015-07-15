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
            products: The product IDs as a python list

        Exceptions:
            None

        Returns:
            A querystring ready to be tied to a URL/URI

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
            productid: List of product Ids to blacklist. Example: ['123','456']

        Exceptions:
            RequestError

        Returns:
            Status code of the request

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
            productid: List of product Ids to remove from the blacklist.
                       Example: ['123','456']

        Exceptions:
            RequestError

        Returns:
            Status code of the request, if the request went trough it should
            come back as 204 (No Content).

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
