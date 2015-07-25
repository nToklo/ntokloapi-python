import unittest

import config
from .. import ntokloapi


class BlacklistTest(unittest.TestCase):

    def setUp(self):
        self.blacklist = ntokloapi.Blacklist(config.TEST_KEY, config.TEST_SECRET)

    def test_blacklist_add_singleitem(self):

        response = self.blacklist.add(productid=['10201', ])
        assert response == "204"

    def test_blacklist_add_multipleitems(self):
        response = self.blacklist.add(productid=['10202', '10203'])
        assert response == "204"

    def test_blacklist_add_empty_elements(self):
        response = self.blacklist.add(productid=['10204', '10205', '', ''])
        assert response == "204"

    def test_blacklist_remove_singleitem(self):
        response = self.blacklist.remove(productid=['10201', ])
        assert response == "204"

    def test_blacklist_remove_multipleitems(self):
        response = self.blacklist.remove(productid=['10202', '10203'])
        assert response == "204"

    def test_blacklist_remove_empty_elements(self):
        response = self.blacklist.remove(productid=['10204', '10205', '', ''])
        assert response == "204"

    def test_blacklist_show_items(self):
        response = self.blacklist.list()
        assert not response
