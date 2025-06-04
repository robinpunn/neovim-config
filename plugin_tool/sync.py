import os
import json
import subprocess

PLUGIN_DIR = os.path.expanduser("~/.local/share/nvim/site/pack/plugins/")
JSON_FILE = "plugins.json"


def get_git_repo_url(plugin_path):
    try:
        result = subprocess.run(
            ["git", "-C", plugin_path, "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True,
        )
        url = result.stdout.strip()

        if "github.com" not in url:
            return None

        if url.startswith("git@github.com:"):
            url = url.replace("git@github.com:", "https://github.com/")
        elif url.startswith("git@github.com"):
            url = url.replace("git@github.com", "https://github.com/")
        elif url.startswith("https://github.com/"):
            pass
        else:
            return None

        if url.endswith(".git"):
            url = url[:-4]

        return url.split("github.com/")[1]
    except subprocess.CalledProcessError:
        return None


def has_docs_dir(plugin_path):
    return os.path.isdir(os.path.join(plugin_path, "doc"))


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
            build = ":helptags ALL" if has_docs_dir(plugin_path) else None

            if plugin is None:
                plugin_dict[name] = {
                    "name": name,
                    "type": plugin_type,
                    "repo": repo,
                }
                if build:
                    plugin_dict[name]["build"] = build
                new_count += 1
            else:
                updated = False
                if "repo" not in plugin and repo:
                    plugin["repo"] = repo
                    updated = True
                if "build" not in plugin and build:
                    plugin["build"] = build
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
