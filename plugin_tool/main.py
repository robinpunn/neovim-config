import sys
from scan import scan_plugins

if __name__ == "__main__":
    if sys.argv[1] == "scan":
        scan_plugins()
