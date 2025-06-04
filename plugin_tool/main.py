import sys
from sync import sync_plugins

if __name__ == "__main__":
    if sys.argv[1] == "sync":
        sync_plugins()
