"""
Base 64 decode and Hexlify.

/
"""
import base64
import binascii


original = "example"
print(binascii.hexlify(base64.b64decode(original)))
