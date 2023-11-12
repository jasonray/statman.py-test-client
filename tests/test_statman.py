import unittest
import pytest
from statman import Statman
import time

class TestStatman(unittest.TestCase):
    _accepted_variance = 0.1

    def test_stopwatch_via_statman(self):
        Statman.stopwatch('sw1', autostart=True)
        Statman.stopwatch('sw2', autostart=True)
        time.sleep(2)
        Statman.stopwatch('sw1').stop()
        elapsed = Statman.stopwatch('sw1').read(precision=1)
        self.assertAlmostEqual(elapsed, 2, delta=0.1)
        time.sleep(2)
        Statman.stopwatch('sw2').stop()
        elapsed = Statman.stopwatch('sw2').read()
        self.assertAlmostEqual(elapsed, 4, delta=0.1)
