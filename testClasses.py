import unittest


from classes import Lib, Lang, LibLang
import classes


first_expected = {}
second_expected = {}
third_expected = {}


class testClass(unittest.TestCase):
    def setUp(self):
        self.many_to_many = classes.getManyToMany()
        self.one_to_many = classes.getOneToMany()

    def test_first(self):
        self.assertEquals(classes.first(self.one_to_many), )
