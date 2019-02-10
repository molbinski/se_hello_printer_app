from hello_world.formater import plain_text_upper_case
from hello_world.formater import plain_text_lower_case
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = plain_text_upper_case("WWIMIE", "EEEMSG")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_lower_case(self):
        l = plain_text_lower_case("WWIMIE", "EEEMSG")
        name = l.split(" ")[0]
        msg = l.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())
