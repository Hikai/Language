"""
Python a few second memory dump script.

. . . (windows)
"""
import subprocess


def check_process():
    """Process monitoring function."""
    cmd = "wmic process get description, executablepath, processid"
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

    return result.stdout


def main():
    """Main function."""
    for line in check_process():
        print(line)


if __name__ == "__main__":
    main()
