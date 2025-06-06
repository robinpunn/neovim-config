import os
from utils import load_plugins, save_plugins, get_git_repo_url, PLUGIN_DIR


def sync_plugins():
    plugins = load_plugins()
    plugin_dict = {p["name"]: p for p in plugins}
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

    save_plugins(list(plugin_dict.values()))
    print(
        f"Sync complete. {new_count} new, {updated_count} updated plugin(s)"
    )
