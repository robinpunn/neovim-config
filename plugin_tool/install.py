from utils import (
    load_plugins,
    get_orphaned_plugins,
    filter_plugins_by_name,
    run_build_steps,
    PLUGIN_DIR
)
import subprocess
import os


def install_plugins(names=None, force=False, dry_run=False):
    all_plugins = load_plugins()

    orphaned_plugins, _ = get_orphaned_plugins(all_plugins)
    to_install = filter_plugins_by_name(orphaned_plugins, names) if names else orphaned_plugins

    if not to_install:
        print("Nothing to install.")
        return

    print(f"{len(to_install)} plugin(s) to install:")
    for plugin in to_install:
        print(f" - {plugin['name']}")

    if dry_run:
        print("\n Dry run: no plugins installed.")
        return

    for plugin in to_install:
        if not force:
            confirm = input(f"Install {plugin['name']}? (y/n): ").strip().lower()
            if confirm != "y":
                continue

        success = install_single_plugin(plugin)
        if success:
            print(f"Installed {plugin['name']}")
        else:
            print(f"Failed to install {plugin['name']}")


def install_single_plugin(plugin):
    plugin_type = plugin.get("type", "start")
    url = f"https://github.com/{plugin['repo']}.git"
    name = plugin['name']

    target_dir = os.path.join(PLUGIN_DIR, plugin_type, name)

    if os.path.exists(target_dir):
        print(f"{name} already exists at {target_dir}")
        return False

    try:
        subprocess.run(["git", "clone", url, target_dir], check=True)

        if plugin.get("tag"):
            subprocess.run(["git", "checkout", f"tags/{plugin['tag']}"], cwd=target_dir, check=True)
        elif plugin.get("branch"):
            subprocess.run(["git", "checkout", plugin['branch']], cwd=target_dir, check=True)

        run_build_steps(plugin, cwd=target_dir)

        config_dir = os.path.expanduser("~/.config/nvim/lua/plugins")
        os.makedirs(config_dir, exist_ok=True)
        config_path = os.path.join(config_dir, f"{name}.lua")

        if not os.path.exists(config_path):
            with open(config_path, "w") as f:
                f.write(f"-- Config for {name}\n")

        init_path = os.path.expanduser("~/.config/nvim/init.lua")
        require_line = f'require("plugins.{name}")'

        with open(init_path, "a+") as f:
            f.seek(0)
            contents = f.read()
            if require_line not in contents:
                f.write(f"\n{require_line}\n")

        subprocess.run(["nvim", "--headless", "+silent", ":helptags ALL", "+quit"], check=True)

        return True

    except subprocess.CalledProcessError as e:
        print(f"Error installing {name}: {e}")
        return False
