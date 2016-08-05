# -*- coding: utf-8 -*-
"""
Flask auto create folder.

Jobs:
 - 'templates' folder create.
 - 'static' folder create.
 - '<filename>' file create.
"""
import os
import sys


def makedir(path):
    """Make folder."""
    try:
        os.makedirs(path)
    except OSError:
        print("{} create failed.".format(path))
    print("{} create success.".format(path))


def makefile(filename):
    """Make python script file."""
    with open(filename, 'w') as script:
        script.write(get_file_content())
        print("{} create success.".format(filename))


def get_file_content():
    """
    Flask base code.

    Return: flask base code.
    """
    base_code = """# -*- coding: utf-8 -*-
\"\"\"
Flask example.

To-do:
 -
\"\"\"
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    \"\"\"String return.\"\"\"
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()"""
    return base_code


def get_now_path():
    """
    Path of script file.

    Return: script path. (exclude script file.)
    """
    path = sys.argv[0]
    path = path[:path.rfind('\\') + 1]
    return path


def main(filename):
    """Main function."""
    path = get_now_path()
    makedir(path + "\\templates\\")
    makedir(path + "\\static\\")
    makefile(path + filename + ".py")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py filename")
        sys.exit()
    main(sys.argv[1])
