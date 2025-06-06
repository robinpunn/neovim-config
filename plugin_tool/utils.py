import os
import json

CONFIG_DIR = os.path.expanduser("~/.config/nvim/plugin_tool")
JSON_FILE = os.path.join(CONFIG_DIR, "plugins.json")


def load_plugins():
    if not os.path.exists(JSON_FILE):
        print("No plugins found")
        return []
    with open(JSON_FILE, "r") as f:
        return json.load(f)


def save_plugins(plugins):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(JSON_FILE, "w") as f:
        json.dump(plugins, f, indent=2)
