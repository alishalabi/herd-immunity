import unittest
# import virus.py
# Still need to install

from person import person


class PersonTest(unittest.TestCase):
    def test_is_alive_and_is_vaccinated(self):
        testPerson = Person()
        testPerson.is_vaccinated = True
        assert testPerson.is_vaccinated = True
        assert testPerson.is_alive = True

    def test_is_alive_and_is_not_vaccinated(self):
        testPerson = Person()
        testPerson.is_vaccinated = False
        assert testPerson.is_vaccinated = False
        assert testPerson.is_alive = True

    def test_did_survive_infection(self):
        testPerson = Person()
        testPerson.is_vaccinated = True
        testPerson(did_survive_infection)
        pass

# (self, _id, is_vaccinated, infected=None)
