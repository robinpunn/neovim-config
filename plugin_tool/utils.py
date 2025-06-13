import os
import json
import subprocess
from configparser import ConfigParser

HOME = os.path.expanduser("~")
PLUGIN_DIR = os.path.join(HOME, ".local", "share", "nvim", "site", "pack", "plugins")
CONFIG_DIR = os.path.join(HOME, ".config", "nvim", "plugin_tool")
BACKUP_DIR = os.path.join(CONFIG_DIR, "backups")
LUA_PLUGINS_DIR = os.path.join(HOME, ".config", "nvim", "lua", "plugins")
LUA_PLUGINS_CORE_DIR = os.path.join(HOME, ".config", "nvim", "lua", "core")
INIT_LUA_FILE = os.path.join(HOME, ".config", "nvim", "init.lua")
JSON_FILE = os.path.join(CONFIG_DIR, "plugins.json")


def load_plugins():
    if not os.path.exists(JSON_FILE):
        print("No plugins found in plugins.json")
        return []
    with open(JSON_FILE, "r") as f:
        return json.load(f)


def save_plugins(plugins):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(JSON_FILE, "w") as f:
        json.dump(plugins, f, indent=2)


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


def get_existing_plugins_by_type():
    found = []
    for plugin_type in ["start", "opt"]:
        dir_path = os.path.join(PLUGIN_DIR, plugin_type)
        if not os.path.exists(dir_path):
            continue
        for name in os.listdir(dir_path):
            full_path = os.path.join(dir_path, name)
            if os.path.isdir(full_path):
                found.append({
                    "name": name,
                    "type": plugin_type,
                    "path": full_path
                })
    return found


def get_orphaned_plugins(plugins=None):
    if plugins is None:
        plugins = load_plugins()
    existing_names = {p["name"] for p in get_existing_plugins_by_type()}
    orphaned_plugins = [
        plugin for plugin in plugins
        if plugin["name"] not in existing_names
    ]

    return orphaned_plugins, existing_names


def filter_plugins_by_name(plugins, names):
    return [p for p in plugins if p["name"] in names]


def plugin_exists_in_json(plugins, name):
    return any(p["name"] == name for p in plugins)


def run_build_steps(plugin, cwd=None):
    build_steps = plugin.get("build")
    if not build_steps:
        return

    if isinstance(build_steps, str):
        build_steps = [build_steps]

    for step in build_steps:
        step = step.strip()
        if step.startswith(":"):
            print(f"Running Neovim command '{step}' for {plugin['name']}...")
            subprocess.run(
                ["nvim", "--headless", "+silent", step, "+quit"],
                cwd=cwd or ".",
                check=True
            )
        else:
            print(f"Running shell command '{step}' for {plugin['name']}...")
            subprocess.run(step, shell=True, cwd=cwd or ".", check=True)
