"""
Get file checksum.

. . .
"""
import hashlib
import os
import sys


class Check_calc():
    """Calculator checksum class."""

    def __init__(self):
        """Initialize method."""
        pass


# def get_file_size(path_file):
#     """Return file size function."""
#     return os.stat(path_file).st_size


# def main(path_file):
#     """Main function."""
#     size_file = get_file_size(path_file)
#     hash_md5 = hashlib.md5()
#     with open(path_file, "rb") as file:
#         if size_file > 4096:
#             for chunk in iter(lambda: file.read(4096), b''):
#                 hash_md5.update(chunk)
#         else:
#             hash_md5.update(file.read())

#     print(hash_md5.hexdigest())


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)

    # main(sys.argv[1])
