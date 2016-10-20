"""
Base 64 decode and Hexlify.

/
"""
import base64
import binascii


original = "original"
unhex = binascii.hexlify(base64.b64decode(original))
to_hex = base64.b64encode(binascii.unhexlify(original))
