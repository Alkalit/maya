import unittest
import maya


class SimpleTest(unittest.TestCase):

    def test_rfc2822(self):
        r = maya.now().rfc2822()
        d = maya.MayaDT.from_rfc2822(r)
        assert r == d.rfc2822()

    def test_iso8601(self):
        r = maya.now().iso8601()
        d = maya.MayaDT.from_iso8601(r)
        assert r == d.iso8601()

    def test_human_when(self):
        r1 = maya.when('yesterday')
        r2 = maya.when('today')

        assert r2.day - r1.day == 1

    def test_dt_tz_translation(self):
        d1 = maya.now().datetime()
        d2 = maya.now().datetime(to_timezone='US/Eastern')
        assert d1.hour - d2.hour == 5

    def test_dt_tz_naive(self):
        d1 = maya.now().datetime(naive=True)
        assert d1.tzinfo is None

        d2 = maya.now().datetime(to_timezone='US/Eastern', naive=True)
        assert d2.tzinfo is None
        assert d1.hour - d2.hour == 5

    def test_random_date(self):
        d = maya.when('11-17-11')
        assert d.year == 2011
        assert d.month == 11
        assert d.day == 17

# rand_day = maya.when('2011-02-07', timezone='US/Eastern')


if __name__ == "__main__":
    unittest.main()
