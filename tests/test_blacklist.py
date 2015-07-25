import unittest

import config as cfg
import ntokloapi


class BlacklistTest(unittest.TestCase):

    def setUp(self):

        """Setup method for the test.

        In this method we connect to the API through the connector and use that
        connection through the tests.
        """
        self.blacklist = ntokloapi.Blacklist(cfg.TEST_KEY, cfg.TEST_SECRET)

    def test_blacklist_add_singleitem(self):

        """
        Procedure: Send a single item to the API to be blacklisted.
        Verification: 204 No Content response from the API
        """
        response = self.blacklist.add(productid=['10201', ])
        assert response == 204

    def test_blacklist_add_multipleitems(self):

        """
        Procedure: Send multiple items to the API to be blacklisted.
        Verification: 204 No Content response from the API
        """
        response = self.blacklist.add(productid=['10202', '10203'])
        assert response == 204

    def test_blacklist_add_empty_elements(self):

        """
        Procedure: Send multiple elements, some of them empty to the API to be
                   blacklisted. We expect the connector to clear it.
        Verification: 204 No Content response from the API
        """
        response = self.blacklist.add(productid=['10204', '10205', '', ''])
        assert response == 204

    def test_blacklist_remove_singleitem(self):

        """
        Procedure: Remove on item from the blacklisted elements in the API.
        Verification: 204 No Content response from the API
        """
        response = self.blacklist.remove(productid=['10201', ])
        assert response == 204

    def test_blacklist_remove_multipleitems(self):

        """
        Procedure: Remove multiple items from the blacklisted elements in the
                   API.
        Verification: 204 No Content response from the API
        """
        response = self.blacklist.remove(productid=['10202', '10203'])
        assert response == 204

    def test_blacklist_remove_empty_elements(self):

        """
        Procedure: Remove multiple items from the blacklisted elements in the
                   API, some of them empty. We expect the connector to clear
                   it up.
        Verification: 204 No Content response from the API
        """
        response = self.blacklist.remove(productid=['10204', '10205', '', ''])
        assert response == 204

    def test_blacklist_show_items(self):

        """
        Procedure: Ask the API for the list of blacklisted elements in the API.
        Verification: Since the length of the returned list is variable, we
                      check that the returning data type is in fact, a list.
        """
        response = self.blacklist.list()
        assert isinstance(response, list)
