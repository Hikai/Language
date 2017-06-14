# -*- coding: utf-8 -*-
"""
Exception global hook library.

@hikai
"""
import sys

def except_handler(except_type, value, traceback):
    """Exception handler function."""
	print("Exception:", except_type)
	print("Value:", value)
	print("Traceback:", traceback)

sys.excepthook = except_handler
