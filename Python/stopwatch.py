# -*- coding: utf-8 -*-
"""
Time class.

. . .
"""
import time


class Stopwatch():
    """Execute time stopwatch."""

    def __init__():
        """Initialize."""
        pass

    def start(self):
        """Stopwatch start method."""
        self.start = time.time()

    def end(self):
        """Stopwatch end method."""
        self.result = time.time() - self.start

    def get_result(self):
        """Return stopwatch result."""
        return self.result
