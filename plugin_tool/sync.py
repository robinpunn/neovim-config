import os
import json
from configparser import ConfigParser

CONFIG_DIR = os.path.expanduser("~/.config/nvim/plugin_tool")
JSON_FILE = os.path.join(CONFIG_DIR, "plugins.json")
PLUGIN_DIR = os.path.expanduser("~/.local/share/nvim/site/pack/plugins/")
os.makedirs(CONFIG_DIR, exist_ok=True)


def get_git_repo_url(plugin_path):
    config_path = os.path.join(plugin_path, ".git", "config")
    if not os.path.isfile(config_path):
        return None

    parser = ConfigParser()
    try:
        parser.read(config_path)
        url = parser.get('remote "origin"', "url")

        if url.startswith("git@github.com:"):
            url = url.replace("git@github.com:", "https://github.com/")
        if url.endswith(".git"):
            url = url[:-4]
        if "github.com/" in url:
            return url.split("github.com/")[1]
        return None
    except Exception:
        return None


def sync_plugins():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            existing_plugins = json.load(f)
    else:
        existing_plugins = []

    plugin_dict = {p["name"]: p for p in existing_plugins}
    new_count = 0
    updated_count = 0

    for plugin_type in ["start", "opt"]:
        dir_path = os.path.join(PLUGIN_DIR, plugin_type)
        if not os.path.exists(dir_path):
            continue

        for name in os.listdir(dir_path):
            plugin_path = os.path.join(dir_path, name)
            if not os.path.isdir(plugin_path):
                continue

            plugin = plugin_dict.get(name)
            repo = get_git_repo_url(plugin_path)

            if plugin is None:
                plugin_dict[name] = {
                    "name": name,
                    "type": plugin_type,
                    "repo": repo,
                }
                new_count += 1
            else:
                updated = False
                if "repo" not in plugin and repo:
                    plugin["repo"] = repo
                    updated = True
                if plugin.get("type") != plugin_type:
                    plugin["type"] = plugin_type
                    updated = True
                if updated:
                    updated_count += 1

    with open(JSON_FILE, "w") as f:
        json.dump(list(plugin_dict.values()), f, indent=2)

    print(
        f"Sync complete. {new_count} new, {updated_count} updated plugin(s)"
    )
