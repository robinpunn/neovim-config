import os
import json

PLUGIN_DIRS = {
    "start": os.path.expanduser("~/.local/share/nvim/site/pack/plugins/start"),
    "opt": os.path.expanduser("~/.local/share/nvim/site/pack/plugins/opt")
}
JSON_FILE = "plugins.json"


def scan_plugins():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            existing_plugins = json.load(f)
    else:
        existing_plugins = []

    plugin_dict = {["name"]: p for p in existing_plugins}

    new_count = 0

    for plugin_type, directory in PLUGIN_DIRS.items():
        if not os.path.exists(directory):
            continue
        for name in os.listdir(directory):
            path = os.path.join(directory, name)
            if os.path.isdir(path):
                if name not in plugin_dict:
                    plugin_dict[name] = {
                        "name": name,
                        "type": plugin_type,
                        "tag": None,
                        "dependencies": []
                    }
                    new_count += 1

    with open(JSON_FILE, "w") as f:
        json.dump(list(plugin_dict.values()), f, indent=2)

    print(f"Scanned complete. {new_count} new plugin(s) plugins added to {JSON_FILE}")
