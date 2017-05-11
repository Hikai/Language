"""
Get file checksum.

. . .
"""
import hashlib
import os
import sys


class Checksum():
    """Calculator checksum class."""

    def __init__(self, path_file):
        """Initialize method."""
        self.path_file = path_file

    def get_size(self):
        """Method return file size."""
        return os.stat(self.path_file).st_size

    def get_file_hash(self):
        """Method return file checksum."""
        size_file = self.get_size()
        hash_md5 = hashlib.md5()

        with open(self.path_file, "rb") as target:
            if size_file > 4096:
                for chunk in iter(lambda: target.read(4096), b''):
                    hash_md5.update(chunk)
            else:
                hash_md5.update(target.read())

        return hash_md5.hexdigest()


def main(path_file):
    """Main function."""
    checksum_file = Checksum(path_file)
    print(checksum_file.get_file_hash())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit(1)

    main(sys.argv[1])
