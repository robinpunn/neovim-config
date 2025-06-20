import os
import shutil
from utils import (
    load_plugins,
    save_plugins, 
    filter_plugins_by_name,
    prompt_yes_no,
    PLUGIN_DIR,
    LUA_PLUGINS_DIR,
    INIT_LUA_FILE
)
from backup import create_backup


def remove_plugins(
    names,
    force=False,
    backup=False,
    json=False,
    repo=False,
    config=False,
    require=False
):
    plugins = load_plugins()
    if not plugins:
        print("No plugins found in plugins.json")
        return

    if not force and not backup:
        if prompt_yes_no("Would you like to create a backup before removing"):
            create_backup()
    elif backup:
        create_backup()

    specific_flags = any([json, repo, config, require])

    for plugin in filter_plugins_by_name(plugins, names):
        name = plugin["name"]

        if specific_flags:
            if json:
                if force or prompt_yes_no(f"Remove plugin.json entry for '{name}'?"):
                    remove_plugin_from_json(plugins, name)
            if repo:
                if force or prompt_yes_no(f"Delete repo for '{name}'?"):
                    remove_plugin_repo(plugin)
            if config:
                if force or prompt_yes_no(f"Remove lua config file for '{name}'?"):
                    remove_lua_config(plugin)
            if require:
                if force or prompt_yes_no(f"Remove require() from init.lua for '{name}'?"):
                    remove_require_from_init(plugin)
        else:
            if force or prompt_yes_no(f"Remove plugin.json entry for '{name}'?"):
                remove_plugin_from_json(plugins, name)
            if force or prompt_yes_no(f"Delete repo for '{name}'?"):
                remove_plugin_repo(plugin)
            if force or prompt_yes_no(f"Remove lua config file for '{name}'?"):
                remove_lua_config(plugin)
            if force or prompt_yes_no(f"Remove require() from init.lua for '{name}'?"):
                remove_require_from_init(plugin)


def remove_plugin_from_json(plugins, name):
    updated = [p for p in plugins if p["name"] != name]
    save_plugins(updated)
    print(f"✅ Removed {name} from plugins.json")


def remove_plugin_repo(plugin):
    plugin_type = plugin.get("type", "start")
    path = os.path.join(PLUGIN_DIR, plugin_type, plugin["name"])
    if os.path.isdir(path):
        shutil.rmtree(path)
        print(f"✅ Deleted repo: {path}")
    else:
        print(f"⚠️ Repo not found: {path}")


def remove_lua_config(name):
    path = os.path.join(LUA_PLUGINS_DIR, f"{name}.lua")
    if os.path.isfile(path):
        os.remove(path)
        print(f"✅ Deleted lua config: {path}")
    else:
        print(f"⚠️ Lua config not found: {path}")


def remove_require_from_init(name):
    require_line = f'require("plugins.{name}")'
    if not os.path.isfile(INIT_LUA_FILE):
        print("⚠️ init.lua not found")
        return

    with open(INIT_LUA_FILE, "r") as f:
        lines = f.readlines()

    with open(INIT_LUA_FILE, "w") as f:
        for line in lines:
            if require_line not in line:
                f.write(line)

    print(f"✅ Removed require line from init.lua for '{name}'")


def delete_plugins_json(force=False):
    if not os.path.exists("plugins.json"):
        print("⚠️ plugins.json not found")
        return

    if force or prompt_yes_no("Are you sure you want to delete plugins.json? (y/n): "):
        try:
            os.remove("plugins.json")
            print("🗑️ Deleted plugins.json")
        except Exception as e:
            print(f"❌ Failed to delete plugins.json: {e}")


def remove_json_entry(name):
    plugins = load_plugins()
    if not plugins:
        print("⚠️ No plugins found in plugins.json")
        return
    remove_plugin_from_json(plugins, name)
