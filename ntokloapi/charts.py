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
from collections import OrderedDict
try:
    # Try to load first the Python 3 version
    from urllib.parse import urlencode
except:
    # Fallback to Python 2
    from urllib import urlencode

from .ntokloapi import NtokloAPIBase
from .exceptions import RequestError


class Chart(NtokloAPIBase):

    def _clean_querystring(self, querystring):
        for key in querystring:
            if not querystring[key]:
                del querystring[key]
        return querystring

    def get(self, date='', scope='', value='', action='', tw='', maxitems=''):

        """Request the recommendations for the application.

        Args:
            date (str): (**optional**) The date for which to retrieve a chart.
                        The date should be an epoch timestamp in milliseconds,
                        truncated to midnight. Example: 1364169600000
            scope (str): (**optional**) A product attribute for which to scope
                         recommendations. For example scope=category will
                         consider the product category when returning
                         recommendations. Supports: category, manufacturer,
                         vendor.
            value (str): (**optional**) The value for the recommendation scope.
                         For example scope=category&value=shoes will consider
                         the shoe category when returning recommendations. The
                         value parameter can be any string value.
            action (str): (**optional**) Filters the requested chart by
                          conversion_funnel actions. If it's not specified then
                          the chart returned is all actions, equivalent to
                          action=all.
            tw (str): (**optional**) The time window for which the charts are
                      requested. If not specified then the chart returns daily
                      chart, equivalent to tw=DAILY. Supports: DAILY, WEEKLY.
            maxItems (str): (**optional**) The max number of items in the
                            charts. Default is 10. Valid range is 1-100.

        Raises:
            RequestError: In case the request couldn't be made or failed.

        Returns:
            JSON Object: A JSON object with the recommendation as "items" and
                         a "tracker_id"

        .. versionadded:: 0.1
        """
        method = "GET"
        uri = "/chart"
        url = "{}{}".format(self.api_endpoint, uri)
        qs_values = self._clean_querystring(OrderedDict(date=date, scope=scope,
                                                        value=value,
                                                        action=action, tw=tw,
                                                        maxItems=maxitems))
        querystring = urlencode(qs_values)
        auth_token = self.get_token(uri + "?" + querystring, method)
        self.headers['Authorization'] = auth_token

        try:
            r = self.session.get(url, params=querystring, headers=self.headers)
            return json.loads(r.text)
        except Exception as e:
            raise RequestError(e)
